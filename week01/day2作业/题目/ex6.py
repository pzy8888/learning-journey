import random
def sui_ji():
    num = random.randint(1,100)
    n=0
    while n <= 7:
        n += 1
        user_input = int(input("请输入数字:"))
        if user_input > num:
            print("偏大，请重新猜：")
        if user_input < num:
            print("偏小，请重新猜：")
        if user_input == num:
            print(f"恭喜你，猜对了，共用了{n}次")
            break
    print("很遗憾，次数用完了")
sui_ji()