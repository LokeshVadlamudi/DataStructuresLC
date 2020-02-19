



# LC - 981. Time Based Key-Value Store
# class TimeMap:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.dic = {}
#
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key in self.dic:
#             self.dic[key].append((value, timestamp))
#         else:
#             self.dic[key] = [(value, timestamp)]
#
#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.dic.keys():
#             return ''
#
#         l = 0
#         r = len(self.dic[key]) - 1
#
#         while l <= r:
#             mid = r - (r - l) // 2
#             if self.dic[key][mid][1] == timestamp:
#                 return self.dic[key][mid][0]
#             elif self.dic[key][mid][1] > timestamp:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         if self.dic[key][mid][1] < timestamp:
#             return self.dic[key][mid][0]
#         return ''


# 42. Trapping Rain Water
# heights = [0,1,0,2,1,0,1,3,2,1,2,1]
#
# maxes = [0 for i in heights]
# print(maxes)
#
# leftMax = 0
# for i in range(len(heights)):
#     height = heights[i]
#     maxes[i] = leftMax
#     leftMax = max(leftMax,height)
#
# rightMax = 0
# for i in reversed(range(len(heights))):
#     height = heights[i]
#     minHeight = min(maxes[i],rightMax)
#     if height < minHeight:
#         maxes[i] = minHeight - height
#     else:
#         maxes[i] = 0
#     rightMax = max(rightMax,height)
# print(sum(maxes))

















