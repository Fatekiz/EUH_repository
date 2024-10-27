from boss_golem import golem

class Wizzard():
    def __init__(self,name,health,dmg,speed):
        self.name = name
        self.health = health
        self.dmg = dmg
        self.speed = speed

        # Métodos
    def attack(self,objetivo):
        objetivo.health -= self.dmg
        print(f"El enemigo '{objetivo.name}' ha sido atacado por tí, su vida ha disminuído ha {objetivo.health}. ")

# Creación
mago = Wizzard("Benja",75,40,8)

# método
mago.attack(golem)