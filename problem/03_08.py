def is_perfect(n):
    pnums = []

    for i in range(1,n):
        pnums.append(True)

    for i in range(2,n):
        if pnums[i-1]:
            for j in range(i+i,n,i):
                pnums.insert(j-1,False)
                pnums.pop(j)

    primes = []

    for i in range(2,n):
        if pnums[i-1]:
            primes.insert(i-1,i)

    Num = n
    decom = []

    for p in primes:
        count = 0
        while Num % p == 0:
            count += 1
            Num = Num / p
        decom.append(count)

    pro = 1

    for i in range(1,len(primes)):
        pro = pro * (((primes[i-1] ** (decom[i-1] + 1)) -1)/(primes[i-1]-1))
        pro = int(pro)

    if pro == 2 * n:
        return True
    else:
        return False
