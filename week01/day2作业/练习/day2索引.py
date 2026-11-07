def twoSum(nums,target):
        seen = {}
        a=[]
        for i, num in enumerate(nums):
            need = target - num
            print(f"第{i}轮: num={num}, need={need}, 当前字典={seen}")
            if need in seen:
                print(f"  找到！need={need} 在下标 {seen[need]}")
                print([need, num])
            seen[num] = i
            print(f"  登记后字典={seen}")
nums2=[1,56,64,72,68,92,150]
t=160
a=twoSum(nums2, t)