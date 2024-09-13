import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Define the dimensions of the grid
GRID_SIZE = 100
CELL_SIZE = 8
SCREEN_SIZE = GRID_SIZE * CELL_SIZE

# Set up display
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Conway's Game of Life")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Randomly initialize the grid (1 for alive, 0 for dead)
def random_grid(grid_size):
    return np.random.choice([1, 0], grid_size * grid_size, p=[0.2, 0.8]).reshape(grid_size, grid_size)

# Count the number of alive neighbors for a given cell
def count_neighbors(grid, x, y, grid_size):
    total = (grid[(x-1) % grid_size, (y-1) % grid_size] + grid[(x-1) % grid_size, y % grid_size] +
             grid[(x-1) % grid_size, (y+1) % grid_size] + grid[x % grid_size, (y-1) % grid_size] +
             grid[x % grid_size, (y+1) % grid_size] + grid[(x+1) % grid_size, (y-1) % grid_size] +
             grid[(x+1) % grid_size, y % grid_size] + grid[(x+1) % grid_size, (y+1) % grid_size])
    return total

# Update the grid based on Conway's rules
def update_grid(grid, grid_size):
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            neighbors = count_neighbors(grid, i, j, grid_size)
            if grid[i, j] == 1:  # Alive
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0  # Cell dies
            else:  # Dead
                if neighbors == 3:
                    new_grid[i, j] = 1  # Cell becomes alive
    return new_grid

# Draw the grid on the pygame window
def draw_grid(screen, grid, grid_size, cell_size):
    for i in range(grid_size):
        for j in range(grid_size):
            color = WHITE if grid[i, j] == 1 else BLACK
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

# Main loop
def run_game_of_life():
    grid = random_grid(GRID_SIZE)
    running = True
    clock = pygame.time.Clock()
    
    while running:
        screen.fill(BLACK)
        draw_grid(screen, grid, GRID_SIZE, CELL_SIZE)
        pygame.display.update()

        # Update grid
        grid = update_grid(grid, GRID_SIZE)

        # Event handling (for closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Frame rate control
        clock.tick(10)

    pygame.quit()

# Run the Game of Life
if __name__ == "__main__":
    run_game_of_life()
