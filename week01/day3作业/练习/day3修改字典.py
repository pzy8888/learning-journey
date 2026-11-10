def xiu_gai():
    answer={}
    answer["a"]=1  #添加字典
    answer["b"]=2
    print(answer)
    answer["a"]=3   #如果有对应的键就更新，没有就添加
    print(answer)
    print(answer["a"]) #查找对应键的值，没有会报错，但是用get不会报错
    answer.update({"c":4,"d":5})#批量添加
    print(answer)
    answer.setdefault("a",6)#键不存在就设置值，有的话不会修改
    print(answer)
xiu_gai()