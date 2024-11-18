import pygame
import sys
from config.settings import *
from core.sprites.guerrero import *
from core.sprites.hongo import *
from core.map import *


def main():
    pygame.init()

    ###LOADS IMAGES
    sprite_warrior=pygame.image.load("assets/images/personajes/warrior.pos1.png")
    sprite_warrior_x2=pygame.transform.scale(sprite_warrior, (sprite_warrior.get_width() * 2, sprite_warrior.get_height() *2.5))
    
    mapa= Map("assets/images/mapa1.png",scale=(win_x,win_y))
    

    fps= pygame.time.Clock()
    screen = pygame.display.set_mode((win_x,win_y))
    bananirou = Warrior(sprite_warrior_x2,health=100, dmg= 15, speed= 5) # personaje

    
    hongo_image = pygame.image.load("assets/images/señor hongo.gif")
    hongos = pygame.sprite.Group()
    for i in range(20):
        hongo = Hongo(hongo_image, speed=1, position=(random.randint(0, 800), random.randint(0, 600)))
        hongos.add(hongo)



    pygame.draw.rect(screen,BLANCO,((win_x//2)-20,(win_y//2)-20,40,40))
    pygame.display.set_caption("EL ULTIMO HEROE.")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Dibujar mapa y personajes
        mapa.dibujar(screen)
        bananirou.dibujar(screen)
        for npc in hongos:
            npc.dibujar(screen)

        # Actualizar y dibujar hongos
        hongos.update()
        hongos.draw(screen)

        # Detectar colisiones entre la espada y los hongos
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:  
            for npc in hongos:
                if bananirou.sword.colliderect(npc.rect):
                    npc.recibir_daño(bananirou.dmg)

        for npc in hongos:
            if bananirou.rect.colliderect(npc.rect):
                bananirou.recibir_daño(npc.dmg)


        # Movimiento del personaje
        bananirou.movimiento(keys)

        fps.tick(60)
        pygame.display.flip()
        

main()