#!/usr/bin/env python3
"""analyze-api-analyzer wordmark banner: signal tower above the harbor at morning, name on the gallery board."""
import math, random
from PIL import Image, ImageDraw, ImageFont
random.seed(29)
HERE=__file__.rsplit('/',1)[0]
W,H=1400,560
HARBOR=(39,71,112); CREAM=(246,239,218); RUST=(178,72,46); ROPE=(193,161,108)
img=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(img,'RGBA')
for y in range(0,330):
    t=y/330; d.line([(0,y),(W,y)],fill=(int(246-8*t),int(239-6*t),int(218+8*t)))
# open sea beyond the breakwater, bright road of low sun from the right
d.rectangle([0,360,W,H],fill=(62,100,134))
for i in range(52):
    x=900+random.uniform(-60,260); y=372+i*3.4; ln=random.uniform(10,80)*(1-i/80)
    d.line([(x,y),(x+ln,y)],fill=(250,240,205,190),width=2)
d.polygon([(430,392),(1400,384),(1400,398),(430,404)],fill=(96,90,80))
# port below: warehouse roofs in rope tan, moored hulls, anchor chains into green water
for x,w,h in [(520,150,52),(700,180,64),(910,140,48),(1080,190,58),(1300,90,44)]:
    d.rectangle([x,360-h,x+w,360],fill=(216,194,152))
    d.polygon([(x-6,360-h),(x+w/2,360-h-24),(x+w+6,360-h)],fill=ROPE)
for x,y,s in [(560,428,1.1),(760,448,0.9),(1010,432,1.2),(1240,452,0.85)]:
    d.polygon([(x,y),(x+56*s,y),(x+44*s,y+12*s),(x+10*s,y+12*s)],fill=(110,84,58))
    d.line([(x+28*s,y),(x+28*s,y-36*s)],fill=(90,78,60),width=2)
    d.line([(x+6,y+10),(x-8,y+34)],fill=(60,80,74),width=2)  # anchor chain down into green water
d.rectangle([430,505,1400,560],fill=(58,102,92,110))
# stone tower left of center
d.rectangle([90,120,430,560],fill=(168,156,134))
for yy in range(140,560,44):
    d.line([(90,yy),(430,yy)],fill=(140,128,106),width=3)
    for xx in range(120,430,76): d.line([(xx+(yy//44%2)*30,yy),(xx+(yy//44%2)*30,yy+44)],fill=(140,128,106),width=2)
d.rectangle([70,96,450,124],fill=(110,84,56))  # gallery floor
# gallery railed in rust red iron
for x in range(84,448,36): d.rectangle([x,58,x+6,98],fill=RUST)
d.rectangle([70,52,450,60],fill=RUST)
# gallery board across the tower face, harbor blue, the one board with the name
d.rectangle([86,150,434,232],fill=HARBOR,outline=ROPE,width=4)
f=ImageFont.truetype(HERE+'/fonts/Asul.ttf',37)
txt='analyze-api-analyzer'
tw=d.textlength(txt,font=f); d.text(((260-tw/2),172),txt,font=f,fill=CREAM)
# yardarm and two signal balls at different heights: one high and clear, one lowered halfway
d.rectangle([40,34,700,48],fill=(96,74,48))
def ball(cx,cy,br):
    d.line([(cx,48),(cx,cy-br-12)],fill=(70,56,38),width=3)
    d.ellipse([cx-10,cy-br-16,cx+10,cy-br+4],outline=(52,50,48),width=4)
    d.ellipse([cx-br,cy-br,cx+br,cy+br],fill=(46,82,128),outline=(24,44,72),width=3)
    d.rectangle([cx-br,cy-9,cx+br,cy+9],fill=RUST)
    d.ellipse([cx-br,cy-br,cx+br,cy+br],outline=(24,44,72),width=3)
    d.arc([cx-br,cy-br,cx+br,cy+br],250,340,fill=ROPE,width=4)
ball(560,96,38)    # high and clear
ball(648,190,38)   # lowered halfway: a state changed, a state pending
# signal flags in sail cream and rust red on a separate halyard, stiff in the wind
d.line([(716,20),(716,240)],fill=(70,56,38),width=3)
for i,(fy,col) in enumerate([(52,CREAM),(104,RUST),(156,CREAM)]):
    d.polygon([(716,fy),(716+84,fy+13),(716,fy+28)],fill=col,outline=(150,130,90))
# coiled rope, rolled charts, unlit oil lantern on the gallery floor
for r in range(30,6,-8): d.ellipse([150-r,86-r*0.4,150+r,86+r*0.4],outline=ROPE,width=5)
for i in range(3):
    d.rounded_rectangle([300,74-i*13,368,84-i*13],5,fill=(232,220,188),outline=ROPE,width=2)
d.rectangle([392,64,420,94],outline=(52,46,40),width=3); d.rectangle([398,70,414,88],fill=(70,72,76))
img.save(HERE+'/banner.png')
print('saved banner')
