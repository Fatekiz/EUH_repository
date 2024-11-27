import  pygame
import random
from core.Classes.personaje import Personaje 

class NPC(Personaje):
    def __init__(self, img, health, dmg, speed, position=(0,0)):
        super().__init__(img, health, dmg, speed, position)
        self.change_direction_time = random.randint(3000,7000)
        self.last_change = pygame.time.get_ticks()
        self.direction = self.random_direction()

    def random_direction(self):
        return random.choice([(self.speed, 0), (-self.speed, 0), (0, self.speed), (0, -self.speed)]) # direccion aleatoria para los npc´s

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change > self.change_direction_time: # cambia la posicion de los npc´s de vez en cuando 
            self.direction = self.random_direction()
            self.last_change = current_time
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def morir(self):
        print(f"¡{self.__class__.__name__} eliminado!") # elimina o saca del grupo a los npcs (los mata)
        self.kill()