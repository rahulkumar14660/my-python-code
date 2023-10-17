lst = [4,3,65,3,6,7,53,6,55,6,90]
max = lst[0]
for i in range(len(lst)):
    if max < lst[i]:
        max = lst[i]
print(max)