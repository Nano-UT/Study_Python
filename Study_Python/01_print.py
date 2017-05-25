# hello.py
print("Hello, Python3!")
# => Hello, Python3!\n
#最後に改行が付く

print("hello", "python3")
# => hello python3\n
# 引数を複数与えると空白を間に入れて出力してくれる

print("hello, Python3!", end="")
print("hello, Python3!", end="")
print("hello, Python3!")
# => Hello, Python3!
# => end="" を引数に与えれば，最後に改行はつかない

x = "Hello"
y = 'Hello'
print(x == y)
# 文字列は " と ' のどちらで囲んでも良い
