def Dict():
    student={"姓名":"小明",
             "年龄":"18",
             "专业":"人工智能",
             "成绩":{"数据结构":76,"高数":88,"数据挖掘":95}
             }
    print(student)
    student["姓名"]="小红"
    student["成绩"]["生产实习"]=88
    student["成绩"].pop("数据挖掘","未知")#或del["成绩"]["数据挖掘"]
    print(student)
    nums=[]
    for i,n in student.items():
        nums.append((i,n))
    print(f"字典中的键为{nums}")
    print(student)
    a = student.get("成绩", "ERROR").get("高数", "ERROR")
    b = student.get("成绩", "ERROR").get("数据结构", "ERROR")
    c = student.get("成绩", "ERROR").get("生产实习", "ERROR")
    d=(int(a)+int(b)+int(c))/3
    print(f"平均成绩为{d:.2f}")
    return c,student,nums

if __name__ == "__main__":
    Dict()