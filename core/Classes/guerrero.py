import pygame
from core.Classes.personaje import Personaje

class Warrior(Personaje):
    def __init__(self, img, health, dmg, speed, position=(100, 100)):
        super().__init__(img, health, dmg, speed, position)
        self.horizontal_sword = pygame.Rect(0, 0, 35, 8)  # Espada del guerrero cuando se mueve a los lados
        self.vertical_sword = pygame.Rect(0, 0, 8, 35) # Espada del guerrero cuando se mueve hacia arriba o abajo
        self.sword_direction = "right"  # Dirección inicial de la espada

    def movimiento(self, keys, paredes ):
        """Movimiento del guerrero, posición de la espada y colisiones"""

        posicion_original = self.rect.copy()

        if keys[pygame.K_LEFT]:  # Izquierda
            self.rect.x -= self.speed
            self.horizontal_sword.topleft = (
                self.rect.x - self.horizontal_sword.width + 13,
                self.rect.y + self.rect.height // 2 - self.horizontal_sword.height // 2
            )
            self.sword_direction = "left"

        if keys[pygame.K_RIGHT]:  # Derecha
            self.rect.x += self.speed
            self.horizontal_sword.topleft = (
                self.rect.x + self.rect.width - 13,
                self.rect.y + self.rect.height // 2 - self.horizontal_sword.height // 2
            )
            self.sword_direction = "right"

        if keys[pygame.K_UP]:  # Arriba
            self.rect.y -= self.speed
            self.vertical_sword.topleft = (
                self.rect.x + self.rect.width // 2 - self.vertical_sword.width // 2,
                self.rect.y - self.vertical_sword.height + 5
            )
            self.sword_direction = "up"

        if keys[pygame.K_DOWN]:  # Abajo
            self.rect.y += self.speed
            self.vertical_sword.topleft = (
                self.rect.x + self.rect.width // 2 - self.vertical_sword.width // 2,
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
        if self.sword_direction in ["left", "right"]:
            pygame.draw.rect(superficie, (255, 255, 255,), self.horizontal_sword) # horizontal
        
        elif self.sword_direction in ["up", "down"]:
            pygame.draw.rect(superficie, (255, 255, 255,), self.vertical_sword) #vertical