import csv
rows=[
    ["姓名","科目","成绩"],
    ["张三","数学","88"],
    ["李四","语文","78"]
]
with open("scores.csv","w",newline="",encoding="utf-8") as f:#newline不能省，不然中间会有空格
    writer = csv.writer(f)
    writer.writerows(rows)