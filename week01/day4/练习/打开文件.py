def file():
    with open("test.txt","w",encoding="utf-8") as f:#用w写内容时会直接清空再写，要追加用a打开
        f.write("第二行\n")
file()

def file2():
    with open("test.txt","r",encoding="utf-8") as f:
        content=f.read()
        print(content)
        return content
file2()