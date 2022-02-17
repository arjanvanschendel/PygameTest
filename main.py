import pygame
import board
pygame.init()

fps = 60

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Chess 2.0")

currentBoard = board.Board()
clock = pygame.time.Clock()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            currentBoard.handleClick(pos)

    screen.fill((150, 150, 150))
    currentBoard.drawBoard(screen)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()