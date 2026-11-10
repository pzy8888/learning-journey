s = "hello world"
print(s)
s.upper()               # 返回新字符串，但 s 本身没变
print(s)                # hello   ← 还是小写
b=s.title()
print(b)
c= s.upper()           # 要改变必须重新赋值
print(c)
d=s.capitalize()
print(d)