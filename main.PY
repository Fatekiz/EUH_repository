import pygame
import sys
from config.settings import *
from core.sprites import guerrero

def main():
    pygame.init()
    screen = pygame.display.set_mode((win_x,win_y))
    pygame.display.set_caption("GAME")


    pj_warrior=Guerrero()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.fill(NEGRO)
        


        pygame.display.flip() 


        


main()