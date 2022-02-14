import pygame

class Board:
    def __init__(self):
        self.board = self.initPieces()
        self.white = (255,255,255)
        self.brown = (205,133,63)
        self.gridsize = 500

    def drawBoard(self, surface):
        for i in range(0,8):
            for j in range(0,8):
                color = self.white if (i+j) % 2 == 1 else self.brown
                widthHeight = self.gridsize/8
                pygame.draw.rect(surface, color, (widthHeight*i, widthHeight*j, widthHeight, widthHeight))
        self.drawPieces()

    def initPieces(self):
        pieceList = [[]]
        return pieceList

    def drawPieces(self):
        return 1