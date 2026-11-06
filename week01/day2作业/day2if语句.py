def pan_duan(name:str):
    if name.strip(): #如果名字去掉首尾空格后输出不为false,即值不为空/值/字符串/容器/数字0的时候
        #if xx 判断xx是否有效
        print(name)
    else:
        print("名字为空")
user_name = input("Enter your name: ")
pan_duan(user_name)