def xun_huang(num:int):
    n=99
    while n<num:
        n+=1
        a=str(n)
        if a==a[::-1]:
            continue
        print(n)
xun_huang(121)