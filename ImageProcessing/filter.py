import sys
from PIL import Image

# defining getpixel function
def getpixel(img, x, y):
    width, height = img.size
    if x < 0:
        x = 0
    if x >= width:
        x = width - 1
    if y < 0:
        y = 0
    if y >= height:
        y = height - 1
    m1 = img.load()
    return m1[x,y]

# defining function region3x3
def region3x3(img, x, y):
    me=getpixel(img,x,y)
    N=getpixel(img,x,y-1)
    S=getpixel(img,x,y+1)
    E=getpixel(img,x+1,y)
    W=getpixel(img,x-1,y)
    NE=getpixel(img,x+1,y+1)
    SE=getpixel(img,x+1,y-1)
    NW=getpixel(img,x-1,y+1)
    SW=getpixel(img,x-1,y-1)
    return [me,N,S,E,W,NE,SE,NW,SW]

#defining function open that opens the file and checks for missing file name
def open(argv):
    if len(argv) <= 1:
        print "Missing Image Filename!"
        sys.exit(1)
    img = Image.open(argv[1])
    img = img.convert("L")
    return img

#defining function filter
def filter(img, f):
    imgdup = img.copy()
    width, height = imgdup.size
    m = imgdup.load()
    for i in range(0, width):
        for j in range(0, height):
            r = region3x3(img, i, j)
            m[i,j] = f(r)
    return imgdup