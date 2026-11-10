def find(nums:list=None):
    answer=[]
    print(nums)
    for i in nums:
        if i in answer:
            print(True)
            return True
        answer.append(i)
    print(False)
LST=input("请输入int元素：").split(",")
user_input=[int(i) for i in LST]
find(user_input)