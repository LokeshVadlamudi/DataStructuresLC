# print(1)
#contest

# 1365. How Many Numbers Are Smaller Than the Current Number
# nums = [8,1,2,2,3]
# res = []
#
# for i in nums:
#     count = 0
#     for j in nums:
#         if j < i:
#             count += 1
#     res.append(count)
# print(res)

# 1366. Rank Teams by Votes
# votes = ["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]
#
# d = {}
#
# for i in votes:
#     for j in i:
#         ind = i.find(j)
#         if j not in d.keys():
#             d[j] = ind
#         else:
#             d[j] += ind
#
# print(d)
# d = sorted(d, key=lambda k: (d[k], k))
#
# print(''.join(d))
# res = []























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

# 49. Group Anagrams
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
#
# d = {}
# for i in strs:
#     # print(sorted(i))
#     a = ''.join(sorted(i))
#     if a not in d:
#         d[a] = [i]
#     else:
#         d[a].append(i)
#
# res = []
# for i,val in d.items():
#     res.append(val)
# print(res)


# 560. Subarray Sum Equals K
# nums = [1,1,1,1]
# k = 2
#
# from collections import Counter
#
# c = Counter()
# c[0] = 1
# s = res = 0
# for i in nums:
#     s += i
#     print(c[s-k])
#     res += c[s-k]
#     c[s] += 1
# print(res)
# print(c)








# l = 0
# r = 1
# count = 0
# while r < len(nums)+1:
#     print(sum(nums[l:r]))
#     if sum(nums[l:r]) == k:
#         count += 1
#         l = l + 1
#         r = r + 1
#         continue
#     elif sum(nums[l:r]) > k:
#         l = r
#         r = r+1
#     else:
#         r = r+1
# print(count)

# 215. Kth Largest Element in an Array

# nums = [3,2,1,5,6,4]
# k = 2
#
# # print(sorted(nums)[len(nums)-k])
# import heapq
# a = heapq.nlargest(k,nums)[-1]
# print(a)


#contest
















