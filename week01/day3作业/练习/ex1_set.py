def set1(a:list=None,b:list=None):
    a1=set(a)
    b1=set(b)
    c=a1 & b1
    d=a1 | b1
    e=a1 - b1
    f=a1 ^ b1
    print(f"交集为{c}，共{len(c)}个元素")
    print(f"并集为{d}，共{len(d)}个元素")
    print(f"差集为{e}，共{len(e)}个元素")
    print(f"对称差为{f}，共{len(f)}个元素")
    return c,d,e,f
user_input_a = input("请输入a：").split(",")
user_input_b = input("请输入b：").split(",")
print(user_input_a)
print(user_input_b)
set1(user_input_a,user_input_b)