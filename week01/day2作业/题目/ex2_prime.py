def isPrime(n):
    if n < 2:
        print(False)
        return False
    if n == 2 :
        print(True)
        return True
    for i in range(2,n):
        if n%i==0:
            print("判断为非素数")
            return False
        else:
            print("是素数")
            return True
            break

num=int(input("请输入数字: "))
isPrime(num)
