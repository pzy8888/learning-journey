from pathlib import Path
import string
import json
import csv
sample = """The,quick brown,fox,jumps over the lazy dog.
A journey of a thousand miles begins with a single step.
Practice makes perfect, and !perfect practice makes a master.
The best time to plant a tree ?was twenty years ago.
The second best time is now.
Knowledge is power, but applied knowledge is more powerful.
Small steps every day lead to big results over time.
The fox and the dog became friends in the end.
Time and tide wait for no man.
Every expert was once a beginner.
"""
data ="""
关键词
[25年度表情包_伸手][25年度表情包_伸手][25年度表情包_伸手][25年度表情包_伸手]
《图书馆》

美术风格
高品质3D游戏CG美术，Unity引擎渲染，融合二次元卡通渲染与物理基础渲染的光影质感。

场景环境
午后学校图书馆，高窗斜阳在深色木桌上投下条纹光斑。书架林立，自习区空荡安静。

角色设定
少女A：形象参考图一，刘海下是黑色蕾丝眼罩，弱气痴女，站在角落靠窗的桌子前，远远望着斜对面的少女B。
少女B：形象参考图二，气质沉静，坐在远处靠墙桌旁专注看书，与少女A隔着数排空桌椅。

分镜

0-1.5s【注视】
中景，少女A全身入镜。她站在角落靠窗的桌子前，双手搭在桌沿，视线越过数排空桌椅，痴痴落在远处少女B身上。少女B侧脸映在午后光线里专注翻书。切至少女A面部，嘴角缓缓翘起。
音效：远处翻书页细响，略显急促的呼吸。

1.5-6s【倚靠桌角】
镜头维持中景。少女A的双手从桌沿滑向桌子一角，身体侧转，将桌角迎入身前。她微微分开双腿，身体前倾，让桌角的木质棱线正好抵入腰腹之间。双手撑住桌沿，整个重心向前压去。静止片刻后，身体开始前后轻晃，桌角隔着衣料在腰腹处来回蹭动，节奏由慢渐快，幅度虽小却带着急切的意味。她的呼吸随之变乱，嘴唇微启，眼神仍痴痴望着远处少女B，脸上的痴笑渐渐加深。晃动持续了数秒，她的身体几乎完全压在桌角上，手指攥紧桌沿指节发白，喉咙里漏出几声细弱的轻叹。
音效：衣料与桌角来回蹭动的沙沙声，节奏由慢渐快，略显紊乱的鼻息，几声细弱的轻叹。
6-7.5s【被发现】
晃动骤停。远处少女B翻书的手指停在半空，缓缓抬起头，穿过整排空桌椅朝这边看来。少女A双手猛地松开，整个身体向后弹开，后背撞上书架，一本书滑落摔在地上。面色瞬间通红。
音效：书脊撞书架闷响，书本落地脆响，剧烈心跳。

7.5-9s【逃跑】
手持跟拍少女A踉跄转身，画面晃动。她弯腰捞起书，在书架间跌撞奔跑，怀里书散落一地。镜头停在书架深处消失的背影上。
音效：慌乱脚步，书册落地扑簌声，剧烈喘息。

9-10s【桌角痕迹】
镜头缓慢摇回，从少女A消失的过道平移至她刚才倚靠过的空桌。焦点落在桌角棱线上，深色木质上一道浅浅的湿润痕迹在午后斜阳下泛着微光。远处少女B垂下眼，目光越过数排桌椅落在那道痕迹上，睫毛轻轻垂了一下，片刻后收回目光继续看书。画面停在她翻书的指尖上。淡出。
音效：翻书页轻响，窗外鸟鸣渐远。



"""
def file():
    Path("data").mkdir(parents=True, exist_ok=True)
    with open("data/test2.txt", "w",encoding="utf-8") as f:
        f.write(sample)
    with open("data/test.txt", "w",encoding="utf-8") as f:
        f.write(data)
    print(f"文件已经创建完成,共{len(sample)}个字符")
text=None
def read_file(text:str):
    for i in Path("data").glob("*.txt"):
        with open(i,"r",encoding="utf-8") as f:
            content=f.read()
            text=content
    return text
def clean_char(text:str):
    text=text.lower()
    for ch in string.punctuation:
        text=text.replace(ch,"")
    return text

def count_char(text:str):
    count={}
    pair=[]
    pair2=[]
    for i in text.split():
        count[i]=count.get(i,0)+1
    for i,num in count.items():
        pair2.append([num,i])
    b=sorted(pair2,reverse=True)
    print(b)
    return b
def JSON_char(pair:list):
    with open("data/Json.txt","w",encoding="utf-8") as f:
        json.dump(pair,f,ensure_ascii=False,indent=4)

def CS(pair:list):
    print(pair)
    pair.insert(0,["次数","单词"])
    with open("data/word.csv","w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(pair)
a=read_file(text)
b=clean_char(a)
c=count_char(b)
d=JSON_char(c)
e=CS(c)