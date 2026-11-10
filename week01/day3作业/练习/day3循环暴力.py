def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):     # 注意 i+1，别自己跟自己比
            if nums[i] == nums[j]:
                print(True)
                return True
    print(False)
    return False
user_input=(input("")).split(",")
lst=[int(i) for i in user_input]
contains_duplicate(lst)
