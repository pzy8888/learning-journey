def biao(n:int):
    for i in range(1,n+1):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i * j}", end="\t")
        print()
num=input("请输入数字：")
N=int(num)
biao(N)
