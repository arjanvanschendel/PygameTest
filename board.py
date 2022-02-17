import logging
import math
from typing import List
import pygame

from piece import Piece, PieceColor, PieceType

logging.basicConfig(level=logging.DEBUG)

class Board:
    def __init__(self):
        self.white = (255,255,255)
        self.brown = (205,133,63)
        self.gridsize = 500
        self.board = self.initPieces()
        self.possibleMoves = []
        self.selectedPiece = None
        self.selectedSquare = None

    def drawBoard(self, screen):
        for i in range(0,8):
            for j in range(0,8):
                color = self.white if (i+j) % 2 == 1 else self.brown
                fieldSize = self.getFieldSize()
                pygame.draw.rect(screen, color, (fieldSize*i, fieldSize*j, fieldSize, fieldSize))
        self.drawPossibleMoves(screen)
        self.drawPieces(screen)

    def handleClick(self, pos):
        clickedCoordinates = self.getClickedSquareCoordinates(pos)
        clicked_x, clicked_y = clickedCoordinates
        clickedThing = self.board[clicked_y][clicked_x]
        logging.debug("Click registered at " + str(clicked_x) + "," + str(clicked_y) + ": object " + str(clickedThing))

        self.deselectAllPieces()

        if clickedThing is None:
            if clickedCoordinates in self.possibleMoves:
                self.movePieceCoordinates(self.selectedSquare, clickedCoordinates)
                logging.debug("Moving piece from " + str(self.selectedSquare) + " to " + str(clickedCoordinates))
            self.possibleMoves = []
            self.selectedPiece = None
            self.selectedSquare = None
        else:
            clickedThing.onClick()            
            if clickedThing.selected:
                self.selectedSquare = clickedCoordinates
                self.selectedPiece = clickedThing
                self.possibleMoves = self.findPossibleMoves(clickedThing, [clicked_x, clicked_y])
            else: 
                self.possibleMoves = []


    def initPieces(self) -> List[List[Piece]]:
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
                if j.selected:
                    pygame.draw.rect(screen, (25,25,25), j.rect)
                screen.blit(j.image, j.rect)

    def deselectAllPieces(self):
        for i in self.board:
            for j in i:
                if j is None:
                    continue
                j.selected = False 

    def movePieceFieldNames(self, fromSquare, toSquare):
        self.movePieceCoordinates(Board.nameToCoords(fromSquare), Board.nameToCoords(toSquare))

    def movePieceCoordinates(self, fromSquare, toSquare):
        piece = self.board[fromSquare[1]][fromSquare[0]]
        piece.setPos((toSquare[1] * self.getFieldSize(), toSquare[0] * self.getFieldSize()))
        self.board[toSquare[1]][toSquare[0]] = piece
        self.board[fromSquare[1]][fromSquare[0]] = None
        piece.hasMoved = True

    def nameToCoords(name):
        x, y = ""
        match name[0].lower():
            case "a": x = 0
            case "b": x = 1
            case "c": x = 2
            case "d": x = 3
            case "e": x = 4
            case "f": x = 5
            case "g": x = 6
            case "h": x = 7
            
        match name[1].lower():
            case "1": y = 0
            case "2": y = 1
            case "3": y = 2
            case "4": y = 3
            case "5": y = 4
            case "6": y = 5
            case "7": y = 6
            case "8": y = 7

        return(y, x)


    def drawPossibleMoves(self, screen):
        if self.possibleMoves is None: return
        for move in self.possibleMoves:
            pos = (move[0]*self.getFieldSize()+self.getFieldSize()*0.5, move[1]*self.getFieldSize()+self.getFieldSize()*0.5)
            pygame.draw.circle(screen, (125,125,125), pos, 10, 0)

    def findPossibleMoves(self, piece, fromPos):
        pieceMoves = Board.findPieceMoves(piece, fromPos)
        possiblePieceMoves = pieceMoves
        for move in pieceMoves:
            # Can't move outside the board
            if(move[0] > 7 or move[0] < 0 or move[1] > 7 or move[1] < 0):
                possiblePieceMoves.remove(move)

            # Can't move to squares with own piece
            elif(self.board[move[1]][move[0]]) is not None:
                if(self.board[move[1]][move[0]].color) is piece.color:
                    possiblePieceMoves.remove(move)
        return possiblePieceMoves

    def findPieceMoves(piece: Piece, fromPos: tuple[int, int]):
        possibleMoves = []
        moveDirectionMultiplier = 1 if piece.color == PieceColor.black else -1
        match piece.type:
            case PieceType.pawn:
                possibleMoves.append([fromPos[0], fromPos[1] + moveDirectionMultiplier])
                if not piece.hasMoved: possibleMoves.append([fromPos[0], fromPos[1] + 2 * moveDirectionMultiplier])
            case PieceType.rook:
                for i in range(0,8):
                    if i is not fromPos[1]:
                        possibleMoves.append([fromPos[0], i])
                    if i is not fromPos[0]:
                        possibleMoves.append([i, fromPos[1]])
            case PieceType.knight:
                distances = [-2, -1, 1, 2]
                for i in distances:
                    for j in distances:
                        if abs(i) is not abs(j):
                            possibleMoves.append([fromPos[0] + i, fromPos[1] + j])
            case PieceType.bishop:
                for i in range(0,8):
                    possibleMoves.append([fromPos[0] + i, fromPos[1] + i])
                    possibleMoves.append([fromPos[0] - i, fromPos[1] - i])
                    possibleMoves.append([fromPos[0] + i, fromPos[1] - i])
                    possibleMoves.append([fromPos[0] - i, fromPos[1] + i])
            case PieceType.king:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        possibleMoves.append([fromPos[0] + i, fromPos[1] + j])
            case PieceType.queen:
                for i in range(0,8):
                    if i is not fromPos[1]:
                        possibleMoves.append([fromPos[0], i])
                    if i is not fromPos[0]:
                        possibleMoves.append([i, fromPos[1]])
                for i in range(0,8):
                    possibleMoves.append([fromPos[0] + i, fromPos[1] + i])
                    possibleMoves.append([fromPos[0] - i, fromPos[1] - i])
                    possibleMoves.append([fromPos[0] + i, fromPos[1] - i])
                    possibleMoves.append([fromPos[0] - i, fromPos[1] + i])

        return possibleMoves

    def getFieldSize(self):
        return self.gridsize / 8

    def getBlankBoard():
        return [[None for i in range(8)] for j in range(8)]

    def getClickedSquareCoordinates(self, pos):
        x_index = math.floor(pos[0]/self.getFieldSize())
        y_index = math.floor(pos[1]/self.getFieldSize())
        return [x_index, y_index]