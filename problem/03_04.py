pnums = []

for i in range(1,101):
    pnums.append(True)

# エラトステネスの篩は√100=10まで調べれば十分だったりします
for i in range(2,101):
    if pnums[i-1]:
        for j in range(i+i,101,i):
#           pnums[j-1]=False  下2行の代わりにこういう書き方ができます
            pnums.insert(j-1,False)
            pnums.pop(j)

for i in range(4,101,2):
    for j in range(2,i-1):
        if pnums[j-1] and pnums[i-j-1]:
                print(i,j,i-j)
                break
# 最初にリストを作っておくことで，素数判定にかかる時間が一定になっていて，早そうなアルゴリズムで良いと思います
