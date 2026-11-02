#!/usr/bin/env python3
"""analyze-api-analyzer intro banner: signal tower gallery at dawn before the hoist, scenery only, no text."""
import math, random
from PIL import Image, ImageDraw, ImageFilter
random.seed(11)
W,H=1200,520
HARBOR=(39,71,112); CREAM=(246,239,218); RUST=(178,72,46); ROPE=(193,161,108); GREEN=(62,110,96)
img=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(img,'RGBA')
# pale sail cream sky, morning light low from the right
for y in range(0,300):
    t=y/300; d.line([(0,y),(W,y)],fill=(int(246-10*t),int(239-8*t),int(218+6*t)))
# open sea in harbor blue with a bright track of sun running to the horizon
d.rectangle([0,268,W,392],fill=(66,104,138))
for i in range(46):
    x=760+random.uniform(-70,190); y=276+i*2.5; ln=random.uniform(8,64)*(1-i/70)
    d.line([(x,y),(x+ln,y)],fill=(250,240,205,190),width=2)
d.rectangle([0,262,W,268],fill=(88,124,156))
# breakwater line
d.polygon([(0,286),(430,278),(760,284),(760,296),(0,300)],fill=(96,90,80))
d.ellipse([742,272,760,290],fill=RUST)  # unlit beacon cap, no lettering anywhere
# moored boats: hulls and masts, softened by distance
def boat(x,y,s,hull):
    d.polygon([(x,y),(x+52*s,y),(x+40*s,y+11*s),(x+10*s,y+11*s)],fill=hull)
    d.line([(x+26*s,y),(x+26*s,y-38*s)],fill=(90,78,60),width=max(1,int(2*s)))
    d.polygon([(x+26*s,y-36*s),(x+26*s,y-4*s),(x+44*s,y-4*s)],fill=(240,234,210))
for bx,by,bs in [(110,296,1.35),(280,310,1.1),(500,302,1.2),(650,314,0.95)]:
    boat(bx,by,bs,(110,84,58))
# port rooftops in rope tan, first rooftops softened
for i,(x,w,h) in enumerate([(30,120,44),(170,150,58),(350,110,40),(880,140,50),(1050,130,42)]):
    d.rectangle([x,268-h,x+w,268],fill=(214,192,150))
    d.polygon([(x-6,268-h),(x+w/2,268-h-22),(x+w+6,268-h)],fill=ROPE)
d.rectangle([0,246,W,270],fill=(176,152,110))
# gallery rail across the midground
d.rectangle([0,392,W,404],fill=(110,84,56))
for x in range(18,W,44): d.rectangle([x,404,x+7,452],fill=(110,84,56))
d.rectangle([0,446,W,456],fill=(110,84,56))
d.rectangle([0,398,W,402],fill=RUST)  # rust red iron rail line
# yardarm beam across the top with two halyards
d.rectangle([0,44,W,60],fill=(96,74,48))
d.line([(700,60),(700,118)],fill=(70,56,38),width=3)  # empty halyard
d.polygon([(688,118),(712,118),(700,136)],outline=(60,48,34),width=3)  # its hook, swaying empty
# rolled charts tied with twine, stacked against the tower wall at left
d.rectangle([0,330,120,470],fill=(128,116,96))
for i in range(3):
    y=412-i*22; d.rounded_rectangle([18,y,108,y+16],7,fill=(232,220,188),outline=ROPE,width=2)
    d.line([(58,y),(58,y+16)],fill=RUST,width=2)
# oil lantern, cold and dark, hanging at the right of the rail
d.line([(1058,60),(1058,96)],fill=(70,56,38),width=3)
d.rectangle([1036,96,1080,142],outline=(52,46,40),width=3)
d.rectangle([1044,104,1072,134],fill=(70,72,76))
# foreground: weathered gallery boards at close quarters
d.rectangle([0,456,W,H],fill=(150,118,78))
for x in range(0,W,150): d.line([(x,456),(x,H)],fill=(118,90,56),width=3)
for _ in range(260):
    x,y=random.uniform(0,W),random.uniform(460,H); d.line([(x,y),(x+random.uniform(6,26),y)],fill=(128,98,62),width=1)
# coil of rope in a neat spiral on the boards
cx,cy=905,494
for r in range(60,10,-13):
    d.ellipse([cx-r,cy-r*0.42,cx+r,cy+r*0.42],outline=(160,126,74),width=5)
    d.ellipse([cx-r,cy-r*0.42,cx+r,cy+r*0.42],outline=(168,136,88),width=2)
# the signal ball hanging into the top of the frame, sharp focus
bx,by,br=470,118,82
d.line([(bx,44),(bx,by-br-16)],fill=(70,56,38),width=4)
d.ellipse([bx-13,by-br-20,bx+13,by-br+2],outline=(70,64,58),width=5)  # iron lifting ring
d.ellipse([bx-br,by-br,bx+br,by+br],fill=HARBOR,outline=(26,48,78),width=3)
d.rectangle([bx-br,by-13,bx+br,by+13],fill=RUST)  # rust red equator band
d.ellipse([bx-br,by-br,bx+br,by+br],outline=(26,48,78),width=3)
for a in (-38,38):  # rope tan seams meeting at the ring
    pts=[]
    for t in range(0,21):
        th=math.radians(-90+a*math.sin(t/20*math.pi)); pts.append((bx+br*math.cos(th)*0.98,by+br*math.sin(th)))
    d.line(pts,fill=ROPE,width=5)
d.arc([bx-br+8,by-br+10,bx+br-30,by+br-40],200,300,fill=(90,130,175),width=6)  # canvas sheen
img=img.filter(ImageFilter.GaussianBlur(0.4))
img.save(__file__.rsplit('/',1)[0]+'/intro-banner.png')
print('saved intro')
