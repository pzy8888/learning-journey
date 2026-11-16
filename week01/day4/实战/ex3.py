from pathlib import Path
import string
import json
from skimage.data import retina

data="""
The,quick !brown,fox,jumps over the lazy dog.
A journey of a thousand. miles begins with a single step.
Practice makes perfect, and !perfect practice makes a master.
The best time to plant a. tree ?was twenty years ago.
The second best time is, now.
Knowledge is power, but applied knowledge is more powerful.
Small steps every day lead to big results over time.
The fox and the dog became friends in the end.
Time and tide wait for no man.
Every expert was once a beginner.
"""
def file():
    Path("mistake").mkdir(parents=True, exist_ok=True)
    with open("mistake/text.txt", "w",encoding="utf-8") as f:
        f.write(data)
def long(Path)->int:
    with open(Path,"r",encoding="utf-8") as f:
        lines=f.readlines()
        print(len(lines))
        long=sorted(lines,reverse=True)
        print(long[0])
        return lines
def read(Path:str)->str:
    with open(Path,"r",encoding="utf-8") as f:
        content=f.read()
        return content
def char(text:str)->str:
    text=text.lower()
    for ch in string.punctuation:
        text=text.replace(ch," ")
    return text
def sp(text:str)->dict:
    count={}
    for i in text.split():
        count[i]=count.get(i,0)+1
    return count
def count(count:dict)->list:
    pair=[]
    for i,v in count.items():
        pair.append([v,i])
    a=sorted(pair,reverse=True)
    return a
def write_json(data:list):
    with open("output/ex3.json","w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
def read_json():
     with open("output/ex3.json","r",encoding="utf-8") as f:
         a=json.load(f)
         print(a)

def main():
    for i in Path("mistake").glob("*.txt"):
        a=long(i)
        b=read(i)
        c=char(b)
        d=sp(c)
        e=count(d)
        f=write_json(e)
        read_json()
    return 0
if __name__=="__main__":
    main()