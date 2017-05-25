import math

n = 101

for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
        print(n, "は素数ではありません")
        break
else:
    print(n, "は素数です")
# else は for の中で break しなかった場合に実行される
# for の中身が1度も実行されなくても実行されるので注意
