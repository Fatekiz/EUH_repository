import pygame

class Healer(pygame.sprite.Sprite):
    def __init__(self,img, health, dmg, speed):
        self.img=img
        self.rect=self.img.get_rect()
        self.rect.top,self.rect.left=100,100
        self.health=health
        self.dmg=dmg
        self.speed=speed
        # espada (será del guerrero pero esta de prueba para la healer)
        self.sword = pygame.Rect(0, 0, 40, 10)

    def dibujar(self, superficie):
        superficie.blit(self.img, self.rect)
        pygame.draw.rect(superficie, (255, 0, 0), self.sword)  # Rectángulo rojo visible

    def movimiento(self, keys):
        # EN EL MAIN DEBE IR EL keys = pygame.key.get_pressed() y llamar con Warrior.movimiento(keys)
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.sword.topleft = (self.rect.x - 40, self.rect.y + self.rect.height // 2)  # Espada a la izquierda
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.sword.topleft = (self.rect.x + self.rect.width, self.rect.y + self.rect.height // 2)  # Espada a la derecha
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.sword.topleft = (self.rect.x + self.rect.width // 2 - 20, self.rect.y - 40)  # Espada arriba
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.sword.topleft = (self.rect.x + self.rect.width // 2 - 20, self.rect.y + self.rect.height)  # Espada abajo