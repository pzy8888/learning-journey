def trap(name:str,lst:list=[]):
    lst.append(name)
    print(lst)
    return lst
trap(1)
trap(2)#结果是1,2而不是1，因为空列表只在函数定义时创建一次，之后都会在上面修改，正常应该在函数内部创建

def right(name:str):
    lst=[]
    lst.append(name)
    print(lst)
    return lst
right(1)
right(2)