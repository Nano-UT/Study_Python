pnums = []

for i in range(1,101):
    pnums.append(True)

for i in range(2,101):
    if pnums[i-1]:
        for j in range(i+i,101,i):
            pnums.insert(j-1,False)
            pnums.pop(j)

for i in range(4,101,2):
    for j in range(2,i-1):
        if pnums[j-1] and pnums[i-j-1]:
                print(i,j,i-j)
                break
