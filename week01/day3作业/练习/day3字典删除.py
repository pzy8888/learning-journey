def delete():
    d={"a":1,"b":2,"c":3,"d":4}
    d.pop("a",None)
    print(d)
    d.clear()
    print(d)
delete()