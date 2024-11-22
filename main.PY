import pygame
import sys
from config.settings import *
from core.Classes.guerrero import *
from core.Classes.hongo import *
from core.map import *

pygame.init()

###LOADS IMAGES
sprite_warrior=pygame.image.load("assets/images/personajes/warrior.pos1.png")

mapa= Map("assets/images/mapa1.png",scale=(win_x,win_y))

    # Variables para el cooldown
cooldown = 1000  # CD ATAQUE 

ultimo_ataque= 0  # Al principio no ha habido ataques

fps= pygame.time.Clock()
screen = pygame.display.set_mode((win_x,win_y))
bananirou = Warrior(sprite_warrior,health=100, dmg= 15, speed= 5) # personaje


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

fondo_menu_final= pygame.image.load("assets/images/menu_final.png")
boton_play_img2 = pygame.image.load("assets/images/boton_reintentar.png")  # Imagen del botón "Play"
boton_play_rect2 = boton_play_img.get_rect(center=(540, 800))  # Posición del botón








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





# orden = pygame.Rect(x,y,ancho,largo)

def main():
    global bananirou, hongos  # Si son variables globales

    # Reinicia al jugador
    bananirou = Warrior(sprite_warrior, health=100, dmg=15, speed=5)

    # Reinicia los hongos
    global hongos
    hongos = pygame.sprite.Group()
    for i in range(20):
        hongo = Hongo(hongo_image, speed=1, position=(random.randint(0, 800), random.randint(0, 600)))
        hongos.add(hongo)

    # Define las paredes del mapa
    paredes = [
        pygame.Rect(0, 105, 40, 50),  # Pared TOP 1
        pygame.Rect(40, -80, 230, 50),  # Pared TOP 1.1
        pygame.Rect(260, 105, 230, 50),  # Pared TOP 2
        pygame.Rect(480, -80, 300, 50),  # Pared TOP 2.1
        pygame.Rect(776, 105, 600, 50),  # Pared TOP 3
        pygame.Rect(-10, -30, 50, 140),  # Pared TOP_LEFT 1
        pygame.Rect(260, -30, 50, 140),  # Pared TOP_LEFT 2
        pygame.Rect(440, -30, 50, 140),  # Pared TOP_RIGHT 1
        pygame.Rect(776, -30, 50, 140),  # Pared TOP_RIGHT 2
        pygame.Rect(1150, 0, 50, 580),  # Pared RIGHT 1
        pygame.Rect(1150, 800, 50, 580),  # Pared RIGHT 2
        pygame.Rect(-70, 0, 50, 960),  # Pared LEFT 1
        pygame.Rect(0, 960,1280, 50),  # Pared DOWN 2
    ]

    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Dibujar mapa y personajes
        mapa.dibujar(screen)
        bananirou.dibujar(screen)
        bananirou.dibujar_barra_salud(screen)

        """" Dibujar paredes (DEPURACIÓN)"""
        #for pared in paredes:
            #pygame.draw.rect(screen, (255, 0, 0), pared)
        

        # Actualizar y dibujar hongos
        hongos.update()
        for hongo in hongos:
            hongo.dibujar(screen)

        # Detectar colisiones
        keys = pygame.key.get_pressed()
        global ultimo_ataque
        tiempo_actual = pygame.time.get_ticks()

        if keys[pygame.K_e]:
            if tiempo_actual - ultimo_ataque >= cooldown:
                for npc in hongos:
                    if bananirou.sword.colliderect(npc.rect):
                        npc.recibir_daño_npc(bananirou.dmg)
                        ultimo_ataque = tiempo_actual

        for npc in hongos:
            if bananirou.rect.colliderect(npc.rect):
                bananirou.recibir_daño_personaje(npc.dmg)
                if bananirou.health <= 0:
                    menu_final()

        # Movimiento del personaje
        bananirou.movimiento(keys, paredes)
        pygame.display.flip()
        fps.tick(60)



def menu_final():
    while True:

        boton_play_rect2 = boton_play_img2.get_rect(center=(640, 650))
        screen.blit(fondo_menu_final, (0, 0))  # Dibujar la imagen de fondo del menú

        # Detectar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si el clic está dentro del área del botón
                if boton_play_rect2.collidepoint(evento.pos):  # Si el clic está dentro del botón
                    main()  # Reinicia el juego

        # Dibujar el botón "Reintentar"
        screen.blit(boton_play_img2, boton_play_rect2)

        # Actualizar la pantalla
        pygame.display.update()


        
mostrar_menu()
main()
