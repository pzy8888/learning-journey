import json
data={
    "name":"小明",
    "age": 21,
    "tags": ["Python", "AI"],
    "scores": {"math": 90, "english": 85,"chinese":88},

}
s=json.dumps(data,ensure_ascii=False,indent=2)
print(s)
obs=json.loads(s)
print(obs)
print(obs["tags"][0])
print(obs.get("scores",{}).get("english",0))
with open("data/out.json","w",encoding="utf-8") as f:
    json.dump(obs,f,ensure_ascii=False,indent=2)#将数据转换为json格式并写入文件