list = [4, 3, 6, 7, 9]
list.sort()
for x in range(1, (len(list)), 2):
    temp = list[x-1]
    list[x-1] = list[x]
    list[x] = temp
print(list)
