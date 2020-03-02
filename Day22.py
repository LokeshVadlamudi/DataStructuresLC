# 1087. Brace Expansion
# S = "{a,b}c{d,e}f"
#
# a = []
#
# if '{' not in S:
#     print([S])
#
# res  = []
# def helper(s,word):
#     if not s:
#         res.append(word)
#     else:
#         if s[0] == '{':
#             i = s.find('}')
#             for letter in s[1:i].split(','):
#                 helper(s[i+1:],word+letter)
#         else:
#             helper(s[1:],word+s[0])
# helper(S,'')
# res.sort()
# print(res)

# 202. Happy Number

# n = 19
#
# d = []
#
# while (n!=1):
#     if n in d:
#         print(False)
#     d.append(n)
#     n = sum([int(i)**2 for i in str(n)])
# print(True)













#decode string
# s = "3[a3[c]]2[bc]"
#
#
# def decode(s,op):
#     m = 0
#     # print(123)
#     for i in range(len(s)):
#         # print(s[i])
#         # print(143)
#         if s[i].isdigit():
#             m = int(s[i])
#             print(m)
#         elif (s[i]=='['):
#             j = i
#             while s[j]!=']':
#                 j+=1
#             a = s[i+1:j]
#             op = m*a
#         else:
#             return op
# op = []
# st = decode(s,op)
# print(st)





# 121. Best Time to Buy and Sell Stock
# p = [7,1,5,3,6,4]
#
# maxprofit = 0
# minPrice = float('inf')
# for i in p:
#     minPrice = min(minPrice,i)
#     profit = i - minPrice
#     maxprofit = max(maxprofit,profit)
#
# print(maxprofit)


# ans = 0
# for i in range(len(p)-1):
#     for j in range(i+1,len(p)):
#         if p[i] < p[j] and p[j] - p[i] > ans:
#             ans = p[j] - p[i]
# print(ans)

# 64. Minimum Path Sum
#
# grid = [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
#
# m, n = len(grid), len(grid[0])
#
# for i in range(m):
#     grid[i][0] = grid[i - 1][0] + grid[i][0] if i > 0 else grid[i][0]
#     for j in range(1, n):
#         grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j] if i > 0 else grid[i][j - 1] + grid[i][j]
# print(grid[-1][-1])






# def helper(x,y,grid,cost):
#     m, n = len(grid), len(grid[0])
#     if x == m or y == n:
#         return float('inf')
#     elif cost[x][y] != -1:
#         return cost[x][y]
#     else:
#         right , down = helper(x+1,y,grid,cost) , helper(x,y+1,grid,cost)
#         print(right,down)
#         cost[x][y] = min(right,down) + grid[x][y]
#     return cost[x][y]
#
#
# m , n = len(grid) , len(grid[0])
# # print(m,n)
# cost = [[-1]*n for _ in range(m)]
# # print(cost)
# cost[m-1][n-1] = grid[m-1][n-1]
# # print(cost[m-1][n-1])
# print(helper(0,0,grid,cost))
# print(cost)








