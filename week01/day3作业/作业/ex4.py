def q_c(nm:list):
    a=set(nm)
    print(list(a))
user_input = input("Enter a number: ")
name=user_input.split(",")
#set快，但是无序
def q_c2(name:list):
    answer=[]
    for i in name:
        if i not in answer:
            answer.append(i)
    print(answer)
    return answer
q_c2(name)
#循环慢但是保留顺序
if __name__=="__main__":
    q_c2(name)
    q_c(name)