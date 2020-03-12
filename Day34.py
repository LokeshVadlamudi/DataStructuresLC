# 1029. Two City Scheduling

# costs = [[10,20],[30,200],[400,50],[30,20]]
#
# costs = sorted(costs , key = lambda x : x[0]-x[1])
# print(sum(cost[0] for cost in costs[:len(costs)//2]) + sum(cost[1] for cost in costs[len(costs)//2:]))
#





# 1010. Pairs of Songs With Total Durations Divisible by 60

# time = [30,20,150,100,40]
# total = 0
#
# c = [0] * 60
# total = 0
# for t in time:
#     total += c[-t % 60]
#     c[t % 60] += 1
# return total



# 463. Island Perimeter

# grid = [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# area = 0
#
# for row in grid + list(map(list, zip(*grid))):
#     for i1, i2 in zip([0] + row, row + [0]):
#         area += int(i1 != i2)
# return area
