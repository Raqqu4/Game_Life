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
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = load_image('mountains.png')
        self.rect = self.image.get_rect()


    def update(self):
        pass


class Landing(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = load_image('pt.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = pygame.


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    running = True
    fps = 30
    clock = pygame.time.Clock()

    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos, all_sprites)

        for i in range(10):
            Ball(20, 100, 100)
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()
