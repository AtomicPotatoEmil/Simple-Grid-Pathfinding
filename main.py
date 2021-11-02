import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from Tile import Tile

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Follow Test")

clock = pygame.time.Clock()

player_x = 0
player_y = 0

enemy_x = 0
enemy_y = 0

check_number = 1

tiles = []
positions = []

timer_start = False
time_until_enemy_move = 0.3

for i in range(0, 10):
        tiles.append(Tile(screen, i * 50, 0))
        tiles.append(Tile(screen, i * 50, 50))
        tiles.append(Tile(screen, i * 50, 100))
        tiles.append(Tile(screen, i * 50, 150))
        tiles.append(Tile(screen, i * 50, 200))
        tiles.append(Tile(screen, i * 50, 250))
        tiles.append(Tile(screen, i * 50, 300))
        tiles.append(Tile(screen, i * 50, 350))
        tiles.append(Tile(screen, i * 50, 400))
        tiles.append(Tile(screen, i * 50, 450))

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    dt = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_x -= 200 * dt
    if keys[K_RIGHT]:
        player_x += 200 * dt
    if keys[K_DOWN]:
        player_y += 200 * dt
    if keys[K_UP]:
        player_y -= 200 * dt
    
    screen.fill((0, 0, 0))

    player = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(player_x, player_y, 25, 25))

    for tile in tiles:
        tile.draw()
        if tile.rect.colliderect(player):
            if tile.collided == False:
                positions.append(tile.x)
                positions.append(tile.y)
                tile.collided = True
                print(positions)

    if len(positions) > 0:
        timer_start = True
    else:
        timer_start = False
    if timer_start:
        time_until_enemy_move -= 1 * dt
    if time_until_enemy_move <= 0:
        enemy_x = positions.pop(0)
        enemy_y = positions.pop(0)
        time_until_enemy_move = 0.3
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(enemy_x, enemy_y, 50, 50))

    pygame.display.update()

pygame.quit()