def lie_biao(nums):
    answer=[]
    for num in nums:
        if num in answer:
            print(f"找到重复元素：{num}")
            continue
        answer.append (num)
    if len(answer)==len(nums):
        print("没有重复元素")
    print(answer)
    return answer
lst=input("").split(",")
lst=[int (i) for i in lst]
lie_biao(lst)
