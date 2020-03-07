# 79. Word Search

# board =[
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# word = "ABCB"
# def dfs(board,i,j,word):
#     if len(word) == 0:
#         return True
#     if i<0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
#         return(False)
#     tmp = board[i][j]
#     board[i][j] = '#'
#     res = dfs(board,i+1,j,word[1:]) or dfs(board,i-1,j,word[1:]) or dfs(board,i,j+1,word[1:]) or dfs(board,i,j-1,word[1:])
#     board[i][j] = tmp
#     return res
#
#
#
# for i in range(len(board)):
#     for j in range(len(board[0])):
#         if dfs(board,i,j,word):
#             print(True)
# print(False)



# 256. Paint House
# costs = [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]


#
# red,blue,green = 0,0,0
#
# for r,b,g in costs:
#     red,blue,green = min(blue,green)+r , min(green,red)+b,min(blue,red)+g
# return min(red,blue,green)




# for i in range(len(costs)):
#     cur = costs[i]
#     ind = cur.index(min(cur))
#     if ind == preInd:
#         ind = (cur[:ind]+cur[ind+1:]).index(min(cur[:ind]+cur[ind+1:]))
#         if ind > preInd:
#             ind += 1
#             res += cur[ind]
#         else:
#             res += cur[ind]
#             preInd = ind
#     else:
#         res += cur[ind]
#
# print(res)


# 136. Single Number
# nums = [4,1,2,1,2]
# nums = sorted(nums)
# res = 0
# for i in range(len(nums)):
#     print(res)
#     res ^= nums[i]
# print(res)








