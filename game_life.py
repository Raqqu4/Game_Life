from random import random
import pygame
from copy import deepcopy


class Board:
    # создание поля
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                pygame.draw.rect(screen, "white",
                                 (self.left + self.cell_size * col, self.top + self.cell_size * row,
                                  self.cell_size, self.cell_size), 1)
                if self.board[row][col] == 1:
                    pygame.draw.rect(screen, "white",
                                     (self.left + self.cell_size * col, self.top + self.cell_size * row,
                                      self.cell_size, self.cell_size))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = mouse_pos[0] - self.left
        y = mouse_pos[1] - self.top
        if x < 0 or y < 0:
            return None
        col = x // self.cell_size
        row = y // self.cell_size
        if col >= self.width or row >= self.height:
            return None
        return col, row

    def on_click(self, cell_coords):
        if cell_coords:
            for row in range(self.height):
                self.board[row][cell_coords[0]] = (self.board[row][cell_coords[0]] + 1) % 2
            for col in range(self.width):
                self.board[cell_coords[1]][col] = (self.board[cell_coords[1]][col] + 1) % 2
            self.board[cell_coords[1]][cell_coords[0]] = (self.board[cell_coords[1]][cell_coords[0]] + 1) % 2


class Life(Board):
    def __init__(self, width=10, height=10):
        super().__init__(width, height)
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def next_move(self):
        board_next = [[0] * self.width for _ in range(self.height)]
        dx = ((-1, -1), (-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1), (0, -1))

        for row in range(self.height):
            for col in range(self.width):
                s = 0

                for d in dx:
                    if 0 <= row + d[0] < self.height\
                            and 0 <= col + d[1] < self.width\
                            and self.board[row + d[0]][col + d[1]] == 1:
                        s += 1

                if self.board[row][col] == 1 and 2 <= s <= 3\
                        or self.board[row][col] == 0 and s == 3:
                    board_next[row][col] = 1

        self.board = deepcopy(board_next)

    def on_click(self, cell_coords):
        if cell_coords:
            self.board[cell_coords[1]][cell_coords[0]] = (self.board[cell_coords[1]][cell_coords[0]] + 1) % 2


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Клетчатое поле')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    cell_size = 10
    game_life = Life(width // cell_size, height // cell_size)
    game_life.set_view(0, 0, cell_size)
    running = True
    gaming = True
    fps = 60
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.button)
                if event.button == 4:
                    if fps < 30:
                        fps += 1
                if event.button == 5:
                    if fps > 0:
                        fps -= 1

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                gaming = not gaming
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not gaming:
                game_life.get_click(event.pos)

        screen.fill((0, 0, 0))
        if gaming:
            game_life.next_move()
        game_life.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
