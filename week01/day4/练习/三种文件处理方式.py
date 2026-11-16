def small_file()->str:
    """
    处理小文件直接将他们读成一个字符串即可

    :param text:
    :return:
    """
    with open("test.txt","r",encoding="utf-8") as f:
        content=f.read()
        print(content)
def file():
    with open("test.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
        print(lines)

def big_file():
    with open("test.txt","r",encoding="utf-8") as f:
        for a in f:
            print(a.strip())
file()