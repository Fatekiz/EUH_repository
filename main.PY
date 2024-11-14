import pygame
import sys
from config.settings import *
from core.sprites.healer import *
from core.sprites.hongo import *
from core.map import *


def main():
    pygame.init()

    ###LOADS IMAGES
    imagen_healer=pygame.image.load("assets/images/skye.gif")
    imagen_healer_x2=pygame.transform.scale(imagen_healer, (imagen_healer.get_width() * 2, imagen_healer.get_height() *2))
    
    mapa= Map("assets/images/mapa.png",scale=(win_x,win_y))
    

    fps= pygame.time.Clock()
    screen = pygame.display.set_mode((win_x,win_y))
    healer1=Healer(imagen_healer_x2,200,30,5) # personaje

    num_hongos=30
    hongos = pygame.sprite.Group() # <-- Grupo de npcs
    for i in range(num_hongos):
        hongo = Hongo("assets/images/señor hongo.gif", speed= 1, position=(random.randint(0, 800), random.randint(0, 600)))
        hongos.add(hongo)




    pygame.draw.rect(screen,BLANCO,((win_x//2)-20,(win_y//2)-20,40,40))
    pygame.display.set_caption("EL ULTIMO HEROE.")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        # Se dibujan el mapa y los personajes.
        mapa.dibujar(screen)
        healer1.dibujar(screen)

        for npc in hongos:
            npc.update() #Movimiento de los npc hongos
            npc.dibujar(screen)

        

        #Se llama al movimiento del healer
        keys = pygame.key.get_pressed()
        healer1.movimiento(keys)

        for npc in pygame.sprite.spritecollide(healer1, hongos, False):
            if keys[pygame.K_e]:
                npc.kill()

        fps.tick(60)
        pygame.display.flip()
        

main()