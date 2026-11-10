def LST(name1:list,name2:list):
    S1=set(name1)
    S2=set(name2)
    J=S1 & S2
    B=S2 | S1
    C=S2 - S1
    D=S2 ^ S1
    print(f"交集为:{J},并集为：{B},差集为:{C},对称差为:{D}")
    J1 = list(J)
    B1 = list(B)
    C1 = list(C)
    D1 = list(D)
    print(f"转化为列表后:交集为:{J1},长度为{len(J1)},并集为：{B1},长度为{len(B1)},差集为:{C1},长度为{len(C1)},对称差为:{D1},长度为{len(D1)}")
    return J1,B1,C1,D1,J,B,C,D
user1=input("请输入列表1：").split(",")
user2=input("请输入列表1：").split(",")
if __name__=="__main__":
    LST(user1, user2)