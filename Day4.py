





#rotten oranges - LC 994


# grid = [[2,1,1],[1,1,0],[0,1,1]]
#
# row , col = len(grid) , len(grid[0])
#
# rotting = {(i,j) for i in range(row) for j in range(col) if grid[i][j] == 2}
#
# fresh = {(i,j) for i in range(row) for j in range(col) if grid[i][j] == 1}
#
# print(fresh)
#
# timer = 0
#
#
# while fresh:
#     if not rotting: print(-1)
#     rotting = {(i+dx,j+dy) for i,j in rotting for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)] if (dx+i,dy+j) in fresh}
#     fresh -= rotting
#     timer += 1
#
# print(timer)











