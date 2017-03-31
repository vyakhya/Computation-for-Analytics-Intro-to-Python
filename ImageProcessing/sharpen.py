from filter import *

# defining laplace function
def laplace(data):
    return data[1] + data[2] + data[3] + data[4] - 4 * data[0]

def minus(A, B):
    width, height = A.size
    m1 = A.load()
    m2 = B.load()
    for i in range(0,width):
        for j in range(0,height):
            r=region3x3(img, i, j)
            m1[i, j] = m1[i, j] - m2[i, j]
    return A

img = open(sys.argv)
img.show()
edges = filter(img, laplace)  # highlighting edges
sharpened = minus(img, edges)
sharpened.show()
