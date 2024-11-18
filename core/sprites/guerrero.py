import pygame

class Warrior(pygame.sprite.Sprite):
    def __init__(self,img, health, dmg, speed):
        self.img=img
        self.rect=self.img.get_rect()
        self.rect.top,self.rect.left=100,100
        self.health=health
        self.dmg=dmg
        self.speed=speed
        # espada (será del guerrero pero esta de prueba para la healer)
        self.sword = pygame.Rect(0, 0, 25, 8)

    def dibujar(self, superficie):
        superficie.blit(self.img, self.rect)
        pygame.draw.rect(superficie, (255, 0, 0), self.sword)  # Rectángulo rojo visible

        if self.health > 0:
            pygame.draw.rect(superficie, (0, 255, 0), (self.rect.x, self.rect.y - 10, self.health, 5))

    def recibir_daño(self, cantidad):
        """ reduce health del warrior"""
        self.health -= cantidad
        if self.health <= 0:
            print("HAS MUERTO...")

    def movimiento(self, keys):
        # Movimiento del personaje
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            # Espada pegada al borde izquierdo del personaje
            self.sword.topleft = (self.rect.x - self.sword.width + 13, self.rect.y + self.rect.height // 2 - self.sword.height // 2)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            # Espada pegada al borde derecho del personaje
            self.sword.topleft = (self.rect.x + self.rect.width - 13, self.rect.y + self.rect.height // 2 - self.sword.height // 2)
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            # Espada pegada al borde superior del personaje
            self.sword.topleft = (self.rect.x + self.rect.width // 2 - self.sword.width // 2, self.rect.y - self.sword.height + 5)
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            # Espada pegada al borde inferior del personaje
            self.sword.topleft = (self.rect.x + self.rect.width // 2 - self.sword.width // 2, self.rect.y + self.rect.height - 5)