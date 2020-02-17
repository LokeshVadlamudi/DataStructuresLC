# LC - 1351. Count Negative Numbers in a Sorted Matrix

# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# count = 0
#
# for i in grid:
#     a = len([j for j in i if j < 0])
#     count += a
# print(count)

# LC - 1352. Product of the Last K Numbers
# class ProductOfNumbers:
#
#     def __init__(self):
#         self.array = [1]
#
#     def add(self, num: int) -> None:
#         if num == 0:
#             self.array = [1]
#         else:
#             self.array.append(self.array[-1] * num)
#
#     def getProduct(self, k: int) -> int:
#         if k >= len(self.array):
#             return 0
#         return self.array[-1] // self.array[-k - 1]
