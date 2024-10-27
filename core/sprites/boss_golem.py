class Boss_golem():
    def __init__(self,name,health,dmg,speed):
        self.name = name
        self.health = health
        self.dmg = dmg
        self.speed = speed

    
    def attack(self,objetivo):
        pass

golem = Boss_golem("golem",200,55,5)