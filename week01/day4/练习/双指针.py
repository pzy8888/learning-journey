def two_zhi(nums:list):
    if not nums:
        return 0
    slow=0
    for fast in range(1,len(nums)):
        if nums[fast]!=nums[slow]:
            slow+=1
            nums[slow]=nums[fast]
    print(nums)
    print(slow+1)
    return slow+1
two_zhi([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15])