import pygame
import game_platform
import player

pygame.init()

HEIGHT = 450
WIDTH = 400
ACCELERAION = 0.5
FRICTION = -0.12
FPS = 60

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("platformer")

ground = game_platform.Platform(WIDTH, HEIGHT)
player = player.Player(WIDTH, ACCELERAION, FRICTION)

all_sprites = pygame.sprite.Group()
all_sprites.add(ground)
all_sprites.add(player)

platforms = pygame.sprite.Group()
platforms.add(ground)

while True:
    # evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # logique de jeu
    player.move()
    player.update(platforms)

    # affichage
    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.update()
    clock.tick(FPS)
