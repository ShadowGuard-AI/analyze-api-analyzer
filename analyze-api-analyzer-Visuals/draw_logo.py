#!/usr/bin/env python3
"""analyze-api-analyzer logo: one hoisted signal ball straight on, name in Asul below."""
import math
from PIL import Image, ImageDraw, ImageFont
HERE=__file__.rsplit('/',1)[0]
W,H=960,700
HARBOR=(39,71,112); CREAM=(246,239,218); RUST=(178,72,46); ROPE=(193,161,108)
img=Image.new('RGB',(W,H),HARBOR); d=ImageDraw.Draw(img,'RGBA')
cx,cy,br=480,268,196
# halyard rises from the ring and leaves the top of the frame
d.line([(cx,0),(cx,cy-br-34)],fill=ROPE,width=10)
d.line([(cx,0),(cx,cy-br-34)],fill=(160,128,78),width=3)
# iron lifting ring
d.ellipse([cx-30,cy-br-44,cx+30,cy-br+16],outline=(52,50,48),width=11)
# the ball: harbor blue canvas sphere
d.ellipse([cx-br,cy-br,cx+br,cy+br],fill=(46,82,128),outline=(24,44,72),width=4)
# rust red band around the equator, last detail surrendered at small size
d.rectangle([cx-br,cy-30,cx+br,cy+30],fill=RUST)
d.ellipse([cx-br,cy-br,cx+br,cy+br],outline=(24,44,72),width=4)
# two rope tan seams meeting at the ring
for sgn in (-1,1):
    # seam arcs kept inside the ball by construction: ellipses narrower than the ball
    box=[cx-br*0.62 if sgn<0 else cx-br*0.18, cy-br, cx+br*0.18 if sgn<0 else cx+br*0.62, cy+br]
    d.arc(box,270,90 if sgn<0 else 90,fill=ROPE,width=8)
    d.arc(box,90,270 if sgn<0 else 270,fill=ROPE,width=8)
# canvas sheen
d.arc([cx-br+26,cy-br+30,cx+br-90,cy+br-110],205,305,fill=(110,152,196),width=13)
# name beneath, Asul in sail cream on harbor blue, spaced wide
f=ImageFont.truetype(HERE+'/fonts/Asul.ttf',44)
txt='analyze-api-analyzer'
# manual wide letterspacing
widths=[d.textlength(ch,font=f) for ch in txt]; gap=7
total=sum(widths)+gap*(len(txt)-1); x=(W-total)/2
for ch,wch in zip(txt,widths):
    d.text((x,566),ch,font=f,fill=CREAM); x+=wch+gap
d.line([(150,548),(810,548)],fill=ROPE,width=2)
img.save(HERE+'/logo.png')
# 64px survival check
img.resize((64,47)).save(HERE+'/scratch/logo64-ship.png')
print('saved logo')
