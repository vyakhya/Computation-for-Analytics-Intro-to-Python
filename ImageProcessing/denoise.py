import sys
from PIL import Image

# defining median function
def median(data):
    data = sorted(data)
    index = len(data)/2
    return data[index]

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

# define region3x3 function here
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

filename = sys.argv[1]
img = Image.open(filename)

# defining denoise function
def denoise(img):
    imgdup = img.copy()
    width, height = img.size
    m = imgdup.load()
    for i in range(0,width):
        for j in range(0,height):
            r=region3x3(img, i, j)
            m[i,j]=median(r)
    return imgdup

if len(sys.argv) <= 1:
    print "missing image filename"
    sys.exit(1)

filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# calling denoise function
imgdup = denoise(img)
imgdup.show()