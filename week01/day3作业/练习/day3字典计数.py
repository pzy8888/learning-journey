txt=["a","b","c","d","e","f","g","h","i","j","a"]
dict={}
for i, in txt:
    dict[i]=dict.get(i,0)+1
    #dict.get(i,0)判断字典中是否有这个值，没有就默认输出0，
    #dict[i]=把列表里面此时的值与它出现的次数对应起来，因为要记录到字典里面，所以默认为1就有了.get(i,0)+1
print(dict)