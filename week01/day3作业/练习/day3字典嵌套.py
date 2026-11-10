school = {
    "class1": {"teacher": "李老师", "count": 30},
    "class2": {"teacher": "王老师", "count": 28},
}

print(school.get("class1",0).get("teacher",{})) # 王老师
#基础查询：school["class"]["teacher]没有回直接报错

#进阶查询try: school["class"]["teacher]   except:None,但是频繁报错会出现大量异常捕获

#推荐查询：xx.get("xx",{}).get("xx",{})逐层提取