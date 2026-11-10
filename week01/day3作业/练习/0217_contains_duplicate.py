def contains_duplicate2(nums):
    seen = set()  #set通过哈希函数定向查找，时间复杂段远小于循环遍历
    for x in nums:
        if x in seen:        # set 查找 O(1)
            return True
        seen.add(x)
    return False
def xun_huan(name:list):
    answer=[]
    for i in name:
        if i  in answer:
            return True
        answer.append(i)
    return answer
q_c2(name)
nums=[1,2,3,4,5,6,6]
print(contains_duplicate(nums))
