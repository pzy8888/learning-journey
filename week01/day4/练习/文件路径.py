from pathlib import Path
def file():
    text = Path("data/test.txt")
    print(text.exists())  # 文件是否存在
    print(text.suffix)  # 文件后缀
    print(text.stem)  # 文件名
    print(text.parent)  # 文件的前置文件夹
def file2():
    Path("data").mkdir(exist_ok=True)
    for f in Path("data").glob("*.txt"):
        print(f.name)
file2()