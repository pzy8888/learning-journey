def di_gui(n:int):
    if n<=1:
        return 1
    return n*di_gui(n-1)
print(di_gui(6))