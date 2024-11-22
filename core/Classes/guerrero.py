import pygame
from core.Classes.personaje import Personaje

class Warrior(Personaje):
    def __init__(self, img, health, dmg, speed, position=(100, 100)):
        super().__init__(img, health, dmg, speed, position)
        self.sword = pygame.Rect(0, 0, 80, 8)  # Espada del guerrero
        self.sword_direction = "right"  # Dirección inicial de la espada

    def movimiento(self, keys, paredes ):
        """Movimiento del guerrero, posición de la espada y colisiones"""

        posicion_original = self.rect.copy()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.sword.topleft = (
                self.rect.x - self.sword.width + 13,
                self.rect.y + self.rect.height // 2 - self.sword.height // 2
            )
            self.sword_direction = "left"

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.sword.topleft = (
                self.rect.x + self.rect.width - 13,
                self.rect.y + self.rect.height // 2 - self.sword.height // 2
            )
            self.sword_direction = "right"

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.sword.topleft = (
                self.rect.x + self.rect.width // 2 - self.sword.width // 2,
                self.rect.y - self.sword.height + 5
            )
            self.sword_direction = "up"

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.sword.topleft = (
                self.rect.x + self.rect.width // 2 - self.sword.width // 2,
                self.rect.y + self.rect.height - 5
            )
            self.sword_direction = "down"

        
        # detectar colisiones con paredes
        for pared in paredes:
            if self.rect.colliderect(pared):
                #volver a la posicion si detecta colisión
                self.rect = posicion_original

    def dibujar(self, superficie):
        """Dibuja al guerrero y su espada."""
        # Llama al método `dibujar` de la clase `Personaje`
        super().dibujar(superficie)
        # Dibuja la espada
        pygame.draw.rect(superficie, (255, 255, 255, 0.9), self.sword)
