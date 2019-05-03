import sys
import cv2
import numpy as np
 

# my stuff
#image = pygame.image.load(sys.argv[1])

# get total number of frames
film = cv2.VideoCapture(sys.argv[1])

totalFrames = int(film.get(cv2.CAP_PROP_FRAME_COUNT))
print totalFrames
width = int(film.get(3))   # float
height = int(film.get(4)) # float

image = film.read(0)
for i in xrange(1, (totalFrames-1)):
    img = film.read(i)
    for x in xrange(0, height):
        print ("Frame:")
        print (i)
        print ("/")
        print (totalFrames)
        print ("---")
        print ("Row:")
        print (x+1)
        print ("/")
        print (height)
        print ("-----------")
        for y in xrange(0, width):
            pixel = img[1][x][y]
            color = (pixel[0]+pixel[1]+pixel[2])/3
            img[1][x][y] = [color,color,color]
print ("DONE!")

print image
film.write
ha = cv2.imwrite("./"+sys.argv[2],imgggg)
print ha