import pygame
from core.Classes.personaje import Personaje

class Warrior(Personaje):
    def __init__(self, sprites, sword_images, health, dmg, speed, position=(100, 100)):
        super().__init__(sprites["right"][0], health, dmg, speed, position)  # Usa el primer sprite como inicial
        self.sprites = sprites  # Diccionario de sprites para cada dirección
        self.sword_images = sword_images  # Diccionario de imágenes de la espada
        self.current_sprite = 0  # Índice del sprite actual
        self.horizontal_sword = pygame.Rect(0, 0, 50, 50)  # Espada horizontal
        self.vertical_sword = pygame.Rect(0, 0, 50, 50)  # Espada vertical
        self.sword_direction = "right"  # Dirección inicial de la espada

    def movimiento(self, keys, paredes):
        """Movimiento del guerrero, posición de la espada y colisiones."""
        posicion_original = self.rect.copy()

        # Movimiento hacia la izquierda
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.horizontal_sword.topleft = (
                self.rect.x - self.horizontal_sword.width + 13,
                self.rect.y + self.rect.height // 2 - self.horizontal_sword.height // 2
            )
            self.sword_direction = "left"
            self.image = self.sprites["left"][self.current_sprite // 10]

        # Movimiento hacia la derecha
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.horizontal_sword.topleft = (
                self.rect.x + self.rect.width - 13,
                self.rect.y + self.rect.height // 2 - self.horizontal_sword.height // 2
            )
            self.sword_direction = "right"
            self.image = self.sprites["right"][self.current_sprite // 10]

        # Movimiento hacia arriba
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.vertical_sword.topleft = (
                self.rect.x + self.rect.width // 2 - self.vertical_sword.width // 2,
                self.rect.y - self.vertical_sword.height + 5
            )
            self.sword_direction = "up"

        # Movimiento hacia abajo
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.vertical_sword.topleft = (
                self.rect.x + self.rect.width // 2 - self.vertical_sword.width // 2,
                self.rect.y + self.rect.height - 5
            )
            self.sword_direction = "down"

        # Animación del sprite solo para movimientos horizontales
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites["right"]) * 10:
                self.current_sprite = 0

        # Detectar colisiones con paredes
        for pared in paredes:
            if self.rect.colliderect(pared):
                self.rect = posicion_original

    def dibujar(self, superficie):
        """Dibuja al guerrero y su espada."""
        # Dibujar al guerrero
        superficie.blit(self.image, self.rect.topleft)

        # Dibujar la espada según la dirección
        if self.sword_direction in self.sword_images:
            if self.sword_direction in ["left", "right"]:
                superficie.blit(self.sword_images[self.sword_direction], self.horizontal_sword.topleft)
            elif self.sword_direction in ["up", "down"]:
                superficie.blit(self.sword_images[self.sword_direction], self.vertical_sword.topleft)