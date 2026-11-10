s = "  hello  "
print((s.strip()))     # 'hello'      首尾都去
print((s.lstrip()))    # 'hello  '    只去左边
print((s.rstrip()))    # '  hello'    只去右边

print("xxhelloxx".strip("x"))   # 'hello'  去首尾的指定字符

print("xxhello".removeprefix("xx"))   # hello
print("helloxx".removesuffix("xx"))   # hello

print("今天天气不错".removeprefix("今天"))
print("今天天气不错".strip("今天"))