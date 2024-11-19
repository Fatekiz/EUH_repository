import pygame
from core.Classes.personaje import Personaje

class Wizzard(Personaje):
    def __init__(self, img, health, dmg, speed, position=(100, 100)):
        super().__init__(img, health, dmg, speed, position)

    def movimiento(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            
    def dibujar(self, superficie):
        """Dibuja al guerrero y su espada."""
        # Llama al método `dibujar` de la clase `Personaje`
        super().dibujar(superficie)
        