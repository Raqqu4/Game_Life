import pygame
import sys

FPS = 50
WIDTH, HEIGHT = 550, 550
tile_width = tile_height = 50
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)


def terminate():
    pygame.quit()
    sys.exit()
