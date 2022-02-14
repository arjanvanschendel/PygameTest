import pygame
import board
pygame.init()

screen = pygame.display.set_mode([500, 500])

currentBoard = board.Board()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((150, 150, 150))
    currentBoard.drawBoard(screen)
    pygame.display.flip()

pygame.quit()