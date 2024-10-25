import pygame

class Warrior():
    def __init__(self,img,rect, health, dmg, speed):
        self.img=img
        self.rect=self.img.get_rect()
        rect.top,rect.left=100,100
        self.health=health
        self.dmg=dmg
        self.speed=speed

    def dibujar(self, superficie):
        superficie.blit(self.img,self.rect)

    def movimiento(self, keys):
        # EN EL MAIN DEBE IR EL keys = pygame.key.get_pressed() y llamar con Warrior.movimiento(keys)
        if keys[pygame.K_LEFT]: 
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: 
            self.rect.x += self.speed
        if keys[pygame.K_UP]:  
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: 
            self.rect.y += self.speed