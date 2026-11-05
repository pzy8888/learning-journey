s = "  Hello Python World  "     # 注意前后各有 2 个空格
long=len(s)
a=s.strip()
long2=len(a)
b=a.upper()
c=a.split(" ")
c2=len(c)
d="Python" in s
print(long)
print(long2)
print(b)
print(c,c2)
print(d)