from filter import *

# defining median function
def median(data):
    data = sorted(data)
    index = len(data)/2
    return data[index]

img = open(sys.argv)
img.show()
img = filter(img, median)  #de-noising
img.show()
