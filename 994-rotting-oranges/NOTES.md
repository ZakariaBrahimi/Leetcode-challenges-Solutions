if not grid or not grid[0]: return 0
hasVisited   = set()
directions   = [(0,1), (0,-1), (1,0), (-1,0)]
fresh_orange = 0
queue = []
minutes  = 0
ROWS  = len(grid)
COLS  = len(grid[0])
for row in range(ROWS):
for col in range(COLS):
if grid[row][col] == 1:
fresh_orange += 1
for row in range(ROWS):
for col in range(COLS):
if grid[row][col] == 2 and (row, col) not in hasVisited:
queue.insert(0, (row, col))
hasVisited.add((row, col))
while fresh_orange!=0 and queue:
for _ in range(len(queue)):
current_row, current_col = queue.pop()
for row_direction, col_direction in directions:
new_row = current_row + row_direction
new_col = current_col + col_direction
if (0<=new_row<ROWS and 0<=new_col<COLS and
(new_row, new_col) not in hasVisited and
grid[new_row][new_col] != 0):
grid[new_row][new_col] = 2
fresh_orange -= 1
queue.insert(0, (new_row, new_col))
hasVisited.add((new_row, new_col))
minutes += 1
for row in range(ROWS):
for col in range(COLS):
if grid[row][col] == 1:
return -1
return minutes
```
* The above approach is mine, it is not correct because I didn't consider BFS as multy sources algorithm for more detials, check [video explanation](https://www.youtube.com/watch?v=y704fEOx0s0)