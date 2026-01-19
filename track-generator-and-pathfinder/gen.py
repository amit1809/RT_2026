import random


class Maze:
    def __init__(self):
        self.rows = 4
        self.cols = 5
        self.horizontal_walls = [[0] * self.cols for _ in range(self.rows + 1)]
        self.vertical_walls = [[0] * (self.cols + 1) for _ in range(self.rows)]
        self.end_pos = None
        self.bonus_points = []
        self.l_zone = None


def generate_maze():
    maze = Maze()
    rows, cols = maze.rows, maze.cols
    walls_needed = 10

    def is_connected():
        """Check if the maze is fully connected using BFS."""
        visited = [[False] * cols for _ in range(rows)]
        queue = [(0, 0)]  # start from the top-left corner
        visited[0][0] = True

        while queue:
            r, c = queue.pop(0)
            # Check all four possible directions, ensuring no walls block the way
            # Up
            if r > 0 and not maze.horizontal_walls[r][c] and not visited[r - 1][c]:
                visited[r - 1][c] = True
                queue.append((r - 1, c))
            # Down
            if r < rows - 1 and not maze.horizontal_walls[r + 1][c] and not visited[r + 1][c]:
                visited[r + 1][c] = True
                queue.append((r + 1, c))
            # Left
            if c > 0 and not maze.vertical_walls[r][c] and not visited[r][c - 1]:
                visited[r][c - 1] = True
                queue.append((r, c - 1))
            # Right
            if c < cols - 1 and not maze.vertical_walls[r][c + 1] and not visited[r][c + 1]:
                visited[r][c + 1] = True
                queue.append((r, c + 1))

        # Check if all cells are visited
        return all(all(row) for row in visited)

    def random_wall_placement():
        """Randomly place 10 walls."""
        remaining_walls = walls_needed
        while remaining_walls > 0:
            # Randomly choose between placing a horizontal or vertical wall
            if random.choice([True, False]):
                # Place horizontal wall
                r = random.randint(0, rows)
                c = random.randint(0, cols - 1)
                if not maze.horizontal_walls[r][c]:
                    maze.horizontal_walls[r][c] = 1
                    remaining_walls -= 1
            else:
                # Place vertical wall
                r = random.randint(0, rows - 1)
                c = random.randint(0, cols)
                if not maze.vertical_walls[r][c]:
                    maze.vertical_walls[r][c] = 1
                    remaining_walls -= 1

    def place_start_point():
        """Place the start point on a random outer edge without a wall."""
        # Candidate positions for the start point
        candidates = []

        # Top edge
        for c in range(cols):
            if not maze.horizontal_walls[0][c]:
                candidates.append((0, c, "top"))

        # Bottom edge
        for c in range(cols):
            if not maze.horizontal_walls[rows][c]:
                candidates.append((rows, c, "bottom"))

        # Left edge
        for r in range(rows):
            if not maze.vertical_walls[r][0]:
                candidates.append((r, 0, "left"))

        # Right edge
        for r in range(rows):
            if not maze.vertical_walls[r][cols]:
                candidates.append((r, cols, "right"))

        # Randomly select a valid start position
        return random.choice(candidates)

    # Generate a valid maze
    while True:
        # Clear previous walls
        maze.horizontal_walls = [[0] * cols for _ in range(rows + 1)]
        maze.vertical_walls = [[0] * (cols + 1) for _ in range(rows)]
        random_wall_placement()
        if is_connected():
            break

    # Place the start point on a random valid edge without a wall
    startInfo = place_start_point()

    if startInfo[2] == "left" or startInfo[2] == "right":
        maze.vertical_walls[startInfo[0]][startInfo[1]] = 2
    if startInfo[2] == "top" or startInfo[2] == "bottom":
        maze.horizontal_walls[startInfo[0]][startInfo[1]] = 2

    # Place the end point inside the grid
    maze.end_pos = (random.randint(0, rows - 1), random.randint(0, cols - 1))

    # Place bonus points in the grid (up to 3)
    maze.bonus_points = []
    for _ in range(3):
        bp = (random.randint(0, rows - 1), random.randint(0, cols - 1))
        while bp == maze.end_pos or bp in maze.bonus_points:
            bp = (random.randint(0, rows - 1), random.randint(0, cols - 1))
        maze.bonus_points.append(bp)

    # Place the L zone
    maze.l_zone = (random.randint(0, rows - 1), random.randint(0, cols - 1))
    while maze.l_zone == maze.end_pos or maze.l_zone in maze.bonus_points:
        maze.l_zone = (random.randint(0, rows - 1),
                       random.randint(0, cols - 1))

    # Display the maze
    for r in range(rows):
        # Print horizontal walls
        print("+", end="")
        for c in range(cols):
            print(" S " if maze.horizontal_walls[r][c] ==
                  2 else "---" if maze.horizontal_walls[r][c] == 1 else "   ", end="+")
        print()

        # Print vertical walls and grid content
        for c in range(cols):
            if maze.vertical_walls[r][c] == 1:
                print("|", end="")
            elif maze.vertical_walls[r][c] == 2:
                print("S", end="")
            else:
                print(" ", end="")
            # Print end, bonus points, or L zone in the cell
            if (r, c) == maze.end_pos:
                print(" T ", end="")
            elif (r, c) in maze.bonus_points:
                print(" G ", end="")
            elif (r, c) == maze.l_zone:
                print(" L ", end="")
            else:
                print("   ", end="")

        # Print the rightmost vertical wall if it exists
        if maze.vertical_walls[r][cols] == 1:
            print("|")
        elif maze.vertical_walls[r][cols] == 2:
            print("S")
        else:
            print(" ")

    # Print the bottom row of horizontal walls
    print("+", end="")
    for c in range(cols):
        print(" S " if maze.horizontal_walls[rows][c] ==
              2 else "---" if maze.horizontal_walls[rows][c] == 1 else "   ", end="+")
    print()

    print("Target Time: " + str(random.randint(55, 85)) + " seconds")
    return maze


# Generate and display the maze
if __name__ == "__main__":
    maze = generate_maze()
