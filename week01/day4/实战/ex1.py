def create_profile(name, age=18, *hobbies, **extra):
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print(f"爱好：{hobbies}")
    print(f"其他信息：{extra}")
    print("-" * 20)
if __name__ == "__main__":
    create_profile("小明")
    create_profile("小红", 21)
    create_profile("小刚", 22, "篮球", "吉他")
    create_profile("小李", 20, "跑步", city="荆州", major="AI")
#带*的表示可变参数，有可变参数的情况下允许调用函数时少填或多填参数，单*的意思是将对应的参数外的未定义参数打包为一个元组，双**表示把定义了但函数内部没有的参数打包为一个字典
