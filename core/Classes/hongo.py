from core.Classes.npc import NPC
import pygame

class Hongo(NPC):
    def __init__(self, img, speed, position=(0, 0), health=30, dmg=10):
        super().__init__(img, health, dmg, speed, position)

    def update(self):
        """Actualiza la posición del hongo (puede agregar comportamientos únicos si es necesario)."""
        super().update()  # Llama al método `update` de la clase base