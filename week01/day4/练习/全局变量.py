x=10
def e():
    x=20
    print(x)
e()
print(f"x在外部的值为{x}")
#函数外部和内部如果有相同名字的参数，他们的值是不互通的，改变某个值是不会影响到另一个值的
def f():
    global x
    x=25
f()
print(f"声明全局变量后修改x的值为{x}")
def r(nums):
    c=x+10
    return c
x=r(x)
print(f"尽量将外部参数传输到函数内部进行修改，而不是全局声明，防止出现bug{x}")