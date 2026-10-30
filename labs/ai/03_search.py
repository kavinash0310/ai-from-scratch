"""Lab 03: represent a maze as a graph and compare BFS with A*.

State: a grid coordinate. Action: move to an open neighbor. Goal test:
coordinate equals destination. Each move costs one step. BFS finds a shortest
path because all moves have equal cost. A* ranks a route by cost-so-far plus
Manhattan-distance estimate.
"""

from collections import deque
from heapq import heappop, heappush

maze = [
    "S...#",
    ".#..#",
    "...#.",
    "#....",
    "...#G",
]
start, goal = (0, 0), (4, 4)
height, width = len(maze), len(maze[0])
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def neighbors(cell):
    row, col = cell
    for dr, dc in moves:
        nxt = (row + dr, col + dc)
        r, c = nxt
        if 0 <= r < height and 0 <= c < width and maze[r][c] != "#":
            yield nxt


def reconstruct_path(parent, end):
    if end not in parent:
        return None
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return list(reversed(path))


def breadth_first_search():
    queue = deque([start])
    parent = {start: None}
    expanded = 0
    while queue:
        state = queue.popleft()
        expanded += 1
        if state == goal:
            return reconstruct_path(parent, goal), expanded
        for nxt in neighbors(state):
            if nxt not in parent:
                parent[nxt] = state
                queue.append(nxt)
    return None, expanded


def astar_search():
    def heuristic(cell):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    frontier = [(heuristic(start), 0, start)]
    parent = {start: None}
    best_cost = {start: 0}
    expanded = 0
    while frontier:
        _, cost, state = heappop(frontier)
        if cost != best_cost[state]:
            continue
        expanded += 1
        if state == goal:
            return reconstruct_path(parent, goal), expanded
        for nxt in neighbors(state):
            new_cost = cost + 1
            if new_cost < best_cost.get(nxt, float("inf")):
                best_cost[nxt] = new_cost
                parent[nxt] = state
                heappush(frontier, (new_cost + heuristic(nxt), new_cost, nxt))
    return None, expanded


for name, search in [("BFS", breadth_first_search), ("A*", astar_search)]:
    path, expanded = search()
    print(f"{name}: no route" if path is None else
          f"{name}: {len(path) - 1} moves; expanded {expanded} states")

# Change a wall and compare. Then make one action cost 5: why is BFS no longer
# guaranteed to find the least-cost route? What must A*'s heuristic satisfy?
