from collections import deque
import heapq
import gen  # Import the maze generator


class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze.horizontal_walls) - 1
        self.cols = len(maze.vertical_walls[0]) - 1
        self.start = None
        self.end = None
        self.bonus_points = []
        self.l_zone = None

        # Find all special points
        self._identify_special_points()

    def _identify_special_points(self):
        """Identify all special points in the maze"""
        print("\nIdentifying special points...")

        # Check all possible start positions including edges
        for r in range(self.rows + 1):
            for c in range(self.cols):
                if self.maze.horizontal_walls[r][c] == 2:
                    print(f"Found start at ({r},{c}) - horizontal")
                    self.start = (r, c)
                    break
            else:
                continue
            break

        if not self.start:
            for r in range(self.rows):
                for c in range(self.cols + 1):
                    if self.maze.vertical_walls[r][c] == 2:
                        print(f"Found start at ({r},{c}) - vertical")
                        self.start = (r, c)
                        break
                else:
                    continue
                break

        # Set end position directly from maze.end_pos
        if self.maze.end_pos:
            self.end = self.maze.end_pos
            print(f"Found end at {self.end}")

        # Find bonus points and L-zone
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.maze.bonus_points:
                    print(f"Found bonus point at ({r},{c})")
                    self.bonus_points.append((r, c))
                elif (r, c) == self.maze.l_zone:
                    print(f"Found L-zone at ({r},{c})")
                    self.l_zone = (r, c)
        print(f"Start: {self.start}, End: {self.end}")
        print(f"Bonus points: {self.bonus_points}")
        print(f"L-zone: {self.l_zone}\n")

    def _is_wall(self, r1, c1, r2, c2):
        """Check if there's a wall between two adjacent cells"""
        if r1 == r2:  # Horizontal movement
            return self.maze.vertical_walls[r1][max(c1, c2)] == 1
        else:  # Vertical movement
            return self.maze.horizontal_walls[max(r1, r2)][c1] == 1

    def _get_neighbors(self, pos):
        """Get valid neighboring cells"""
        r, c = pos
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if not self._is_wall(r, c, nr, nc):
                    neighbors.append((nr, nc))
        return neighbors

    def _a_star(self, start, end, collected_points=None):
        """A* pathfinding algorithm that returns all optimal paths"""
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        if collected_points is None:
            collected_points = set()

        open_set = []
        heapq.heappush(open_set, (0, start, collected_points.copy()))
        came_from = {}
        g_score = {start: 0}
        optimal_paths = []
        min_cost = float('inf')

        while open_set:
            current_cost, current, current_collected = heapq.heappop(open_set)

            if current == end:
                if current_cost < min_cost:
                    min_cost = current_cost
                    optimal_paths = []
                if current_cost == min_cost:
                    path = []
                    temp = current
                    while temp in came_from:
                        path.append(temp)
                        temp = came_from[temp]
                    optimal_paths.append(path[::-1])
                continue

            for neighbor in self._get_neighbors(current):
                # Skip if neighbor is a collected bonus point (unless it's the end)
                if (neighbor in self.bonus_points and
                    neighbor not in {start, end} and
                        neighbor in current_collected):
                    continue

                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score

                    # Update collected points if we're at a bonus point
                    new_collected = current_collected.copy()
                    if neighbor in self.bonus_points:
                        new_collected.add(neighbor)

                    f_score = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(
                        open_set, (f_score, neighbor, new_collected))

        return optimal_paths if optimal_paths else None

    def solve(self):
        """Calculate all optimal paths through the maze"""
        print("\nStarting pathfinding...")
        if not self.start or not self.end:
            print("Error: Start or end point not found!")
            return None

        # Get all bonus points except L-zone
        points_to_visit = [pt for pt in self.bonus_points if pt != self.l_zone]

        # Generate all possible orders of visiting bonus points
        from itertools import permutations
        best_paths = []
        best_length = float('inf')

        # Try all permutations of bonus points
        for order in permutations(points_to_visit):
            current_path = []
            current_pos = self.start
            valid = True

            # Visit all bonus points in this order
            for point in order:
                paths = self._a_star(current_pos, point, set())
                if not paths:
                    valid = False
                    break
                # Use the first path (all are same length)
                current_path.extend(paths[0])
                current_pos = point

            # Only proceed if we successfully visited all bonus points
            if valid:
                # Visit L-zone (must be after all bonus points)
                paths = self._a_star(current_pos, self.l_zone, set())
                if paths:
                    current_path.extend(paths[0])
                    current_pos = self.l_zone

                    # Then go to end
                    paths = self._a_star(current_pos, self.end, set())
                    if paths:
                        current_path.extend(paths[0])

                        # Check if this is the best path so far
                        if len(current_path) < best_length:
                            best_length = len(current_path)
                            best_paths = [current_path]
                        elif len(current_path) == best_length:
                            best_paths.append(current_path)

        return best_paths

    def print_path(self, path):
        """Print the maze with the path marked using ASCII characters"""
        print("\nMaze with solution path:")

        # Create a grid to mark path positions
        path_grid = [[False for _ in range(self.cols)]
                     for _ in range(self.rows)]
        for (r, c) in path:
            path_grid[r][c] = True

        for r in range(self.rows):
            # Print horizontal walls
            print("+", end="")
            for c in range(self.cols):
                print(" S " if self.maze.horizontal_walls[r][c] ==
                      2 else "---" if self.maze.horizontal_walls[r][c] == 1 else "   ", end="+")
            print()

            # Print vertical walls and grid content
            for c in range(self.cols):
                if self.maze.vertical_walls[r][c] == 1:
                    print("|", end="")
                elif self.maze.vertical_walls[r][c] == 2:
                    print("S", end="")
                else:
                    print(" ", end="")

                # Print cell content
                if (r, c) == self.end:
                    print(" T ", end="")
                elif (r, c) in self.bonus_points:
                    print(" G ", end="")
                elif (r, c) == self.l_zone:
                    print(" L ", end="")
                elif path_grid[r][c]:
                    print(" * ", end="")
                else:
                    print("   ", end="")

            # Print the rightmost vertical wall if it exists
            if self.maze.vertical_walls[r][self.cols] == 1:
                print("|")
            elif self.maze.vertical_walls[r][self.cols] == 2:
                print("S")
            else:
                print(" ")

        # Print the bottom row of horizontal walls
        print("+", end="")
        for c in range(self.cols):
            print(" S " if self.maze.horizontal_walls[self.rows][c] ==
                  2 else "---" if self.maze.horizontal_walls[self.rows][c] == 1 else "   ", end="+")
        print()


if __name__ == "__main__":
    # Generate a maze
    print("Generating maze...")
    maze = gen.generate_maze()

    # Solve it
    solver = MazeSolver(maze)
    paths = solver.solve()

    if paths:
        print(
            f"\nFound {len(paths)} optimal path(s) with length {len(paths[0])}:")
        for i, path in enumerate(paths, 1):
            print(f"\nPath {i}:")
            print(path)
            solver.print_path(path)
    else:
        print("\nNo valid path found")
