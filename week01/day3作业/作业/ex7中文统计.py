def char_count(name:list=None):
    count={}
    for chinese in name:
        if chinese.strip():#str.strip()指去掉首尾空白，用在单一的字符上是判断是否为空白，意思是返回应该去掉首尾空白字符的新字符串
            #if not chinese.isspace(): 类似这个，str.isspace()表示是否是空白字符
            count[chinese]=count.get(chinese,0)+1
    print(count)
user_input=input("Enter your name:")
char_count(user_input)

if __name__=="__main__":
    char_count(user_input)


