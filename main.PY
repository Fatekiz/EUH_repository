import pygame
import sys
from config.settings import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((win_x,win_y))

    pygame.draw.rect(screen,BLANCO,((win_x//2)-20,(win_y//2)-20,40,40))
    pygame.display.set_caption("GAME")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

main()