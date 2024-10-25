import pygame

class Healer:
    def __init__(self, health, dmg, speed, healing_power, cooldown_curar=5):
        self.healt = health #vida
        self.healt_max = health#vida maxima que tendra la personaje con esto puedo hacer que al aumentar la vida no se pase de la inicial
        self.dmg = dmg #daño
        self.speed = speed # velocidad
        self.healing_power = healing_power # poder curativo
        self.cooldown_curar = cooldown_curar # tiempo para poder curarse
        self.cooldown_actual = 0 # contador del colwdon
        self.rect = pygame.Rect(100, 100, 50, 50)  # Posición inicial y tamaño del coso

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, (0, 255, 0), self.rect)  # Dibuja un rectángulo verde

    def auto_curar(self):
        if self.cooldown_actual == 0:
            if self.healt < self.healt_max:
                self.healt += self.healing_power
                if self.healt > self.healt_max:
                    self.healt = self.healt_max
                self.cooldown_actual = self.cooldown_curar
                print(f"{self.__class__.__name__} se ha curado a sí misma por {self.healing_power} puntos de salud. Salud actual: {self.healt}")
            else:
                print("La Healer ya tiene la salud completa.")
        else:
            print("Habilidad de curación en recarga. No puede curarse ahora.")

    def atacar(self, enemigo):
        enemigo.recibir_daño(self.dmg)
        if self.cooldown_actual > 0:
            self.cooldown_actual -= 1  # Reduce el cooldown en cada ataque
            print(f"Cooldown reducido a {self.cooldown_actual}")
        else:
            print("Habilidad de curación lista para usarse.")

    def movimiento(self, keys):
        if keys[pygame.K_LEFT]: 
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: 
            self.rect.x += self.speed
        if keys[pygame.K_UP]:  
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: 
            self.rect.y += self.speed

