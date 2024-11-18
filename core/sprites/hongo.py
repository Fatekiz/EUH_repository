import random
import pygame


class Hongo(pygame.sprite.Sprite):
    def __init__(self, image, speed, position=(0, 0), health=30, dmg=10):
        super().__init__()
        self.image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))  # Escalar imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.speed = speed
        self.health = health
        self.dmg = dmg
        self.max_health = health  # Salud máxima para calcular el tamaño de la barra

        # Tiempo para cambiar de dirección
        self.change_direction_time = random.randint(3000, 7000)
        self.last_change = pygame.time.get_ticks()

        # Dirección inicial aleatoria
        self.direction = self.random_direction()

    def random_direction(self):
        return random.choice([(self.speed, 0), (-self.speed, 0), (0, self.speed), (0, -self.speed)])

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change > self.change_direction_time:
            self.direction = self.random_direction()
            self.last_change = current_time

        # Mover el hongo
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def recibir_daño(self, cantidad):
        self.health -= cantidad
        if self.health <= 0:
            print("¡Hongo eliminado!")
            self.kill()

    def dibujar(self, screen):
        # Dibujar la imagen del hongo
        screen.blit(self.image, self.rect.topleft)

        # Dibujar barra de salud
        if self.health > 0:
            # Calcula la proporción de la barra en función de la salud actual
            barra_ancho = 50  # Ancho total de la barra
            barra_altura = 5   # Altura de la barra
            barra_x = self.rect.x + (self.rect.width // 2) - (barra_ancho // 2)  # Centrar sobre el hongo
            barra_y = self.rect.y - 10  # Por encima del hongo

            # Calcula la salud proporcional
            salud_proporcional = (self.health / self.max_health) * barra_ancho
            # Barra roja (fondo)
            pygame.draw.rect(screen, (255, 0, 0), (barra_x, barra_y, barra_ancho, barra_altura))
            # Barra verde (salud actual)
            pygame.draw.rect(screen, (0, 255, 0), (barra_x, barra_y, salud_proporcional, barra_altura))
