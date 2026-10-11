from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

base = Path(__file__).parent
out = base / 'background-wechat.png'
W, H = 1800, 766
im = Image.new('RGB', (W, H), '#101821')
d = ImageDraw.Draw(im)
# The unmodified App Store icon identifies the platform without inventing UI.
icon = Image.open(base / 'app-store-icon.png').convert('RGBA')
icon = icon.resize((180, 180), Image.Resampling.LANCZOS)
im.paste(icon, ((W - icon.width) // 2, 92), icon)
# The exact rejection code, rather than an explanatory headline, is the focal object.
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 248)
label = '4.3(a)'
box = d.textbbox((0, 0), label, font=font)
x = (W - (box[2] - box[0])) // 2
d.text((x, 285), label, font=font, fill='#F26A55')
im.save(out, optimize=True)
