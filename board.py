import pygame

from piece import Piece, PieceColor, PieceType

class Board:
    def __init__(self):
        self.white = (255,255,255)
        self.brown = (205,133,63)
        self.gridsize = 500
        self.board = self.initPieces()

    def drawBoard(self, screen):
        for i in range(0,8):
            for j in range(0,8):
                color = self.white if (i+j) % 2 == 1 else self.brown
                fieldSize = self.getFieldSize()
                pygame.draw.rect(screen, color, (fieldSize*i, fieldSize*j, fieldSize, fieldSize))
        self.drawPieces(screen)

    def initPieces(self):
        pieceList = [[None for i in range(8)] for j in range(8)]
        pieceList[0][0] = Piece(PieceType.rook, PieceColor.black, self.getFieldSize(), 0, 0)
        pieceList[0][1] = Piece(PieceType.knight, PieceColor.black, self.getFieldSize(), 0, 1)
        pieceList[0][2] = Piece(PieceType.bishop, PieceColor.black, self.getFieldSize(), 0, 2)
        pieceList[0][3] = Piece(PieceType.queen, PieceColor.black, self.getFieldSize(), 0, 3)
        pieceList[0][4] = Piece(PieceType.king, PieceColor.black, self.getFieldSize(), 0, 4)
        pieceList[0][5] = Piece(PieceType.bishop, PieceColor.black, self.getFieldSize(), 0, 5)
        pieceList[0][6] = Piece(PieceType.knight, PieceColor.black, self.getFieldSize(), 0, 6)
        pieceList[0][7] = Piece(PieceType.rook, PieceColor.black, self.getFieldSize(), 0, 7)
        pieceList[1][0] = Piece(PieceType.pawn, PieceColor.black, self.getFieldSize(), 1, 0)
        pieceList[1][1] = Piece(PieceType.pawn, PieceColor.black, self.getFieldSize(), 1, 1)
        pieceList[1][2] = Piece(PieceType.pawn, PieceColor.black, self.getFieldSize(), 1, 2)
        pieceList[1][3] = Piece(PieceType.pawn, PieceColor.black, self.getFieldSize(), 1, 3)
        pieceList[1][4] = Piece(PieceType.pawn, PieceColor.black, self.getFieldSize(), 1, 4)
        pieceList[1][5] = Piece(PieceType.pawn, PieceColor.black, self.getFieldSize(), 1, 5)
        pieceList[1][6] = Piece(PieceType.pawn, PieceColor.black, self.getFieldSize(), 1, 6)
        pieceList[1][7] = Piece(PieceType.pawn, PieceColor.black, self.getFieldSize(), 1, 7)
        return pieceList

    def drawPieces(self, screen):
        for i in self.board:
            for j in i:
                if j is None:
                    return
                screen.blit(j.image, j.rect)
                

    def getFieldSize(self):
        return self.gridsize / 8