# processing
pinpong
bx=285
by=150
bxs=0
bys=0
rx=10
ry=100
rx2=540
ry2=100
cx=10
cx2=40
cx3=70
cx4=300
cx5=330
cx6=360
i=0
i2=0
def setup():
    size(600,400)
def draw():
    global bx,by,bxs,bys,rx,ry,rx2,ry2,cx,cx2,cx3,cx4,cx5,cx6,i,i2
    fill(255,255,255)
    rect(0,0,1000,400)
    fill(39,157,77)
    rect(10,10,550,300)
    fill(224,9,88)
    rect(10,10,275,300)
    fill(0,0,100)
    triangle(255,310,315,310,285,280)
    fill(0,0,100)
    triangle(255,10,315,10,285,40)
    fill(58,250,98)
    rect(rx,ry,20,100)
    fill(13,255,100)
    rect(rx2,ry2,20,100)
    ellipse(bx,by,15,15)
    rect(cx,330,30,30)
    rect(cx2,330,30,30)
    rect(cx3,330,30,30)
    rect(cx4,330,30,30)
    rect(cx5,330,30,30)
    rect(cx6,330,30,30)
    bx+=bxs
    by+=bys
    if keyPressed:
        if key == 'p' and bxs == 0 and bys == 0:
            bxs=-2
            bys=2
        if key == 'w' and ry>=11:
            ry=ry-2
        if key =='s' and ry<=209:
            ry=ry+2
        if key =='o' and ry2>=11:
            ry2=ry2-2
        if key == 'l' and ry2<=209:
            ry2=ry2+2  
    if bx<=rx+28 and by<=ry+100 and bx>=rx and by>=ry:
        bxs=-bxs
    if bx>=rx2-6 and by>=ry2 and bx<=rx2 and by<=ry2+100:
        bxs=-bxs
    if bx<=19 and i == 0:
        bxs=0
        bys=0
        bx=285
        by=150
        cx=999
        i+=1
    if bx<=19 and i == 1:
        bxs=0
        bys=0
        bx=285
        by=150
        cx2=999
        i+=1
    if bx<=19 and i == 2:
        bxs=0
        bys=0
        bx=285
        by=150
        cx3=999
    if by<=18:
        bys=-bys
    if bx>=553 and i2 == 0:
        bxs=0
        bys=0
        bx=285
        by=150
        i2+=1
        cx4=999
    if bx>=553 and i2 == 1:
        bxs=0
        bys=0
        bx=285
        by=150
        i2+=1
        cx5=999
    if bx>=553 and i2 == 2:
        bxs=0
        bys=0
        bx=285
        by=150
        cx6=999
    if by>=297:
        bys=-bys
    if cx3 == 999:
        rect(0,0,600,400)
    if cx6 == 999:
        fill(0,0,0)
        rect(0,0,600,400)  
          
