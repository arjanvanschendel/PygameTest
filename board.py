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
        pieceList = Board.getBlankBoard()
        pieceList[0][0] = Piece.pieceFromString('br', self.getFieldSize(), 0, 0)
        pieceList[0][1] = Piece.pieceFromString('bb', self.getFieldSize(), 0, 1)
        pieceList[0][2] = Piece.pieceFromString('bn', self.getFieldSize(), 0, 2)
        pieceList[0][3] = Piece.pieceFromString('bk', self.getFieldSize(), 0, 3)
        pieceList[0][4] = Piece.pieceFromString('bq', self.getFieldSize(), 0, 4)
        pieceList[0][5] = Piece.pieceFromString('bn', self.getFieldSize(), 0, 5)
        pieceList[0][6] = Piece.pieceFromString('bb', self.getFieldSize(), 0, 6)
        pieceList[0][7] = Piece.pieceFromString('br', self.getFieldSize(), 0, 7)
        pieceList[7][0] = Piece.pieceFromString('wr', self.getFieldSize(), 7, 0)
        pieceList[7][1] = Piece.pieceFromString('wb', self.getFieldSize(), 7, 1)
        pieceList[7][2] = Piece.pieceFromString('wn', self.getFieldSize(), 7, 2)
        pieceList[7][3] = Piece.pieceFromString('wk', self.getFieldSize(), 7, 3)
        pieceList[7][4] = Piece.pieceFromString('wq', self.getFieldSize(), 7, 4)
        pieceList[7][5] = Piece.pieceFromString('wn', self.getFieldSize(), 7, 5)
        pieceList[7][6] = Piece.pieceFromString('wb', self.getFieldSize(), 7, 6)
        pieceList[7][7] = Piece.pieceFromString('wr', self.getFieldSize(), 7, 7)
        for i in range(0,8):
            pieceList[1][i] = Piece.pieceFromString('bp', self.getFieldSize(), 1, i)
            pieceList[6][i] = Piece.pieceFromString('wp', self.getFieldSize(), 6, i)
        return pieceList

    def drawPieces(self, screen):
        for i in self.board:
            for j in i:
                if j is None:
                    continue
                screen.blit(j.image, j.rect)        

    def getFieldSize(self):
        return self.gridsize / 8

    def getBlankBoard():
        return [[None for i in range(8)] for j in range(8)]