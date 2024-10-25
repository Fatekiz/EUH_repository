# Trabajado por benja

class Mago():
    def __init__(self,name,health,dmg,speed):
        self.name = name
        self.health = health
        self.dmg = dmg     # dmg de damage <-- daño
        self.speed = speed

    def attack(self,object):
        object.health -= self.dmg 
        print(f"El jugador {self.name} ha atacado a {object.name}, la vida del enemigo se redujo a {object.name}")

# Creando el objeto
benja = Mago("benja",75,25,8)