import tkinter as tk
import numpy as np

# Constants for grid and window size
GRID_SIZE = 100  # Number of cells per row and column
CELL_SIZE = 5    # Size of each cell in pixels
UPDATE_INTERVAL = 100  # Milliseconds between updates

# Initialize grid with random alive/dead cells
def random_grid(grid_size):
    return np.random.choice([1, 0], grid_size * grid_size, p=[0.2, 0.8]).reshape(grid_size, grid_size)

# Update the grid based on Conway's rules
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # Calculate the sum of alive neighbors
            total = int((grid[i, (j-1)%GRID_SIZE] + grid[i, (j+1)%GRID_SIZE] +
                         grid[(i-1)%GRID_SIZE, j] + grid[(i+1)%GRID_SIZE, j] +
                         grid[(i-1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i-1)%GRID_SIZE, (j+1)%GRID_SIZE] +
                         grid[(i+1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i+1)%GRID_SIZE, (j+1)%GRID_SIZE]))
            
            # Apply the Game of Life rules
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0  # Cell dies
            else:
                if total == 3:
                    new_grid[i, j] = 1  # Cell becomes alive
    return new_grid

# Create the Tkinter application
class GameOfLifeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conway's Game of Life")
        
        # Set up the canvas for drawing the cells
        self.canvas = tk.Canvas(self.root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="white")
        self.canvas.pack()
        
        # Initialize the grid
        self.grid = random_grid(GRID_SIZE)
        
        # Start the animation loop
        self.update()

    # Update the canvas and the grid in each step
    def update(self):
        self.grid = update_grid(self.grid)
        self.draw_grid()
        self.root.after(UPDATE_INTERVAL, self.update)

    # Draw the grid on the canvas
    def draw_grid(self):
        self.canvas.delete(tk.ALL)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x0, y0 = j * CELL_SIZE, i * CELL_SIZE
                x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
                if self.grid[i, j] == 1:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="black", outline="")

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = GameOfLifeApp(root)
    root.mainloop()
