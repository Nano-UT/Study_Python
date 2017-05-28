import math

def is_perfect(n):
    pnums = []

    for i in range(1,n):
        pnums.append(True)

    for i in range(2,int(math.sqrt(n))+1):
        if pnums[i-1]:
            for j in range(i+i,n,i):
                pnums[j-1]=False

    primes = []

    for i in range(2,n):
        if pnums[i-1]:
            primes.append(i)

    Num = n
    decom = []

    for p in primes:
        count = 0
        while Num % p == 0:
            count += 1
            Num = Num // p
        decom.append(count)

    pro = 1

    for i in range(0,len(primes)):
        pro = pro * (((primes[i] ** (decom[i] + 1)) -1)//(primes[i]-1))

    if pro == 2 * n:
        return True
    else:
        return False


def my_filter(ran, fun):
    for i in ran:
        if fun(i):
            print(i)
