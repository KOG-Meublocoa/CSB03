# import pygame, sys
# from pygame.locals import *

# pygame.init()

# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello world!')

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     # DISPLAYSURF.fill((255, 255, 255))
#     # pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (100, 80, 150, 50))
#     # pygame.display.update()


import pygame

pygame.init

screen_height = 600
screen_width = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong game")

ball_image=pygame.image.load('assets/ball.png')
paddle_image=pygame.image.load('asssets/paddle.png')

ball_x=screen_width/2
ball_y=screen_height/2

player1_x =5
player1_y = screen_height/2

player2_x = 590
player2_y = screen_height/2


w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False

pygame.time.Clock()
fps = 60


loop = True
event = pygame.event.get

while loop:
    event.get