d = {"a": 1, "b": 2}
print(d)
print(list(d.keys()))
for k in d:
    print(d)
for k in list(d.keys()):
    del d[k]
    print(d)