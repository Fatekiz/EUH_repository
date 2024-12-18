import pygame
import random
import sys
from config.settings import *
from core.Classes.guerrero import *
from core.Classes.hongo import *
from core.Classes.loboBoss import *
from core.map import *

pygame.init()


mapa= Map("assets/images/mapa1.png",scale=(win_x,win_y))
mapa2= Map("assets/images/mapa2.jpg", scale=(win_x,win_y))

    # Variables para el cooldown
cooldown = 100  # CD ATAQUE 
global ultimo_ataque
ultimo_ataque= 0  # Al principio no ha habido ataques

sprites = {
    "left": [
        pygame.transform.scale(pygame.image.load("assets/images/personajes/warrior/mov1izquierda.png"),(60,60)),
        pygame.transform.scale(pygame.image.load("assets/images/personajes/warrior/mov2izquierda.png"),(60,60)),],
    "right": [
        pygame.transform.scale(pygame.image.load("assets/images/personajes/warrior/mov1derecha.png"),(60,60)),
        pygame.transform.scale(pygame.image.load("assets/images/personajes/warrior/mov2derecha.png"),(60,60)),],
    "up": [],
    "down": [],
}

sword_images = {
    "left": pygame.transform.scale(pygame.image.load("assets/images/personajes/warrior/sword4.png"), (50, 50)),
    "right": pygame.transform.scale(pygame.image.load("assets/images/personajes/warrior/sword2.png"), (50, 50)),
    "up": pygame.transform.scale(pygame.image.load("assets/images/personajes/warrior/sword1.png"), (50, 50)),
    "down": pygame.transform.scale(pygame.image.load("assets/images/personajes/warrior/sword3.png"), (50, 50)),
}


bananirou= Warrior(sprites, sword_images, health=100, dmg=10, speed=5)

# Cargar las imágenes originales
sprite_1 = pygame.image.load("assets/images/personajes/warrior/mov1derecha.png")
sprite_2 = pygame.image.load("assets/images/personajes/warrior/mov2derecha.png")
sprite_3 = pygame.image.load("assets/images/personajes/warrior/mov3derecha.png")
sprite_4 = pygame.image.load("assets/images/personajes/warrior/mov4derecha.png")
sprite_5 = pygame.image.load("assets/images/personajes/warrior/mov1izquierda.png")
sprite_6 = pygame.image.load("assets/images/personajes/warrior/mov2izquierda.png")
sprite_7 = pygame.image.load("assets/images/personajes/warrior/mov3izquierda.png")
sprite_8 = pygame.image.load("assets/images/personajes/warrior/mov4izquierda.png")

# Calcular las nuevas dimensiones (duplicar tamaño)
nuevo_ancho = sprite_1.get_width() * 3
nuevo_alto = sprite_1.get_height() * 3

# Redimensionar los sprites



fps= pygame.time.Clock()
screen = pygame.display.set_mode((win_x,win_y))


lobo_images = [
    pygame.image.load(f"assets/images/personajes/Wolf/wolf_attack{i}.png") for i in range(1, 6)
]  # Sprites del lobo

hongo_image = pygame.image.load("assets/images/enemigos/hongo.png")
queilino_image= pygame.image.load("assets/images/enemigos/queilino.png")
hongos = pygame.sprite.Group()

# Cargar imágenes
fondo_menu = pygame.image.load("assets/images/menu.png")  # Imagen de fondo del menú
boton_play_img = pygame.image.load("assets/images/boton_play.png")  # Imagen del botón "Play"
boton_play_rect = boton_play_img.get_rect(center=(640, 500))  # Posición del botón


pygame.draw.rect(screen,BLANCO,((win_x//2)-20,(win_y//2)-20,40,40))
pygame.display.set_caption("EL ULTIMO HEROE.")

fondo_menu_final= pygame.image.load("assets/images/menu_final.png")
boton_play_img2 = pygame.image.load("assets/images/boton_reintentar.png")  # Imagen del botón "Play"
boton_play_rect2 = boton_play_img.get_rect(center=(540, 800))  # Posición del botón

fuente = pygame.font.SysFont("Arial", 25)
texto_play = fuente.render("Presiona Enter para Jugar", True, NEGRO)
fondo_controles= pygame.image.load("assets/images/controles.png")

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


def controles():
    while True:
        # Rellenar la pantalla con el fondo (puedes cambiarlo por una imagen)
        screen.blit(fondo_controles, (0, 0))

        # Detectar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Si presionan Enter, empieza el juego
                    return  # Sale de la función y comienza el juego

        # Dibujar el texto de "Presiona Enter"
        screen.blit(texto_play, (win_x // 2 - texto_play.get_width() // 2, win_y // 2 - texto_play.get_height() // 2))

        # Actualizar la pantalla
        pygame.display.update()



# orden = pygame.Rect(x,y,ancho,largo)

def mapa_1():
    global bananirou, hongos

    # Configuración inicial
    num_oleadas = 3  # Total de oleadas
    enemigos_por_oleada = 10
    oleada_actual = 1
    enemigos_eliminados = 0  # Contador de enemigos eliminados

    # Reinicia al jugador

    bananirou= Warrior(sprites, sword_images, health=100, dmg=10, speed=5)

    # Define las paredes del mapa
    paredes = [
        pygame.Rect(0, 105, 40, 50),
        pygame.Rect(40, -80, 230, 50),
        pygame.Rect(260, 105, 230, 50),
        pygame.Rect(480, -80, 300, 50),
        pygame.Rect(776, 105, 600, 50),
        pygame.Rect(-10, -30, 50, 140),
        pygame.Rect(260, -30, 50, 140),
        pygame.Rect(440, -30, 50, 140),
        pygame.Rect(776, -30, 50, 140),
        pygame.Rect(1150, 0, 50, 580),
        pygame.Rect(1150, 800, 50, 580),
        pygame.Rect(-70, 0, 50, 960),
        pygame.Rect(0, 960, 1280, 50),
    ]

    while oleada_actual <= num_oleadas:
        
        # Generar enemigos para la oleada actual
        hongos = pygame.sprite.Group()
        for i in range(enemigos_por_oleada):
            hongo = Hongo(hongo_image, speed=1, position=(random.randint(500, 900), random.randint(500, 900)))
            hongos.add(hongo)

        while len(hongos) > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Dibujar mapa, personaje y enemigos
            mapa.dibujar(screen)
            bananirou.dibujar(screen)
            bananirou.dibujar_barra_salud(screen)
            
            for hongo in hongos:
                hongo.update(paredes)
                hongo.dibujar(screen)

            # Detectar colisiones y ataques
            keys = pygame.key.get_pressed()
            global ultimo_ataque
            tiempo_actual = pygame.time.get_ticks()

            if keys[pygame.K_e]:
                if tiempo_actual - ultimo_ataque >= cooldown:
                    for npc in list(hongos):  # Convertimos a lista para evitar errores al eliminar
                        if bananirou.horizontal_sword.colliderect(npc.rect) or bananirou.vertical_sword.colliderect(npc.rect):
                            npc.recibir_daño_npc(bananirou.dmg)
                            if npc.health <= 0:
                                hongos.remove(npc)
                                enemigos_eliminados += 1  # Incrementa el contador
                            ultimo_ataque = tiempo_actual

            for npc in hongos:
                if bananirou.rect.colliderect(npc.rect):
                    bananirou.recibir_daño_personaje(npc.dmg)
                    if bananirou.health <= 0:
                        menu_final()

            # Movimiento del personaje
            bananirou.movimiento(keys, paredes)

            # Dibujar el contador de enemigos eliminados
            font = pygame.font.Font(None, 36)
            texto_contador = font.render(f"Eliminados: {enemigos_eliminados} - Oleada {oleada_actual}", True, (255, 255, 255))
            screen.blit(texto_contador, (10, 10))  # Posición en la esquina superior izquierda

            pygame.display.flip()
            fps.tick(60)

        # Fin de la oleada
        oleada_actual += 1
        bananirou.health = 100


    mapa_2()


def mapa_2():
    global bananirou, hongos

    # Configuración inicial
    num_oleadas = 2  # Total de oleadas
    enemigos_por_oleada = 10
    oleada_actual = 1
    enemigos_eliminados = 0  # Contador de enemigos eliminados

    bananirou = Warrior(sprites, sword_images, health=100, dmg=10, speed=5)
    
    # Define las paredes del mapa
    paredes = [
        pygame.Rect(0, 0, 1280, 1),  # Coordenadas para la pared superior
        pygame.Rect(0, 0, 1, 960),  # Coordenadas para la pared izquierda
        pygame.Rect(0, 959, 1280, 1),  # Coordenadas para la pared inferior
        pygame.Rect(1279, 0, 1, 960),  # Coordenadas para la pared derecha
    ]

    # Variable para el BossLobo
    boss_lobo = None

    while oleada_actual <= num_oleadas:
        
        # Generar enemigos para la oleada actual
        hongos = pygame.sprite.Group()
        for i in range(enemigos_por_oleada):
            hongo = Hongo(queilino_image, speed=1, position=(random.randint(0, 800), random.randint(0, 600)))
            hongos.add(hongo)

        while len(hongos) > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Dibujar mapa, personaje y enemigos
            mapa2.dibujar(screen)
            bananirou.dibujar(screen)
            bananirou.dibujar_barra_salud(screen)
            
            for pared in paredes:
                pygame.draw.rect(screen, (255, 0, 0), pared)
            for hongo in hongos:
                hongo.update(paredes)
                hongo.dibujar(screen)

            # Detectar colisiones y ataques
            keys = pygame.key.get_pressed()
            global ultimo_ataque
            tiempo_actual = pygame.time.get_ticks()

            if keys[pygame.K_e]:
                if tiempo_actual - ultimo_ataque >= cooldown:
                    for npc in list(hongos):  # Convertimos a lista para evitar errores al eliminar
                        if bananirou.horizontal_sword.colliderect(npc.rect) or bananirou.vertical_sword.colliderect(npc.rect):
                            npc.recibir_daño_npc(bananirou.dmg)
                            if npc.health <= 0:
                                hongos.remove(npc)
                                enemigos_eliminados += 1  # Incrementa el contador
                            ultimo_ataque = tiempo_actual

            for npc in hongos:
                if bananirou.rect.colliderect(npc.rect):
                    bananirou.recibir_daño_personaje(npc.dmg)
                    if bananirou.health <= 0:
                        menu_final()

            # Movimiento del personaje
            bananirou.movimiento(keys, paredes)

            # Dibujar el contador de enemigos eliminados
            font = pygame.font.Font(None, 36)
            texto_contador = font.render(f"Eliminados: {enemigos_eliminados}", True, (255, 255, 255))
            screen.blit(texto_contador, (10, 10))  # Posición en la esquina superior izquierda

            pygame.display.flip()
            fps.tick(60)

        # Al terminar la oleada, crear al BossLobo
        if oleada_actual == num_oleadas:
            img_boss_lobo = pygame.image.load("assets/images/personajes/Wolf/wolf_pos1.png")

            if img_boss_lobo is None:
                print("Error al cargar la imagen del BossLobo")
            boss_lobo = BossLobo(img=img_boss_lobo, speed=5, position=(500, 300), health=200, dmg=20)

            if boss_lobo:
                print("Actualizando BossLobo")
                boss_lobo.update(paredes)
                boss_lobo.dibujar(screen)


            boss_lobo.target = bananirou  # Asignar al personaje como objetivo
            enemigos_eliminados = 0  # Reiniciar el contador de enemigos eliminados

        # Si el BossLobo está en el juego, actualizarlo
        

            # Dibujar mapa, personaje y BossLobo
            mapa2.dibujar(screen)
            bananirou.dibujar(screen)
            bananirou.dibujar_barra_salud(screen)
            boss_lobo.update(paredes)
            boss_lobo.dibujar(screen)

            # Detectar colisiones y daño entre el BossLobo y el personaje
            if boss_lobo.rect.colliderect(bananirou.rect):
                print("Colisión con BossLobo")
                bananirou.recibir_daño_personaje(boss_lobo.dmg)
                if bananirou.health <= 0:
                    print("El jugador ha muerto")
                    menu_final()


            # Dibujar el contador de enemigos eliminados
            font = pygame.font.Font(None, 36)
            texto_contador = font.render(f"Eliminados: {enemigos_eliminados}", True, (255, 255, 255))
            screen.blit(texto_contador, (10, 10))  # Posición en la esquina superior izquierda

            pygame.display.flip()
            fps.tick(60)

        oleada_actual += 1
        bananirou.health = 100

        try:
            boss_lobo.update(paredes)
            boss_lobo.dibujar(screen)
        except Exception as e:
            print(f"Error al actualizar o dibujar el BossLobo: {e}")



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
                    mapa_1()  # Reinicia el juego

        # Dibujar el botón "Reintentar"
        screen.blit(boton_play_img2, boton_play_rect2)

        # Actualizar la pantalla
        pygame.display.update()


        
mostrar_menu()
controles()
mapa_1()
