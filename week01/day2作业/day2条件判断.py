def test(score):
    if score >= 90:
        return ("优秀")
    elif score >= 80 :
        return("良好")
    elif score >= 60:
        return("及格")
    else:
        return("不及格")
score2 = input("请输入成绩：")
score3 = int(score2)
c=test(score3)
print(c)
