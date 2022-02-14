import pygame


class Piece(pygame.sprite.Sprite):

    def __init__(self, spriteLocation):
        super().__init__()
        self.image = pygame.image.load(spriteLocation).convert()
        self.image.set_colorkey((255,255,255))