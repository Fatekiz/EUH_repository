import pygame
from npc1 import *


class Guerrero():
    def __init__(self, health, dmg, speed):
        self.health=health
        self.dmg=dmg
        self.speed=speed
    def attack(self, npc):
        npc.health-= self.dmg
        print(f"Se hizo el ataque y la vida del npc es: {npc.health}")




jose = Guerrero(200,30,10)

jose.attack(npc)