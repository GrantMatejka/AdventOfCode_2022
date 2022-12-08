def print_grid(grid):
    for row in grid:
        for num in row:
            print('%2d ' % num, end='')
        print()

def traverse_graph(grid, start_loc, end_loc):
    scores = [[1_000_000_000 for _ in r] for r in grid]
    scores[start_loc[0]][start_loc[1]] = 0
    visited = set()
    queue = [start_loc]
    
    directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ]

    while len(queue) > 0:
        curr_loc = queue.pop(0)
        visited.add(str(curr_loc))

        for d in directions:
            new_row = curr_loc[0] + d[0]
            new_col = curr_loc[1] + d[1]
            # I hate whitespace formatted conditionals
            # If we are in bounds
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                # If neighbor is at most 1 above
                if grid[curr_loc[0]][curr_loc[1]] + 1 >= grid[new_row][new_col]:
                    if [new_row, new_col] == end_loc:
                        scores[new_row][new_col] = scores[curr_loc[0]][curr_loc[1]] + 1
                    # If haven't visited this node yet
                    elif str([new_row, new_col]) not in visited:
                        queue.append([new_row, new_col])
                        old = scores[new_row][new_col]
                        new = scores[curr_loc[0]][curr_loc[1]] + 1
                        if new < old:
                            scores[new_row][new_col] = new

    return scores[end_loc[0]][end_loc[1]]


with open('input.txt') as f:
    grid = []
    start_loc = []
    end_loc = []
    for row_idx, row in enumerate(f.readlines()):
        grid.append([])
        for col_idx, ch in enumerate(row.strip()):
            num = None
            if ch == 'E':
                num = ord('z')
                end_loc = [row_idx, col_idx]
            elif ch == 'S':
                start_loc = [row_idx, col_idx]
                num = ord('a')
            else:
                num = ord(ch)
            num -= ord('a')
            grid[row_idx].append(num)
                
    print(traverse_graph(grid, start_loc, end_loc))