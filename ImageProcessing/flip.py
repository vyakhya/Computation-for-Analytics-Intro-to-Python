import sys
from PIL import Image

# defining flip function
def flip(img):
    imgdup = img.copy()
    width, height = img.size
    m1 = img.load()
    m2 = imgdup.load()
    for i in range(0,width):
        for j in range(0,height):
            m2[i,j]=m1[width-i-1,j]
    return imgdup

if len(sys.argv) <= 1:
    print "missing image filename"
    sys.exit(1)

filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# calling flip function
imgdup = flip(img)
imgdup.show()

