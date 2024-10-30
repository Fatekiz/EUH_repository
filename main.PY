import pygame
import sys
from config.settings import *
from core.sprites.healer import *
from core.sprites.skeleton import *
from core.map import *


def main():
    pygame.init()

    ###LOADS IMAGES
    imagen_healer=pygame.image.load("assets/images/skye.gif")
    imagen_healer_x2=pygame.transform.scale(imagen_healer, (imagen_healer.get_width() * 2.5, imagen_healer.get_height() *2.5))
    
    mapa= Map("assets/images/mapa.png",scale=(win_x,win_y))
    

    fps= pygame.time.Clock()
    screen = pygame.display.set_mode((win_x,win_y))
    brujo1=Healer(imagen_healer_x2,200,30,5)

    num_skeletons=10
    skeletons=[]
    for i in range(num_skeletons):
        x= Skeleton("assets/images/señor hongo.gif", speed= 1, position=(random.randint(0, 800), random.randint(0, 600)))
        skeletons.append(x)




    pygame.draw.rect(screen,BLANCO,((win_x//2)-20,(win_y//2)-20,40,40))
    pygame.display.set_caption("GAME")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()






        mapa.dibujar(screen)
        brujo1.dibujar(screen)

        for npc in skeletons:
            npc.update()
            npc.dibujar(screen)


        keys = pygame.key.get_pressed()
        brujo1.movimiento(keys)


        fps.tick(60)
        pygame.display.flip() 
        

main()