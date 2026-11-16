def word_count(text:str)->dict[str:int]:#类型注解的意思是，输入一个str字符串，返回一个字典，字典内部字符串和int值对应
    counts={}
    for word in text.split():
        counts[word]=counts.get(word,0)+1
    return counts