def str():
    result=""
    word=["我","是","人工智能","大四","学生"]
    for i in word:
        result += i
    print(result)
    return result
str()

def str2():
    word = ["我", "是", "人工智能", "大四", "学生"]
    result ="".join(word)
    print(result)
    return result
str2()