def create_user(name:str,city:str,age:int=21):
    print(name,age,city)
    return name,age,city
create_user(name="小明",city="荆州",age=24)