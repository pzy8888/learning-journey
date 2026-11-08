def lie_biao(nums:list):
    nums.append(7)
    nums+="8" #可以通过+=快速添加元素，但只限于str类型
    nums.insert(0,0)
    print(nums)
    nums.remove("8")
    nums.remove(7)   #删除int元素7，而不删"7"
    print(nums)
    nums.pop(0)
    nums.sort(reverse=False)#排序，且顺序不颠倒
    print(nums)
    sum=0
    max = nums[0]
    min = nums[0]
    for n in nums:
        sum+=n
        if n>max:
            max=n
        if n<min:
            min=n
    print(f"最大值是{max}：最小值是{min}.列表总长度为：{len(nums)},列表数字总和为:{sum}")
    nums.sort(reverse=True)
    print(f"倒序为{nums}")
NUM=input("请输入列表元素，并用逗号隔开:")

print(NUM)
print(type(NUM))
Num=NUM.split(",")

print(Num)
print(type(Num))
num_new=[int (i)for i in Num]

lie_biao(num_new)

