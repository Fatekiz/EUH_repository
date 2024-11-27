from core.Classes.npc import NPC

class Hongo(NPC):
    def __init__(self, img, speed, position=(0, 0)):
        super().__init__(img, speed, position)

    def update(self, paredes):
        super().update(paredes)  # Llama al método de la clase padre
