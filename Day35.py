# 162. Find Peak Element
# nums = [1,2,3,1]

# for i in range(len(nums) - 1):
#     if nums[i] > nums[i + 1]:
#         return i
# return len(nums) - 1

#
# l = 0
# r = len(nums) - 1
# while (l < r):
#     mid = (l + r) // 2
#     if nums[mid] > nums[mid + 1]:
#         r = mid
#     else:
#         l = mid + 1
# return l


# return nums.index(max(nums))













# 244. Shortest Word Distance II

# from collections import defaultdict
#
#
# class WordDistance:
#
#     def __init__(self, words: List[str]):
#         self.d = defaultdict(list)
#         for i, val in enumerate(words):
#             self.d[val].append(i)
#
#     def shortest(self, word1: str, word2: str) -> int:
#
#         loc1, loc2 = self.d[word1], self.d[word2]
#         l1, l2 = 0, 0
#         min_diff = float('inf')
#
#         while l1 < len(loc1) and l2 < len(loc2):
#             min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
#             if loc1[l1] < loc2[l2]:
#                 l1 += 1
#             else:
#                 l2 += 1
#
#         return min_diff
#






