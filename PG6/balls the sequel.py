import os
import sys
import random
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):  # если файл не существует, то выходим
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, *group):
        super().__init__(*group)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)



class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, *group):
        super().__init__(*group)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

vertical_borders = pygame.sprite.Group()

horizontal_borders = 0
    all_sprites = pygame.sprite.Group()
    for i in range(10):
        Ball(10, 100, 100, all_sprites)


    running = True
    fps = 30
    clock = pygame.time.Clock()

    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Border(5, 5, width - 5, 5)
        Border(5, height - 5, width - 5, height - 5)
        Border(5, 5, 5, height - 5)
        Border(width - 5, 5, width - 5, height - 5)

        for i in range(10):
            Ball(20, 100, 100)
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()
