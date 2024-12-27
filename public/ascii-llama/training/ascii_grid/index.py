import numpy as np

class AsciiGrid3D:
    def __init__(self, width, height, depth, default_char=' '):
        self.width = width
        self.height = height
        self.depth = depth
        self.grid = np.full((depth, height, width), default_char, dtype=str)

    def set_voxel(self, x, y, z, char):
        self.grid[z, y, x] = char

    def get_voxel(self, x, y, z):
        return self.grid[z, y, x]

    def print_grid(self):
        for z in range(self.depth):
            print(f"Depth {z}:")
            for y in range(self.height):
                row = ''.join(self.grid[z, y, :])
                print(row)
            print()

# Example usage
#grid = AsciiGrid3D(10, 10, 10)

# Set some voxels
#grid.set_voxel(5, 5, 5, '#')
#grid.set_voxel(3, 7, 2, 'X')
#grid.set_voxel(8, 3, 6, 'O')

# Print the grid
#grid.print_grid()