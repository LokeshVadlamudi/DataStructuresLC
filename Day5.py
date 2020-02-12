
# LC 56. Merge Intervals

# intervals = [[1,3],[2,6],[8,10],[15,18]]
#
#
# res = []
#
# for i in sorted(intervals,key=lambda i:i[0]):
#   if res and i[0] <= res[-1][1]:
#     res[-1][1] = max(i[1],res[-1][1])
#   else:
#     res.append(i)
# print(res)
#



# LC 953. Verifying an Alien Dictionary

# words = ["hello","leetcode"]
# order = "hlabcdefgijkmnopqrstuvwxyz"
#
# d = {c: i for i,c in enumerate(order)}
#
# words = [[d[c] for c in w]for w in words]
#
# flag = True
# for w1,w2 in zip(words,words):
#     print(w1,w2)
#     flag = (w1<=w2)
#     if flag == False:
#         print(flag)
# print(flag)
#
# print([0, 6, 1, 1, 14 ,1] <= [0, 6, 1, 1, 14])

