import random
import sys
import time

import pygame
from pygame.locals import QUIT

from conway.cell import Cell

# number of cells x,y
dimensions = 750


# Grid is initialised as a nxn matrix of dead cells
grid = [[Cell(0, x, y) for x in range(dimensions)] for y in range(dimensions)]
# Placeholder so we don't make changes to the grid live
temp_grid = grid
empty_grid = [[False for x in range(dimensions)] for y in range(dimensions)]


# random generation (sorta sucks)
def random_matrix(dims):
    m = []
    for i in range(dims):
        m.append([])
        for j in range(dims):
            random_integer = random.uniform(0,1)
            m[i].append(round(random_integer))
    return m


# uses random matrix to manually assign each 0,1 to the grid :((((

def random_grid_generation():
    global temp_grid
    matrix = random_matrix(dimensions)
    for i in range(dimensions):
        for j in range(dimensions):
            temp_grid[i][j].alive = matrix[i][j]
    return temp_grid


# if every cell is dead -> program quits

def fizzled_out():
    grid_status = [[grid[y][x].alive for x in range(dimensions)] for y in range(dimensions)]
    if grid_status == empty_grid:
        return True
    return False


def state():
    changes = []
    for y in range(dimensions):
        for x in range(dimensions):
            should_be_alive = grid[y][x].rules(grid, dimensions)
            changes.append((y, x, should_be_alive))
    for y, x, alive in changes:
        grid[y][x].update(alive)


cur_time = time.time()
dtime = 0
counter = 0
grid = random_grid_generation()


def stats():
    global counter
    global cur_time
    global dtime
    delta_time = dtime - cur_time
    avg = counter / delta_time
    print(f"iterations: {counter}, time started: {cur_time}, program time: {dtime-cur_time}, iter/second: {avg}")


# Initialize pygame
pygame.init()

# Set up display dimensions
window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Game of Life')

# Calculate cell size based on window dimensions and grid dimensions
cell_size = min(window_width // dimensions, window_height // dimensions)

# Function to draw the grid
def draw_grid():
    for y in range(dimensions):
        for x in range(dimensions):
            color = (255, 255, 255) if grid[y][x].alive else (0, 0, 0)
            pygame.draw.rect(window, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))


# void main()

try:
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        state()
        stats()
        window.fill((0, 0, 0))
        draw_grid()
        pygame.display.flip()
        dtime = time.time()
        counter += 1
        # Adjust the speed of the simulation
        time.sleep(0.1)
        if fizzled_out():
            stats()
            pygame.quit()
except KeyboardInterrupt:
    stats()
    pygame.quit()
