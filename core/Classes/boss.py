import pygame

class NPC():
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.rect = pygame.Rect(self.x, self.y, 64, 64)  # Tamaño genérico

    def mover_hacia(self, objetivo_x, objetivo_y):
        if self.x < objetivo_x:
            self.x += self.velocidad
        elif self.x > objetivo_x:
            self.x -= self.velocidad
        if self.y < objetivo_y:
            self.y += self.velocidad
        elif self.y > objetivo_y:
            self.y -= self.velocidad
        self.rect.topleft = (self.x, self.y)

    def dibujar(self, pantalla, sprite):
        pantalla.blit(sprite, (self.x, self.y))
