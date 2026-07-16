#!/usr/bin/env python3
"""Sample merk-kleuren pixel-exact uit een screenshot van een referentiedeck.

Gebruik:
  python3 sample_colours.py slide.png                 # top-8 dominante kleuren (quantize)
  python3 sample_colours.py slide.png X1 Y1 X2 Y2     # meest-verzadigde kleur in een crop (accent)

Tip: draai eerst zonder crop voor de palet-basis (navy/wit/cream), daarna met crops op
labels/accenten voor de exacte amber/rood.
"""
import sys, collections, colorsys
from PIL import Image

im = Image.open(sys.argv[1]).convert("RGB")
if len(sys.argv) >= 6:
    x1, y1, x2, y2 = map(int, sys.argv[2:6])
    crop = im.crop((x1, y1, x2, y2))
    best, bs = None, -1
    for r, g, b in crop.getdata():
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        if s > bs and v > 0.35:
            bs, best = s, (r, g, b)
    print(f"meest-verzadigd in crop: #{best[0]:02X}{best[1]:02X}{best[2]:02X}  rgb{best}")
else:
    q = im.resize((160, 90)).quantize(colors=8).convert("RGB")
    cnt = collections.Counter(q.getdata())
    print(f"top-8 kleuren van {sys.argv[1]} ({im.size[0]}x{im.size[1]}):")
    for (r, g, b), n in cnt.most_common(8):
        print(f"  #{r:02X}{g:02X}{b:02X}  {100*n/(160*90):4.1f}%")
