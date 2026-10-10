#!/usr/bin/env python3
"""Compose quiet, platform-specific Chinese covers from a JSON brief and optional image assets.

This utility does not call any image-generation service. No font files are bundled.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont, ImageOps

SPECS = {
    "wechat": {"size": (900, 383), "top": 36, "margin": 42, "title_size": 54},
    "xhs": {"size": (1080, 1440), "top": 265, "margin": 84, "title_size": 94},
    "douyin": {"size": (1080, 1920), "top": 300, "margin": 90, "title_size": 99},
}
FONT_BOLD = [
    "/System/Library/Fonts/PingFang.ttc",  # macOS
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
FONT_REGULAR = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def load_font(size: int, bold: bool = False, override: str | None = None) -> ImageFont.FreeTypeFont:
    candidates = ([override] if override else []) + (FONT_BOLD if bold else FONT_REGULAR)
    for path in candidates:
        if path and Path(path).exists():
            try:
                return ImageFont.truetype(path, size, index=0)
            except OSError:
                pass
    raise RuntimeError("未找到中文字体。macOS 可用系统 PingFang；其他系统请安装 Noto Sans CJK 或在 JSON 里指定 font_path。")


def color(value: str) -> tuple[int, int, int]:
    raw = value.lstrip("#")
    if len(raw) != 6:
        raise ValueError(f"颜色格式必须为 #RRGGBB: {value}")
    return tuple(int(raw[i : i + 2], 16) for i in (0, 2, 4))


def fit_focal(src: Image.Image, size: tuple[int, int], focus: tuple[float, float]) -> Image.Image:
    w, h = size
    sw, sh = src.size
    scale = max(w / sw, h / sh)
    rw, rh = math.ceil(sw * scale), math.ceil(sh * scale)
    image = src.convert("RGB").resize((rw, rh), Image.Resampling.LANCZOS)
    x = max(0, min(rw - w, round(focus[0] * rw - w / 2)))
    y = max(0, min(rh - h, round(focus[1] * rh - h / 2)))
    return image.crop((x, y, x + w, y + h))


def font_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> float:
    return draw.textlength(text, font=font)


def wrap_text(draw: ImageDraw.ImageDraw, source: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines = []
    for paragraph in source.split("\n"):
        if not paragraph:
            if lines:
                lines.append("")
            continue
        line = ""
        for char in paragraph:
            candidate = line + char
            if line and font_width(draw, candidate, font) > max_width:
                lines.append(line.rstrip())
                line = char.lstrip()
            else:
                line = candidate
        if line:
            lines.append(line.rstrip())
    return lines


def resolve_path(spec_dir: Path, path: str | None) -> Path | None:
    if not path:
        return None
    candidate = Path(path).expanduser()
    return candidate if candidate.is_absolute() else (spec_dir / candidate).resolve()


def scrim(img: Image.Image, fg: tuple[int, int, int], region: tuple[int, int, int, int]) -> Image.Image:
    """Apply a restrained local translucent wash only when using a photographic background."""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    x0, y0, x1, y1 = region
    if sum(fg) < 390:
        wash = (246, 244, 238, 172)
    else:
        wash = (21, 21, 21, 150)
    for y in range(y0, min(y1, img.height)):
        # Uneven fade creates a softer transition than a rectangular textbox.
        t = (y - y0) / max(1, (y1 - y0))
        alpha = int(wash[3] * (1.0 - 0.52 * t))
        draw.line((x0, y, x1, y), fill=(*wash[:3], alpha))
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def draw_typography(img: Image.Image, key: str, cfg: dict[str, Any], theme: dict[str, str], has_photo: bool, font_path: str | None) -> Image.Image:
    title = str(cfg.get("headline") or "").strip()
    subtitle = str(cfg.get("subline") or "").strip()
    if not title and not subtitle:
        return img

    w, h = img.size
    defaults = SPECS[key]
    margin = int(cfg.get("margin", defaults["margin"]))
    position = cfg.get("text_position", "top" if key != "wechat" else "center")
    if position not in ("top", "center", "bottom"):
        raise ValueError(f"不支持 text_position={position}，仅 top/center/bottom")
    if key == "wechat":
        # Protect the middle square center crop if text is explicitly requested.
        max_width = min(w - 2 * margin, 347)
        align = "center"
    else:
        max_width = w - 2 * margin
        align = cfg.get("align", "left")
        if align not in ("left", "center"):
            raise ValueError("align 仅支持 left/center")

    draw = ImageDraw.Draw(img)
    fontsize = int(cfg.get("title_size", defaults["title_size"]))
    min_size = 34 if key != "wechat" else 25
    lines = []
    font = None
    if title:
        for size in range(fontsize, min_size - 1, -2):
            test_font = load_font(size, bold=True, override=font_path)
            test_lines = wrap_text(draw, title, test_font, max_width)
            if len(test_lines) <= 2:
                font = test_font
                lines = test_lines
                break
        if font is None:
            raise ValueError(f"[{key}] 标题太长，无法在两行内排版，请缩短到适合封面阅读的长度：{title!r}")

    size = font.size if font else defaults["title_size"]
    line_gap = round(size * 0.19)
    line_height = round(size * 1.28)
    subfont = load_font(round(size * 0.36), bold=False, override=font_path)
    if subtitle and len(wrap_text(draw, subtitle, subfont, max_width)) > 1:
        raise ValueError(f"[{key}] 副标题太长：{subtitle!r}")
    block_h = len(lines) * line_height + (round(size * 0.5) + round(subfont.size * 1.35) if subtitle else 0)
    if position == "top":
        y = defaults["top"]
    elif position == "bottom":
        y = h - int(h * (0.2 if key == "wechat" else 0.23)) - block_h
    else:
        y = (h - block_h) // 2
    if key == "douyin":
        y = max(200, min(y, h - block_h - 360))
    elif key == "xhs":
        y = max(160, min(y, h - block_h - 180))

    foreground = color(theme.get("foreground", "#191919"))
    if has_photo and cfg.get("scrim", True):
        pad_y = int(size * 0.6)
        img = scrim(img, foreground, (0, max(0, y - pad_y), w, min(h, y + block_h + pad_y)))
        draw = ImageDraw.Draw(img)

    x = w // 2 if align == "center" else margin
    for line in lines:
        draw.text((x, y), line, font=font, fill=foreground, anchor="mt" if align == "center" else "lt")
        y += line_height
    if subtitle:
        y += round(size * 0.5)
        draw.text((x, y), subtitle, font=subfont, fill=color(theme.get("accent", "#777777")), anchor="mt" if align == "center" else "lt")
    return img


def save_previews(img: Image.Image, key: str, out: Path, debug: bool) -> None:
    w, h = img.size
    if key in ("wechat", "xhs"):
        side = min(w, h)
        x = (w - side) // 2
        y = (h - side) // 2
        square = img.crop((x, y, x + side, y + side))
        square.save(out / f"preview-{key}-square.png", optimize=True)
    if debug:
        vis = img.convert("RGBA")
        over = Image.new("RGBA", img.size)
        draw = ImageDraw.Draw(over)
        if key in ("wechat", "xhs"):
            side = min(w, h)
            x, y = (w - side) // 2, (h - side) // 2
            draw.rectangle((x, y, x + side - 1, y + side - 1), outline=(216, 66, 66, 220), width=4)
        if key == "douyin":
            draw.rectangle((50, 230, w - 50, h - 330), outline=(216, 66, 66, 200), width=4)
            draw.rectangle((0, 0, w, 230), fill=(0, 0, 0, 55))
            draw.rectangle((0, h - 330, w, h), fill=(0, 0, 0, 55))
        Image.alpha_composite(vis, over).convert("RGB").save(out / f"debug-{key}.png", optimize=True)


def render(spec: dict[str, Any], base_dir: Path, out: Path, debug: bool) -> None:
    platforms = spec.get("platforms")
    if not isinstance(platforms, dict) or not platforms:
        raise ValueError("JSON 必须包含 platforms，如 {\"wechat\":{}, \"xhs\":{}, \"douyin\":{}}")
    theme = spec.get("palette", {})
    bg_color = color(theme.get("background", "#F3F0E9"))
    fp = spec.get("focus", [0.5, 0.5])
    if len(fp) != 2 or any(not 0 <= float(q) <= 1 for q in fp):
        raise ValueError("focus 必须是两个 0~1 数字，如 [0.5,0.5]")
    font_path = spec.get("font_path")
    if font_path:
        full_font = resolve_path(base_dir, font_path)
        font_path = str(full_font)
        if not full_font or not full_font.is_file():
            raise FileNotFoundError(f"字体不存在：{full_font}")
    out.mkdir(parents=True, exist_ok=True)
    for key, raw_cfg in platforms.items():
        if key not in SPECS:
            raise ValueError(f"未知平台 {key!r}，支持 {list(SPECS)}")
        cfg = raw_cfg or {}
        size = SPECS[key]["size"]
        bg_path = resolve_path(base_dir, cfg.get("background") or spec.get("background"))
        has_photo = bg_path is not None
        if not has_photo and not str(cfg.get("headline") or "").strip() and not str(cfg.get("subline") or "").strip():
            raise ValueError(f"[{key}] 没有背景素材且没有文字，会得到空白封面；请先提供背景图，或为纯排版封面设置 headline")
        if bg_path is not None:
            if not bg_path.is_file():
                raise FileNotFoundError(f"[{key}] 背景图不存在：{bg_path}")
            with Image.open(bg_path) as source:
                override_focus = cfg.get("focus", fp)
                if len(override_focus) != 2 or any(not 0 <= float(q) <= 1 for q in override_focus):
                    raise ValueError("focus 必须是两个 0~1 数字")
                img = fit_focal(ImageOps.exif_transpose(source), size, tuple(map(float, override_focus)))
        else:
            img = Image.new("RGB", size, bg_color)
        img = draw_typography(img, key, cfg, theme, has_photo, font_path)
        filename = out / f"cover-{key}.png"
        img.save(filename, optimize=True)
        save_previews(img, key, out, debug)
        print(f"✓ {filename}: {size[0]}x{size[1]}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Editorial Cover: PNG composition and safe-area previews")
    parser.add_argument("--spec", required=True, help="JSON 配置文件")
    parser.add_argument("--out", required=True, help="输出目录")
    parser.add_argument("--debug", action="store_true", help="输出安全区视觉检查图")
    args = parser.parse_args()
    spec_path = Path(args.spec).expanduser().resolve()
    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        render(spec, spec_path.parent, Path(args.out).expanduser(), args.debug)
        return 0
    except (ValueError, RuntimeError, FileNotFoundError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
