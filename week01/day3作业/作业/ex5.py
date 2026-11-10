import time
def time():
    big_list = list(range(100000))
    big_set = set(big_list)

    # 在列表里找最后一个元素，做 1000 次
    start = time.time()
    for _ in range(1000):
        99999 in big_list
    print(f"list 查找 1000 次：{time.time() - start:.4f} 秒")

    # 在集合里找，做 1000 次
    start = time.time()
    for _ in range(1000):
        99999 in big_set
    print(f"set  查找 1000 次：{time.time() - start:.4f} 秒")


if __name__ == "__main__":
    time()