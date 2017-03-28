import sys
from PIL import Image
if len(sys.argv) != 2:
    print "$ python view.py imagename.png"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

