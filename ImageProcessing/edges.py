from filter import *

# defining laplace function
def laplace(data):
    return data[1] + data[2] + data[3] + data[4] - 4 * data[0]

img = open(sys.argv)
img.show()
edges = filter(img, laplace)  #highlighting edges
edges.show()