# Example file showing a circle moving on screen
import pygame
import time
from board import Board
from config import cell_width, cell_height, number_of_cells

# pygame setup
pygame.init()
screen = pygame.display.set_mode((cell_width * number_of_cells, cell_height * number_of_cells))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

board = Board(screen)

currentPositionX = 0
currentPositionY = 0

# Définir les constantes
DEBOUNCE_DELAY = 0.5  # Délai en secondes

# Initialiser les variables de debounce
last_key_time = {}

# Fonction de debounce
def debounce(key):
    current_time = time.time()
    if key in last_key_time:
        if current_time - last_key_time[key] < DEBOUNCE_DELAY:
            return False
    last_key_time[key] = current_time
    return True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            computedX = 0
            computedY = 0

            while x > cell_width:
                x -= cell_width
                computedX += 1

            while y > cell_height:
                y -= cell_height
                computedY += 1

            board.select_piece(computedX, computedY)

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    # Refresh the screen
    board.draw()
    pygame.display.flip()

pygame.quit()