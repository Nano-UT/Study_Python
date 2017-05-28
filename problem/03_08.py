def is_perfect(n):
    pnums = []

    for i in range(1,n):
        pnums.append(True)

# √nまで調べれば十分です
    for i in range(2,n):
        if pnums[i-1]:
            for j in range(i+i,n,i):
#               pnums[j-1]=False  とかけます
                pnums.insert(j-1,False)
                pnums.pop(j)

    primes = []

    for i in range(2,n):
        if pnums[i-1]:
#           primes.append(i)でいいのでは？
            primes.insert(i-1,i)

    Num = n
    decom = []

    for p in primes:
        count = 0
        while Num % p == 0:
            count += 1
#           結果に整数型を期待する除算は // 演算子を使ってください
            Num = Num / p
        decom.append(count)

    pro = 1

#   primesの一番最後の要素が使われてないのが怪しい…
    for i in range(1,len(primes)):
#       約数の総和の公式と等比数列の和の公式ですね
#       結果に整数型を期待する除算は // 演算子を使ってください
        pro = pro * (((primes[i-1] ** (decom[i-1] + 1)) -1)/(primes[i-1]-1))
        pro = int(pro)

    if pro == 2 * n:
        return True
    else:
        return False
# 結果は良さそうです
