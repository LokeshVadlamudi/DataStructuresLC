n = '123'
count = len(n)-1
for j in range(len(n) - 1):

    # print(count)
    if int(n[j]) + 1 == int(n[j + 1]):
        # print(int(n[j]))
        count -= 1

    # else:
    #     break
print(count)
