import random
import pygame

class Skeleton(pygame.sprite.Sprite):
    def __init__(self,image_path, speed, position=(0,0)):
        self.image = pygame.image.load(image_path)
        self.image_x2= pygame.transform.scale(self.image, (self.image.get_width() * 2.5, self.image.get_height() *2.5))
        self.rect = self.image.get_rect(topleft=position)  # Rectángulo para la posición y colisiones
        self.speed = speed

        # Tiempo para cambiar de dirección (en milisegundos)
        self.change_direction_time = 3000  # Cambia cada 2 segundos
        self.last_change = pygame.time.get_ticks()  # Marca el tiempo actual

        # Dirección inicial aleatoria
        self.direction = self.random_direction()

    def random_direction(self):
        # Selecciona una dirección aleatoria (izquierda, derecha, arriba, abajo)
        return random.choice([(self.speed, 0), (-self.speed, 0), (0, self.speed), (0, -self.speed)])

    def update(self):
        # Comprobar si es tiempo de cambiar de dirección
        current_time = pygame.time.get_ticks()
        if current_time - (self.last_change - random.randint(0,2000)) > self.change_direction_time:
            self.direction = self.random_direction()  # Cambiar a una nueva dirección
            self.last_change = current_time  # Reiniciar el tiempo de cambio

        # Mover el NPC en la dirección actual
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def dibujar(self, screen):
        # Dibujar la imagen del NPC en su posición actual
        screen.blit(self.image_x2, self.rect.topleft)