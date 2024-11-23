import pygame
import time
class Personaje(pygame.sprite.Sprite):
    def __init__(self, img, health, dmg, speed, position=(0, 0)):
        super().__init__()
        self.image = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))  # Cambiado a 'image'
        self.rect = self.image.get_rect(topleft=position)
        self.rect.width = int(self.rect.width * 0.8)  # Reduce ancho al 80%
        self.rect.height = int(self.rect.height * 0.8)  # Reduce altura al 80%
        self.health = health
        self.max_health = health
        self.dmg = dmg
        self.speed = speed
        self.last_damage_time = 0  # Guarda el tiempo del último daño recibido
        self.damage_cooldown = 1  # Cooldown en segundos entre daños

    def recibir_daño_personaje(self, cantidad):
        """Reduce la salud del personaje si ha pasado el cooldown."""
        tiempo_actual = time.time()
        if tiempo_actual - self.last_damage_time >= self.damage_cooldown:
            self.health -= cantidad
            self.last_damage_time = tiempo_actual  # Actualiza el último tiempo de daño
            if self.health <= 0:
                self.health = 0
                return "1"  # Devuelve "1" si el personaje muere
        return "0"
        

    def recibir_daño_npc(self, cantidad):
        """Reduce la salud del personaje."""
        self.health -= cantidad
        if self.health <= 0:
            self.health = 0
            self.morir()


    def dibujar(self, superficie):
        """Dibuja la imagen del personaje y la barra de salud."""
        superficie.blit(self.image, self.rect)
        self.dibujar_barra_salud(superficie)

    def dibujar_barra_salud(self, superficie):
        """Dibuja la barra de salud."""
        if self.health > 0:
            barra_ancho = 50
            barra_altura = 5
            barra_x = self.rect.x + (self.rect.width // 2) - (barra_ancho // 2)
            barra_y = self.rect.y - 10
            salud_proporcional = (self.health / self.max_health) * barra_ancho
            pygame.draw.rect(superficie, (255, 0, 0), (barra_x, barra_y, barra_ancho, barra_altura))  # Fondo rojo
            pygame.draw.rect(superficie, (0, 255, 0), (barra_x, barra_y, salud_proporcional, barra_altura))  # Salud verde