from filter import *

# defining avg function
def avg(data):
    return sum(data)/len(data)

img = open(sys.argv)
img.show()
img = filter(img, avg)  # blurring
img.show()
