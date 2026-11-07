def lie_biao():
    nums=[1,5,8,6,9]
    nums.append(11)
    print(nums)
    nums.insert(0,4)
    print(nums)
    nums.remove(4)
    print(nums)
    nums.pop(2)
    print(nums)
    a=nums
    a.pop()
    print(a)
    print(nums)
    b = nums.copy()
    b.pop(0)
    print(b)
    print(nums)
lie_biao()