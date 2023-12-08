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


class Creature(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('creature.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_DOWN:
                self.rect.y += 10
            if args[0].key == pygame.K_UP:
                self.rect.y -= 10
            if args[0].key == pygame.K_RIGHT:
                self.rect.x += 10
            if args[0].key == pygame.K_LEFT:
                self.rect.x -= 10


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    Creature(all_sprites)

    running = True
    pygame.mouse.set_visible(False)
    while running:
        screen.fill(pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            all_sprites.update(event)

        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

