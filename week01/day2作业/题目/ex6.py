import random
def sui_ji():
    num = random.randint(1,100)
    n=0
    while n < 7:
        n += 1
        try:
            user_input = int(input(f"第 {n} 次，请输入 1-100："))
        except ValueError:  # 输入不是数字
            print("请输入数字！")
            continue
        if user_input > num:
            print("偏大，请重新猜：")
        elif user_input < num:
            print("偏小，请重新猜：")
        else:
            print(f"恭喜你，猜对了，共用了{n}次")
            break
        if n==6:
            print("很遗憾，次数用完了")
            break

sui_ji()