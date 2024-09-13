import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the grid with random values (1 for alive, 0 for dead)
def random_grid(N):
    return np.random.choice([1, 0], N*N, p=[0.2, 0.8]).reshape(N, N)

# Count the number of neighbors for each cell
def count_neighbors(grid, N):
    neighbors = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            # Calculate the sum of all neighbors
            neighbors[i, j] = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                               grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                               grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                               grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
    return neighbors

# Update the grid according to Conway's rules
def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    neighbors = count_neighbors(grid, N)
    
    for i in range(N):
        for j in range(N):
            # Apply Conway's rules
            if grid[i, j] == 1:
                if neighbors[i, j] < 2 or neighbors[i, j] > 3:
                    newGrid[i, j] = 0  # Cell dies
            else:
                if neighbors[i, j] == 3:
                    newGrid[i, j] = 1  # Cell becomes alive

    img.set_data(neighbors)  # Set data to neighbors count instead of grid
    grid[:] = newGrid[:]  # Update the grid for the next step
    return img

# Main function to set up the animation
def run_game_of_life(N=100, update_interval=100):
    grid = random_grid(N)
    
    # Set up the plot
    fig, ax = plt.subplots()
    
    # Use a colormap to represent the number of neighbors
    img = ax.imshow(count_neighbors(grid, N), interpolation='nearest', cmap='viridis')
    
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                                  frames=10, interval=update_interval, save_count=50)
    
    plt.colorbar(img)  # Add color bar to show the number of neighbors
    plt.show()

# Run the Game of Life
if __name__ == "__main__":
    run_game_of_life(N=100, update_interval=100)
