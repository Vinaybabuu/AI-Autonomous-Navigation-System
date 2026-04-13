import pygame
import os
from grid import create_grid
from astar import astar
from agent import Agent
from moviepy import ImageSequenceClip

os.environ['SDL_VIDEODRIVER'] = 'dummy'

ROWS, COLS = 20, 20
CELL_SIZE = 30

pygame.init()
screen = pygame.display.set_mode((COLS*CELL_SIZE, ROWS*CELL_SIZE))

grid = create_grid(ROWS, COLS)

start = (0, 0)
goal = (19, 19)

grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0

path = astar(grid, start, goal)
agent = Agent(start)

counter = 0

running = True
clock = pygame.time.Clock()

while running and path:
    screen.fill((255,255,255))

    for i in range(ROWS):
        for j in range(COLS):
            color = (200,200,200)
            if grid[i][j] == 1:
                color = (0,0,0)
            pygame.draw.rect(screen, color,
                             (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for p in path:
        pygame.draw.rect(screen, (0,255,0),
                         (p[1]*CELL_SIZE, p[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, (255,0,0),
                     (agent.position[1]*CELL_SIZE,
                      agent.position[0]*CELL_SIZE,
                      CELL_SIZE, CELL_SIZE))

    if path:
        agent.move(path)

    pygame.display.flip()
    pygame.image.save(screen, f"../outputs/frame_{counter:04d}.png")
    counter += 1
    clock.tick(5)

if counter > 0:
    clip = ImageSequenceClip([f"../outputs/frame_{i:04d}.png" for i in range(counter)], fps=5)
    clip.write_videofile("../outputs/simulation.mp4")

pygame.image.save(screen, "../outputs/simulation_final.png")
pygame.quit()