def second_max(lst):
    max=float("-inf")
    second_max=float("-inf")
    for num in lst:
        if num>max:
            second_max=max
            max=num
        elif num> second_max and num != max:
            second_max =num
    print(f"最大值为{max},第二大的值为{second_max}")
b=input("请输入元素：")
c=b.split(",")
d1= [ int(i) for i in c]
second_max(d1)