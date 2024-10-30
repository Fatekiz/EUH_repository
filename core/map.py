import pygame

class Map:
    def __init__(self, image_path, position=(0, 0), scale=None):
        # Cargar la imagen del mapa
        self.image = pygame.image.load(image_path)

        # Redimensionar la imagen si se especifica un tamaño (scale)
        if scale:
            self.image = pygame.transform.scale(self.image, scale)

        # Posición inicial del mapa en pantalla
        self.position = position

    def dibujar(self, superficie):
        # Dibujar la imagen en la posición dada
        superficie.blit(self.image, self.position)