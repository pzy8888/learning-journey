import csv
with open("scores.csv","r",newline="",encoding="utf-8") as f:
    reader=csv.DictReader(f)#读取内容，并转化为字典，比普通的reader好用
    for row in reader:
        print(row)
        print(row["姓名"],row["成绩"])