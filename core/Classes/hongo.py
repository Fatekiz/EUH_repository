import pygame
import random
from core.Classes.personaje import Personaje

class Hongo(Personaje):
    def __init__(self, img, speed, position=(0, 0), health=30, dmg=10):
        super().__init__(img, health, dmg, speed, position)
        self.change_direction_time = random.randint(3000, 7000)
        self.last_change = pygame.time.get_ticks()
        self.direction = self.random_direction()

    def random_direction(self):
        return random.choice([(self.speed, 0), (-self.speed, 0), (0, self.speed), (0, -self.speed)])

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change > self.change_direction_time:
            self.direction = self.random_direction()
            self.last_change = current_time
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def dibujar(self, superficie):
        """Dibuja al hongo y su barra de salud."""
        superficie.blit(self.image, self.rect)
        self.dibujar_barra_salud(superficie)

    def morir(self):
        print("¡Hongo eliminado!")
        self.kill()
