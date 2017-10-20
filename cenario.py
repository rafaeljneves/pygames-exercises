"""
exercícios de cenario.py

com pygames

1- criação de cenários isométricos
"""

import pygame

from pygame.locals import *

screenDimension = (600,600)
screen = pygame.display.set_mode(screenDimension,0,32)

house = pygame.image.load('static/img/isometric_house.png')
player = pygame.image.load('static/img/playerboy.png')
keys = [False, False, False, False]
player_pos = [220,300]

velocity    = 0.8
width_polyg = 0
width_line  = 42


while True:
    pygame.display.flip()
    screen.fill(0)

    pygame.draw.polygon(screen, (0,255,0), ( (10,250), (250,110),(500,250), (250,390), (10,250)  ),width_polyg)
    pygame.draw.line(screen, (170,150,0), (9,270), (250,410), width_line )
    pygame.draw.line(screen, (100,80, 0), (250, 410), (499, 270), width_line)

    screen.blit(house, (0,32 ))
    screen.blit(player, player_pos)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                keys[0] = True
            if event.key == K_UP:
                keys[1] = True
            if event.key == K_LEFT:
                keys[2] = True
            if event.key == K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                keys[0] = False
            if event.key == K_UP:
                keys[1] = False
            if event.key == K_LEFT:
                keys[2] = False
            if event.key == K_RIGHT:
                keys[3] = False



    if   keys[0]:
        player_pos[1] += velocity
    elif keys[1]:
        player_pos[1] -= velocity
    elif keys[2]:
        player_pos[0] -= velocity
    elif keys[3]:
        player_pos[0] += velocity


    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)