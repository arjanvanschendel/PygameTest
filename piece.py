from enum import Enum
import pygame

class PieceType(Enum):
    pawn = 1,
    bishop = 2,
    knight = 3,
    rook = 4,
    queen = 5,
    king = 6

class PieceColor(Enum):
    white = 1,
    black = 2

class Piece(pygame.sprite.Sprite):

    def __init__(self, type: PieceType, color: PieceColor, size, y, x):
        super(Piece, self).__init__()
        self.type = type
        self.color = color
        self.image = pygame.transform.scale(pygame.image.load(self.getImageForType()), (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x * size, y * size]

    def update(self):
        pass

    def setPos(self, pos):
        self.rect.topleft = pos

    def getImageForType(self):
        if self.color == PieceColor.white:
            if self.type == PieceType.pawn:
                return 'pieces/wp.png'
            if self.type == PieceType.bishop:
                return 'pieces/wb.png'
            if self.type == PieceType.knight:
                return 'pieces/wn.png'
            if self.type == PieceType.rook:
                return 'pieces/wr.png'
            if self.type == PieceType.queen:
                return 'pieces/wq.png'
            if self.type == PieceType.king:
                return 'pieces/wk.png'
        if self.type == PieceType.pawn:
            return 'pieces/bp.png'
        if self.type == PieceType.bishop:
            return 'pieces/bb.png'
        if self.type == PieceType.knight:
            return 'pieces/bn.png'
        if self.type == PieceType.rook:
            return 'pieces/br.png'
        if self.type == PieceType.queen:
            return 'pieces/bq.png'
        if self.type == PieceType.king:
            return 'pieces/bk.png'