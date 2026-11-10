def sums(nums:list=None,target:int=None):
    answer={}
    seen=[]
    seen2=[]
    for i,n in enumerate(nums):
        a = targe - n
        if a in answer:
            print(f"第{i}次遍历,此时n的值为{n},a的值为{a}")
            b=answer[a]
            seen.append((b,i))
            seen2.append((a,n))
            print(f"此时的找到的对应的列表下标为{seen}")
            print(f"此时的找到的对应的值为{seen2}")
        answer[n]=i
    return seen
user_input=(input("请输入数组元素：").split(","))
targe=int(input("请输入目标值:"))
user_input2=[int(i) for i in user_input]
print(user_input2)
if __name__ == "__main__":
    sums(user_input2)

