def dict0(answer:dict=None):
    print(answer.get("c",5))#get返回但不添加，setdefault添加
    print(answer)
    print(answer.setdefault("c",6))
    print(answer)
user_input=input("enter:")
di=user_input.split(",")
Dict={}
print(di)
for i ,num in enumerate(di):
    Dict[num]=i
dict0(Dict)