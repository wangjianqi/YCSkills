from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

out = Path(__file__).parent / 'background-wechat.png'
W, H = 1800, 766
im = Image.new('RGB', (W, H), '#101821')
d = ImageDraw.Draw(im)
# Narrow rails give the composition energy without imitating an App Store screen.
d.rectangle((0, 0, 25, H), fill='#E95C4B')
d.line((64, 102, 1736, 102), fill='#34414B', width=2)
d.line((64, 668, 1736, 668), fill='#34414B', width=2)
# The actual rejection code is the focal object, rendered deterministically.
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 214)
label = '4.3(a)'
box = d.textbbox((0, 0), label, font=font)
x = (W - (box[2] - box[0])) // 2
d.text((x, 95), label, font=font, fill='#F26A55')
# A short underline anchors the exact code to the article, not to an invented UI.
d.rounded_rectangle((W//2-125, 337, W//2+125, 349), radius=6, fill='#F26A55')
im.save(out, optimize=True)
