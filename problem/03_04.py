import math
pnums = []

for i in range(1,101):
    pnums.append(True)

for i in range(2,int(math.sqrt(100)+1)):
    if pnums[i-1]:
        for j in range(i+i,101,i):
            pnums[j-1]=False

for i in range(4,101,2):
    for j in range(2,i-1):
        if pnums[j-1] and pnums[i-j-1]:
                print(i,j,i-j)
                break
