import  pygame
import random
from core.Classes.personaje import Personaje 

class NPC(Personaje):
    def __init__(self, img, speed, position=(0, 0), health=30, dmg=10):
        super().__init__(img, health, dmg, speed, position)
        self.change_direction_time = random.randint(3000, 7000)
        self.last_change = pygame.time.get_ticks()
        self.direction = self.random_direction()

    def random_direction(self):
        return random.choice([(self.speed, 0), (-self.speed, 0), (0, self.speed), (0, -self.speed)])
    
    def recibir_daño_npc(self, cantidad):
        """Reduce la salud del personaje."""
        self.health -= cantidad
        if self.health <= 0:
            self.health = 0
            self.kill()

    def handle_wall_collision(self, paredes):
        for pared in paredes:
            if self.rect.colliderect(pared):
                self.direction = self.random_direction()
                break
  # Salimos del loop para evitar múltiples cambios en un frame

    def update(self, paredes):
        """Actualiza la posición y maneja colisiones."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change > self.change_direction_time:
            self.direction = self.random_direction()
            self.last_change = current_time

        # Mover al NPC
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

        # Detectar colisión con paredes
        self.handle_wall_collision(paredes)
