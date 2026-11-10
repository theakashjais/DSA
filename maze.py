import random
import matplotlib.pyplot as plt

dfs = True

def scale(k): return 2 * k + 1
def get_elem(mem): return mem.pop() if dfs else mem.pop(0)

def create_maze(rows, cols, plot=False):
    visited = [[0] * cols for i in range(rows)]
    maze = [[0] * scale(cols) for i in range(scale(rows))]
    mem = []

    # show walls
    #for y in range(scale(rows)):
    #    for x in range(scale(cols)):
    #        if y % 2 == 1 and x % 2 == 1:
    #            maze[y][x] = 1

    start_y, start_x = (random.randrange(rows), random.randrange(cols))
    maze[scale(start_y)][scale(start_x)] = 1

    if plot:
        fig, ax = plt.subplots()
        ax.set_title(f'{rows}x{cols} maze, {"stack" if dfs else "queue"} size: {len(mem)}')
        ax.axis('off')
        plt.tight_layout()
        img = ax.imshow(maze, interpolation='nearest', cmap=plt.cm.nipy_spectral)
        plt.pause(0.0001)
        input('enter any key to start ...')

    mem.append((start_y, start_x, scale(start_y), scale(start_x)))

    while mem:
        y, x, y2, x2 = get_elem(mem)

        if visited[y][x]:
            if plot:
                ax.set_title(f'{rows}x{cols} maze, {"stack" if dfs else "queue"} size: {len(mem)}')
                img.set_data(maze)
                plt.pause(0.0001)
            continue

        maze[scale(y)][scale(x)] = maze[y2][x2] = 1
        visited[y][x] = 1

        if plot:
            ax.set_title(f'{rows}x{cols} maze, {"stack" if dfs else "queue"} size: {len(mem)}')
            img.set_data(maze)
            plt.pause(0.01)

        neighbors = [(y, max(0, x-1)), (y, min(cols-1, x+1)), (max(0, y-1), x), (min(rows-1, y+1), x)]
        random.shuffle(neighbors)
        for (yn, xn) in neighbors:
            if visited[yn][xn]:
                continue
            y2, x2 = (scale(max(y, yn)) - 1, scale(x)) if xn == x else (scale(y), scale(max(x, xn)) - 1)
            mem.append((yn, xn, y2, x2))

    if plot:
        plt.savefig(f'maze-{"dfs" if dfs else "bfs"}-gen.pdf', bbox_inches='tight', pad_inches=0.0)
        plt.show()

    return maze


def solve_maze(maze, rows, cols, start, goal, plot=False):
    h, w = rows, cols
    start_y, start_x = start
    goal_y, goal_x = goal
    maze[scale(start_y)][scale(start_x)] = .85
    maze[scale(goal_y)][scale(goal_x)] = .25
    visited = set()
    mem = []

    if plot:
        fig, ax = plt.subplots()
        ax.set_title(f'{rows}x{cols} maze, {"stack" if dfs else "queue"} size: {len(mem)}')
        ax.axis('off')
        plt.tight_layout()
        img = ax.imshow(maze, interpolation='nearest', cmap=plt.cm.nipy_spectral)
        plt.pause(0.0001)
        input('enter any key to start ...')

    mem.append((start_y, start_x, scale(start_y), scale(start_x)))

    while mem:
        y, x, y2, x2 = get_elem(mem)
        if (y, x) in visited:
            continue
        if x != start_x or y != start_y:
            maze[scale(y)][scale(x)] = maze[y2][x2] = .5
        visited.add((y, x))

        if plot:
            ax.set_title(f'{rows}x{cols} maze, {"stack" if dfs else "queue"} size: {len(mem)}')
            img.set_data(maze)
            plt.pause(0.01)

        neighbors = []
        if maze[scale(y)][scale(x) - 1] > 0: neighbors.append((y, max(0, x-1)))
        if maze[scale(y)][scale(x) + 1] > 0: neighbors.append((y, min(cols-1, x+1)))
        if maze[scale(y) - 1][scale(x)] > 0: neighbors.append((max(0, y-1), x))
        if maze[scale(y) + 1][scale(x)] > 0: neighbors.append((min(rows-1, y+1), x))
        random.shuffle(neighbors)
        for (yn, xn) in neighbors:
            if (yn, xn) in visited:
                continue
            if xn == goal_x and yn == goal_y:
                y2, x2 = (scale(max(y, yn)) - 1, scale(x)) if xn == x else (scale(y), scale(max(x, xn)) - 1)
                maze[y2][x2] = .5
                if plot:
                    ax.set_title(f'{rows}x{cols} maze, {"stack" if dfs else "queue"} size: {len(mem)}')
                    img.set_data(maze)
                    plt.pause(0.0001)
                    plt.savefig(f'maze-{"dfs" if dfs else "bfs"}-solve.pdf', bbox_inches='tight', pad_inches=0.0)
                    plt.show()
                return

            y2, x2 = (scale(max(y, yn)) - 1, scale(x)) if xn == x else (scale(y), scale(max(x, xn)) - 1)
            mem.append((yn, xn, y2, x2))


maze = create_maze(10, 20, True)
solve_maze(maze, 10, 20, (0, 0), (9, 6), True)
