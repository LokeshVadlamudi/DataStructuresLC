# # Minimum Number of Steps to Make Two Strings Anagram - 1347
# s = "aba"
# t = "bab"
#
# from collections import Counter
# c = Counter(s)
# d = Counter(t)
#
# if c == d:
#     print(True)
# count = 0
# for i in (c-d).values():
#     count = count + i
# print(count)


# 1346. Check If N and Its Double Exist
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         d = {}
#         for i,val in enumerate(arr):
#             if val in d.keys():
#                 d[val].append(i)
#             else:
#                 d[val] = [i]
#
#         for i,val in enumerate(arr):
#             if len(d[val]) >= 1 and len(d.keys()) == 1:
#                 return(True)
#             if val*2 in d.keys() and i not in d[val*2] and (val*2 != val != 0):
#                 return(True)
#         return(False)

#add binary - 67
# a = "11"
# b = "1"
# print(bin(int(a,2) + int(b,2))[2:])




#angle between hands of clock - 1344
# hour = 12
# minutes = 30
#
# h = hour * 30 + (1/2*minutes)
#
# m = minutes * 6
# if abs(h-m) <= 180:
#     print(abs(h-m))
# else:
#     print(360 -(abs(h-m)))
# #
# #
# #




# 1342. Number of Steps to Reduce a Number to Zero
#java script

# var
# numberOfSteps = function(num)
# {
#     count = 0;
# while (num > 0){
# if (num % 2 == 0){
# num = num / 2;
# count += 1;
# }
# else {
# num = num - 1;
# count += 1;
# }
#
# };
# return count
#
# };

# $python
# class Solution:
#     def numberOfSteps(self, num: int) -> int:
#         count = 0
#         while num > 0:
#             c = [1, 2][num % 2 == 0]
#             if c == 2:
#                 num = num // c
#                 count += 1
#             else:
#                 num = num - c
#                 count += 1
#
#         return (count)
#
# #         count = 0
# #         while num > 0:
# #             # c = [1,2][num/2==0]
# #             if num % 2 != 0:
# #                 num = num - 1
# #                 count += 1
# #                 print(count)
# #             else:
# #                 num = num // 2
# #                 count += 1
#
#
# #         return(count)





















