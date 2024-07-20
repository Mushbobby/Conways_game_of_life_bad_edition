class Cell:
    def __init__(self, alive, x, y):
        self.alive = alive
        self.x = x
        self.y = y

    def check_neighbours(self, grid, dims):
        # Check all 8 possible neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < dims and 0 <= ny < dims and grid[ny][nx].alive:
                count += 1
        return count

    def rules(self, grid, dims):
        # Example rule: A cell becomes alive if neighbours are between 1 and 2
        neighbours_count = self.check_neighbours(grid, dims)


        if self.alive and (2 <= neighbours_count <= 3):
            return True
        elif self.alive and neighbours_count < 3:
            return False
        elif self.alive and neighbours_count > 3:
            return False
        elif not self.alive and neighbours_count == 3:
            return True
        return False

    def update(self, should_be_alive):
        self.alive = should_be_alive
