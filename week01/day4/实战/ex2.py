def trap(num:int,lst:list=[])->list:
    lst.append(num)
    return lst
def right(num:int,lst:list=None)->list:
    if lst is None:
        lst=[]
    lst.append(num)
    return lst
def main():
    print("错误的版本：")
    print(trap(1))
    print(trap(2))
    print("**********")
    print("正确的版本:")
    print(right(3))
    print(right(4))
if __name__ == "__main__":
    main()