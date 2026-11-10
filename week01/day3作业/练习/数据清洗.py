import string
def clean_text(text):
    text2 = text.lower()#同一大小写，将大写转化为小写
    for ch in string.punctuation:  #strin.punctuation---字符串库
        text2 = text2.replace(ch, " ")#遍历字符串，将文本中的所有字符串替换为空格，后续用split去掉
    #不能再循环中修改前缀。如果改成text3=text2.replace就无法累加替换，每次循环都会重置，最后就只有一个符号替换了。

    return text2
def clear(text:str)->str:
    counts={}
    for word in text.split():
        counts[word]=counts.get(word,0)+1
    print(counts)
    return counts

def top_n(count:dict=None):
    pair=[]
    for i,num in count.items(): #dict.items类似列表的enumerate，能同时获取键/值或者索引/元素，for x in dict默认取键
        pair.append((num,i))
    pair.sort(reverse=True)#比较元组是"先比第一个，相同再比第二个"。所以把次数放前面，就能按频次排序。
    print(pair)

user_input=input("Enter a text: ")
a=clean_text(user_input)
b=clear(clean_text(user_input))
clean_text(user_input)
clear(a)
top_n(b)