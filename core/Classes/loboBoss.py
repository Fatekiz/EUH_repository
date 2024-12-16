import pygame
import random
from core.Classes.npc import NPC
import pygame
import random

class BossLobo(NPC):
    def __init__(self, img, speed, position=(0, 0), health=200, dmg=20):
        super().__init__(img, speed, position, health, dmg)
        self.target = None  # El objetivo que seguirá (personaje principal)

    def seguir_objetivo(self):
        """Ajusta la dirección del boss para seguir al objetivo."""
        if self.target:
            dx = self.target.rect.centerx - self.rect.centerx
            dy = self.target.rect.centery - self.rect.centery
            distancia = (dx**2 + dy**2)**0.5

            if distancia != 0:
                self.direction = (self.speed * dx / distancia, self.speed * dy / distancia)

    def update(self, paredes):
        """Actualiza la posición del boss, sigue al objetivo y maneja colisiones."""
        self.seguir_objetivo()

        # Mover al boss
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

        # Detectar colisión con paredes
        self.handle_wall_collision(paredes)

    def recibir_daño_boss(self, cantidad):
        """Reduce la salud del boss y verifica si muere."""
        self.health -= cantidad
        if self.health <= 0:
            self.health = 0
            self.kill()
