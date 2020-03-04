# 415. Add Strings
# num1 = '123'
# num2 = '234'
#
# num1 = list(num1)
# num2 = list(num2)
#
# print(num1,num2)
# # print(or)
# res , carry = [],0
#
# while num1 or num2:
#     n1 = n2 = 0
#     if num1: n1 = ord(num1.pop()) - ord('0')
#     if num2: n2 = ord(num2.pop()) - ord('0')
#
#     carry , remain = divmod(n1+n2+carry,10)
#     res.append(remain)
# if carry:
#     res.append(carry)
#
# print(''.join(str(d) for d in res)[::-1])



# 22. Generate Parentheses

# n = 3
#
# res = []
# s = [('(',1,0)]
# while s:
#     x,l,r = s.pop()
#
#     if l-r < 0 or l>n or r>n:
#         continue
#     if l==n and r==n:
#         res.append(x)
#     s.append((x+'(',l+1,r))
#     s.append((x+')',l,r+1))
# print(res)

# 735. Asteroid Collision
# asteroids = [10,2, -5]
# ans = []
#
# for i in asteroids:
#     while ans and i < 0 < ans[-1]:
#         if ans[-1] < -i:
#             ans.pop()
#             continue
#         elif ans[-1] == i:
#             ans.pop()
#         break
#     else:
#         ans.append(i)
#
# print(ans)













