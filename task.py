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
def setup():
    size(600,400)
def draw():
    global bx,by,bxs,bys,rx,ry,rx2,ry2
    rect(10,10,550,300)
    rect(10,10,275,300)
    triangle(255,310,315,310,285,280)
    triangle(255,10,315,10,285,40)
    rect(rx,ry,20,100)
    rect(rx2,ry2,20,100)
    ellipse(bx,by,15,15)
    bx+=bxs
    by+=bys
    if keyPressed:
        if key == 'p':
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
    if bx<=rx+20 and by<=ry+100 and bx>=rx and by>=ry:
        bxs=-bxs
    if bx>=rx2 and by>=ry2 and bx<=rx2+20 and by<=ry2+100:
        bxs=-bxs
    if bx<=19:
        bxs=0
        bys=0
        bx=285
        by=150
    if by<=18:
        bys=-bys
    if bx>=553:
        bxs=0
        bys=0
        bx=285
        by=150
    if by>=297:
        bys=-bys  
