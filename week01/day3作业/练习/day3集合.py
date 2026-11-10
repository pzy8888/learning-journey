s = {1, 2, 3}
s.add(4)          # 加一个
s.remove(1)       # 删（不存在会报 KeyError）
s.discard(99)     # 删（不存在也不报错）
print(2 in s)     # True   ← O(1)，非常快
s.update([5, 6])  # 批量加
