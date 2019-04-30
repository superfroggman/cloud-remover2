import pygame
import sys
import cv2
import numpy as np

pygame.init()
 

# my stuff
#image = pygame.image.load(sys.argv[1])

# get total number of frames
cap = cv2.VideoCapture('youve_been_gnomed.mp4')

totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
totalFrames = int(totalFrames)
image = cap.read(0)
print totalFrames   
for i in xrange(0, (totalFrames)):
    img = cap.read(i)
    for x in xrange(0, image.get_rect().size[0]):
        print (x+1)
        print ("/")
        print (image.get_rect().size[0])
        print ("-----------")
        for y in xrange(0, image.get_rect().size[1]):
            pixel = img.get_at((x, y))
            color = (pixel[0]+pixel[1]+pixel[2])/3
            image.set_at((x,y), (color,color,color))
print ("DONE!")

pygame.image.save(image, sys.argv[2])