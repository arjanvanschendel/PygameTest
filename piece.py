from enum import Enum
import string
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

    def pieceFromString(fromString, size, y, x):
        foundColor = Piece.colorFromChar(fromString[0])
        foundType = Piece.typeFromChar(fromString[1])
        return Piece(foundType, foundColor, size, y, x)

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

    def typeFromChar(c: string):
        match c.lower():
            case 'p': return PieceType.pawn
            case 'b': return PieceType.bishop
            case 'n': return PieceType.knight
            case 'r': return PieceType.rook
            case 'q': return PieceType.queen
            case 'k': return PieceType.king

    def colorFromChar(c: string):
        match c.lower():
            case 'b': return PieceColor.black
            case 'w': return PieceColor.white


    def getImageForType(self):
        if self.color == PieceColor.white:
            match self.type:
                case PieceType.pawn: return 'pieces/wp.png'
                case PieceType.bishop: return 'pieces/wb.png'
                case PieceType.knight: return 'pieces/wn.png'
                case PieceType.rook: return 'pieces/wr.png'
                case PieceType.queen: return 'pieces/wq.png'
                case PieceType.king: return 'pieces/wk.png'
        match self.type:
            case PieceType.pawn: return 'pieces/bp.png'
            case PieceType.bishop: return 'pieces/bb.png'
            case PieceType.knight: return 'pieces/bn.png'
            case PieceType.rook: return 'pieces/br.png'
            case PieceType.queen: return 'pieces/bq.png'
            case PieceType.king: return 'pieces/bk.png'