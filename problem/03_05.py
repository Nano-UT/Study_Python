def fib(x):
    fibs = [0,1]
    for i in range(2,x+1):
        add = fibs[i-2]+fibs[i-1]
        fibs.append(add)
    print(fibs[x])

fib(10)
# よいと思います
