import pygame
import random
class Npc_jose():
    def __init__(self,img,rect, health, dmg, speed):
        self.img=img
        self.rect=self.img.get_rect()
        rect.top,rect.left= random.randint(500,1000), random.randint(500,1000)
        self.health=health
        self.dmg=dmg
        self.speed=speed

    def dibujar(self, superficie):
        superficie.blit(self.img,self.rect)

    def movimiento(self, keys):
        # EN EL MAIN DEBE IR EL keys = pygame.key.get_pressed() y llamar con Npc_jose.movimiento(keys)
        if keys[pygame.K_a]: 
            self.rect.x -= self.speed
        if keys[pygame.K_d]: 
            self.rect.x += self.speed
        if keys[pygame.K_w]:  
            self.rect.y -= self.speed
        if keys[pygame.K_s]: 
            self.rect.y += self.speed