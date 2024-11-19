import pygame
import sys
from config.settings import *
from core.sprites.guerrero import *
from core.sprites.hongo import *
from core.map import *

pygame.init()

###LOADS IMAGES
sprite_warrior=pygame.image.load("assets/images/personajes/warrior.pos1.png")
sprite_warrior_x2=pygame.transform.scale(sprite_warrior, (sprite_warrior.get_width() * 2, sprite_warrior.get_height() *2.5))

mapa= Map("assets/images/mapa1.png",scale=(win_x,win_y))

    # Variables para el cooldown
cooldown = 1000  # CD ATAQUE 

ultimo_ataque= 0  # Al principio no ha habido ataques

fps= pygame.time.Clock()
screen = pygame.display.set_mode((win_x,win_y))
bananirou = Warrior(sprite_warrior_x2,health=100, dmg= 15, speed= 5) # personaje


hongo_image = pygame.image.load("assets/images/señor hongo.gif")
hongos = pygame.sprite.Group()
for i in range(20):
    hongo = Hongo(hongo_image, speed=1, position=(random.randint(0, 800), random.randint(0, 600)))
    hongos.add(hongo)

# Cargar imágenes
fondo_menu = pygame.image.load("assets/images/menu.png")  # Imagen de fondo del menú
boton_play_img = pygame.image.load("assets/images/boton_play.png")  # Imagen del botón "Play"
boton_play_rect = boton_play_img.get_rect(center=(640, 500))  # Posición del botón


pygame.draw.rect(screen,BLANCO,((win_x//2)-20,(win_y//2)-20,40,40))
pygame.display.set_caption("EL ULTIMO HEROE.")


def mostrar_menu():
    while True:
        screen.blit(fondo_menu, (0, 0))  # Dibujar la imagen de fondo del menú

        # Detectar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si el clic está dentro del área del botón
                if boton_play_rect.collidepoint(evento.pos):  # Si el clic está dentro del botón
                    return  # Salir de la función y empezar el juego

        # Dibujar el botón "Play" centrado
        screen.blit(boton_play_img, boton_play_rect)

        # Actualizar la screen
        pygame.display.update()


def main():
    
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
        tiempo_actual= pygame.time.get_ticks()
        # Detectar colisiones entre la espada y los hongos
        keys = pygame.key.get_pressed()



        global ultimo_ataque
        
        if keys[pygame.K_e]:
        # Verificar si ha pasado el cooldown
            if tiempo_actual - ultimo_ataque >= cooldown:
                # Realizar el ataque
                for npc in hongos:
                    if bananirou.sword.colliderect(npc.rect):
                        npc.recibir_daño(bananirou.dmg)
                        ultimo_ataque = tiempo_actual

        for npc in hongos:
            if bananirou.rect.colliderect(npc.rect):
                bananirou.recibir_daño(npc.dmg)


        # Movimiento del personaje
        bananirou.movimiento(keys)

        fps.tick(60)
        pygame.display.flip()
        
mostrar_menu()
main()