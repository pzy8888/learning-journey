name ="潘志远"
z_y="人工智能"
n_j="大四"
a_h="雕刻，建模"
tem=input("请输入摄氏度：")
t=float(tem)
hua=t*1.8+32
print(f"姓名：{name}，现在是{z_y}专业的一名{n_j}学生，兴趣爱好是{a_h},现在的温度是{hua:.1f}℉")

s="Hello world and python"
b=s.upper()
long=len(s)
s2=s.replace(" ","")
long2=len(s2)
zi=input("请输入查找字段：")
p= zi in s
c=s.split(" ")
long3=len(c)
print(f"长度为：{long},去空格长度为：{long2},查找字段{zi}在字符串中的情况为{p},大写后的字符串为：{b},共有{long3}个单词,他们分别是{c}")

user_input=input("请输入姓名：")
if user_input.strip() == "":
    print("姓名不能为空")
else:
    print(f"欢迎{user_input.strip()}到来")
height=input("请输入体重：")
l=input("请输入身高")
bmi=float(height)/(float(l)*float(l))
print(f"bmi指数为：{bmi:.1f}")


num1=input("请输入数字1：")
num2=input("请输入数字2：")
a1=float(num1)
a2=float(num2)
a1,a2=a2,a1
print(f"交互后的num1的值为：num1={a1},num2={a2}")