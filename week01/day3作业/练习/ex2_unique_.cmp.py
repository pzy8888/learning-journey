def cmp():
    a=[3,1,3,2,1,4,2]
    b=set(a)
    c=list(b)
    print(c)
    return c
cmp()

def cmp2():
    a=[3,1,3,2,1,4,2]
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
    print(c)
    return c
cmp2()
#set是将列表转换为集合进行去重的，去重后无序，循环去重是根据列表顺序依次进行的，所以去重顺序不变