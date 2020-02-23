#leetcode contest 177
# 1360. Number of Days Between Two Dates
# date1 = "2019-06-29"
# date2 = "2019-06-30"
#
# d1 = date1.split('-')
# d2 = date2.split('-')
#
# from datetime import date
#
# # date(int(d2[0]),int(d2[1]),int(d2[2]))-date(int(d1[0]),int(d1[1]),int(d1[2]))).days)
#
#
# date1 = date(int(d1[0]),int(d1[1]), int(d1[2]))
# date2 = date(int(d2[0]), int(d2[1]), int(d2[2]))
#
# print((date2-date1).days)



# 5171. Closest Divisors
num = 999
res = []

n1 = num + 1
n2 = num + 2


def goGood(n3):
    largestDivisor = 0
    min1 = float('inf')
    try:
        i = 1
        while i < n3:
            if n3 % i == 0 and abs(i-(n3//i)) < min1:
                largestDivisor = i
                min1 = abs(i-(n3//i))
            if abs(goGood(n3//2)[0] - goGood(n3//2)[1]) < abs(largestDivisor - (n3//largestDivisor)):
                n3 = n3//2
            else:
                i = n3//2
            i += 1


    except ZeroDivisionError:
        return None

    return [largestDivisor,n3//largestDivisor]

def done(l1,l2):
    if abs(l1[0]-l1[1]) > abs(l2[0]-l2[1]):
        return l2
    else:
        return l1

print(done(goGood(n1),goGood(n2)))
























# 3. Longest Substring Without Repeating Characters
# s = "abcabcbb"
#
# d = {}
# longest = [0,1]
# startIdx = 0
# for i,c in enumerate(s):
#     if c in d:
#         startIdx = max(startIdx,d[c]+1)
#     if longest[1] - longest[0] < i + 1 - startIdx:
#         longest = [startIdx,i+1]
#     d[c] = i
# print(longest)



# 394. Decode String

# s = "3[a]2[bc]"

# stack = []
#
#
# for i in range(len(s)):
#     if s[i]==']':
#         new = ''
#         while stack:
#             val = stack.pop()
#             if val == '[':
#                 break
#             new = val + new
#         num = ''
#         while stack and stack[-1].isdigit():
#             num = stack.pop() + num
#         stack.append(new*int(num))
#         print(stack)
#     else:
#         stack.append(s[i])
#         print(stack)
#
# print(stack)




# import re


# while '[' in s:
#     s = re.sub(r'(\d+)\[([a-z]*)\]',lambda m: int(m.group(1)) * m.group(2), s)
#
#
# print(s)





# c = 0
# i = 0
# a = ''
# res = []
# while i != len(s):
#     while s[i].isdigit():
#         c = c + int(s[i])
#         i += 1
#     while s[i].isalpha():
#         a = a + s[i]
#         i += 1
#     res.append(a*c)
#     c = 0
#     a = ''
#     i += 1
# print(''.join(res))





# 46. Permutations

# nums = [1,2,3]
# perms = []
#
#
# def helper(arr,curperm,perms):
#     if not len(arr) and len(curperm):
#         perms.append(curperm[:])
#     else:
#         for i in range(len(arr)):
#             newarr = arr[:i]+arr[i+1:]
#             newperm = curperm + [arr[i]]
#             helper(newarr,newperm,perms)
# helper(nums,[],perms)
#
# print(perms)















# def helper(i,arr,perms):
#     if i == len(arr) - 1:
#         perms.append(arr[:])
#         print(perms)
#     else:
#         for j in range(i,len(arr)):
#             print(i,j)
#             swap(arr,i,j)
#             print(arr)
#             helper(i+1,arr,perms)
#             print(i,j)
#             swap(arr,i,j)
#
# def swap(arr,i,j):
#     arr[i] , arr[j] = arr[j] , arr[i]
#
# helper(0,nums,perms)
#
# print(perms)




