#   Author: Adam Cherochak 20161026
#   Purpose: Halloween Scary Pop-up
#   Detail: this program displays a full-screen image
#           the user is encouraged to find differences
#           the program will call a scary sound file and
#           change the image to something scary
#   SOURCE: https://www.raspberrypi.org/learning/scary-spot-the-difference/worksheet/

import pygame
from pygame.locals import*
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height), FULLSCREEN)

difference = pygame.image.load('spot_the_diff.png')
difference = pygame.transform.scale(difference, (width, height))

screen.blit(difference, (0,0))
pygame.display.update()

zombie = pygame.image.load('scary_face.png')
zombie = pygame.transform.scale(zombie, (width, height))

scream = pygame.mixer.Sound("scream.wav")

sleep(randrange(5,15))

scream.play()
sleep(0.4)
screen.blit(zombie, (0,0))
pygame.display.update()

sleep(3)
scream.stop()
pygame.quit()
