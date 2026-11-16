import csv
data=[
    ["姓名","科目","成绩"],
    ["小红","体育","88"],
    ["小米","体育","90"],
    ["张三","体育","78"],
    ["李四","体育","67"]
]
def create_csv():
    with open('data/ex5.csv', 'w', newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_csv2()->list:
    with open('data/ex5.csv',"r",newline='',encoding="utf-8") as f:
        reader = csv.DictReader(f)
        s=0
        n=0
        lst=[["平均分"]]
        for row in reader:
            a=int(row["成绩"])
            s+=a
            n+=1
        S=s/n
        lst.append([S])
        print(lst)
        print(f"平均成绩保留两位小数后为{s/n:.2f}")
    return lst
def write_csv(lst:list=None):
    with open('data/ex5.csv',"a",newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(lst)
create_csv()
a=read_csv2()
write_csv(a)