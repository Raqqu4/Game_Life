from pprint import pprint
from load import load_level, load_image
from const import *
from screen import start_screen
from camera import Camera


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        if tile_type == 'wall':
            wall_group.add(self)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self, dx, dy):
        self.rect.x += dx * tile_width
        self.rect.y += dy * tile_height
        if pygame.sprite.spritecollide(self, wall_group, False):
            self.rect.x -= dx * tile_width
            self.rect.y -= dy * tile_height


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


if __name__ == '__main__':
    pprint(load_level('map01.txt'))
    pygame.init()

    tile_images = {
        'wall': load_image('box.png'),
        'empty': load_image('grass.png')
    }
    player_image = load_image('mario.png')

    # группы спрайтов
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()

    running = True
    clock = pygame.time.Clock()

    start_screen()
    player, level_x, level_y = generate_level(load_level('map01.txt'))

    size = (level_x + 1) * tile_width, (level_y + 1) * tile_height
    screen = pygame.display.set_mode()
    camera = Camera()
    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_group.update(0, -1)
                if event.key == pygame.K_DOWN:
                    player_group.update(0, 1)
                if event.key == pygame.K_LEFT:
                    player_group.update(-1, 0)
                if event.key == pygame.K_RIGHT:
                    player_group.update(1, 0)

            camera.update(player)
            for sprite in all_sprites:
                camera.apply(sprite)

        all_sprites.draw(screen)
        player_group.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()
