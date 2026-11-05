# Day 1｜环境搭建 + Python 基础语法 I

> 日期：2026-11-04（周三）
> 目标：跑通开发环境 + 能独立写出带输入的字符串处理小程序
> 总时长：3 小时

---

## 今日时间表

| 时间 | 做什么 |
|---|---|
| 0:00–0:45 | 环境搭建（WSL2 / Python / Git / uv） |
| 0:45–1:15 | 语法讲解，跟着敲一遍 |
| 1:15–2:30 | 6 道练习题，自己写 |
| 2:30–3:00 | 建仓库、第一次提交、写 3 行笔记 |

---

# 第一步：环境搭建（45 分钟）

## 1.1 确认系统

先在终端里确认你是 Windows 还是 Mac：

- **Windows** → 走 1.2 装 WSL2
- **Mac** → 跳过 1.2，直接走 1.3，终端就是你的 Linux 环境

## 1.2 Windows：装 WSL2 + Ubuntu（约 20 分钟，可能要重启）

**以管理员身份**打开 PowerShell（开始菜单搜 PowerShell → 右键 → 以管理员身份运行），执行：

```powershell
wsl --install
```

它会自动装好 WSL2 + Ubuntu。装完**重启电脑**。

重启后 Ubuntu 会自动弹出，让你设置用户名和密码（**密码输入时屏幕不显示，这是正常的**，输完回车）。

验证：

```powershell
wsl -l -v
```

应该看到 `Ubuntu`，且 `VERSION` 是 `2`。

> **如果 `wsl --install` 报错**：先跑 `wsl --update`，再重试。
> **如果已经装过 WSL 但没有 Ubuntu**：跑 `wsl --install -d Ubuntu-22.04`

## 1.3 装 Python 工具链（在 Ubuntu 终端里执行）

打开 Ubuntu 终端（开始菜单搜 Ubuntu，或 PowerShell 里输 `wsl`），依次执行：

```bash
# 更新软件源
sudo apt update && sudo apt upgrade -y

# 装 Python 必备组件
sudo apt install -y python3 python3-pip python3-venv git curl

# 验证
python3 --version     # 应该显示 Python 3.10.x 或更高
git --version
```

**注意：这里用 `python3` 而不是 `python`。** 后面所有命令都用 `python3`。

## 1.4 装 uv（Python 包管理器）

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

装完终端会提示你 `source` 某个文件，或者**关掉终端重新打开**。

验证：

```bash
uv --version
```

## 1.5 配置 Git

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
git config --global init.defaultBranch main

# 生成 SSH 密钥（一路回车即可）
ssh-keygen -t ed25519 -C "你的邮箱@example.com"

# 查看公钥，复制输出的全部内容
cat ~/.ssh/id_ed25519.pub
```

然后去 GitHub → Settings → SSH and GPG keys → New SSH key → 粘贴。

测试连接：

```bash
ssh -T git@github.com
```

看到 `Hi 你的用户名! You've successfully authenticated` 就成功了。

## 1.6 装 VS Code 并连上 WSL

1. 下载安装 VS Code（Windows 版）
2. 打开 VS Code，在扩展里搜 **WSL**，安装微软官方那个
3. 在 Ubuntu 终端里进入你要放代码的目录，执行 `code .`

```bash
mkdir -p ~/code && cd ~/code
code .
```

VS Code 会打开，左下角显示 `WSL: Ubuntu` 就对了。

## 1.7 建仓库

在 Ubuntu 终端：

```bash
cd ~/code
mkdir learning-journey && cd learning-journey
git init
mkdir week01
echo "# 我的学习记录" > README.md
git add .
git commit -m "init: 初始化学习仓库"
```

**✅ 环境搭建完成标志**：上面 `git commit` 成功输出了提交信息。

---

# 第二步：Python 基础语法 I（30 分钟，跟着敲）

> 规则：看一小段就自己敲一遍，**不要复制粘贴**。手打才会形成记忆。

## 2.1 第一个程序

在 `week01/` 下建文件 `hello.py`：

```python
print("Hello, Python")
print(1 + 1)
```

运行：

```bash
python3 week01/hello.py
```

## 2.2 变量：不用声明类型

```python
name = "小明"      # 字符串 str
age = 21           # 整数 int
height = 178.5     # 小数 float
is_student = True  # 布尔 bool
nothing = None     # 空值 None

print(name, age, height, is_student, nothing)
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
```

**要点**：Python 是动态类型，变量名只是"标签"，`a = 1` 之后 `a = "文本"` 也合法（但不建议这么干）。

## 2.3 类型转换

```python
a = "123"
print(a + "4")        # "1234"  ← 字符串拼接
print(int(a) + 4)     # 127     ← 转成整数再算

b = 3.99
print(int(b))         # 3       ← 直接截断，不四舍五入
print(round(b))       # 4       ← round 才四舍五入
```

## 2.4 算术运算符（重点记住后两个）

```python
print(7 + 3)    # 10
print(7 - 3)    # 4
print(7 * 3)    # 21
print(7 / 3)    # 2.3333...  ← 单斜杠永远返回 float
print(7 // 3)   # 2          ← 双斜杠：整除，取整数部分
print(7 % 3)    # 1          ← 取余数
print(7 ** 3)   # 343        ← 幂
```

## 2.5 字符串

```python
s = "Hello World"

print(len(s))          # 11        长度
print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
print(s.strip())       # 去掉首尾空白（常用于清洗用户输入）
print(s.split(" "))    # ['Hello', 'World']  按空格切成列表
print(s.replace("World", "Python"))  # Hello Python
print("World" in s)    # True       判断包含
print(s[0])            # H          取第 0 个字符
print(s[0:5])          # Hello      切片，左闭右开
```

## 2.6 f-string：格式化输出的标准做法

```python
name = "小明"
age = 21
score = 87.456

print(f"我叫{name}，今年{age}岁")
print(f"成绩保留一位小数：{score:.1f}")   # 87.5
print(f"成绩保留两位：{score:.2f}")       # 87.46
print(f"百分数：{0.873:.1%}")             # 87.3%
```

**这是最常用的技能**，后面所有项目输出都靠它。

## 2.7 input()：接收用户输入

```python
name = input("请输入你的名字：")
print(f"你好，{name}")

age = input("请输入年龄：")
print(type(age))          # <class 'str'>  ← 注意！是字符串
print(int(age) + 1)       # 必须转换才能算
```

**⚠️ 最重要的坑：`input()` 永远返回字符串。** 要算数必须先 `int()` 或 `float()`。

## 2.8 注释和缩进

```python
# 这是单行注释

"""
这是多行注释（其实是字符串，但常这么用）
"""

age = 18
if age >= 18:
    print("成年")        # ← 缩进 4 个空格，Python 靠缩进划分代码块
    print("可以投票")
else:
    print("未成年")
```

**⚠️ 缩进必须统一用 4 个空格，不要混 Tab。** 混用会报 `IndentationError`。

---

# 第三步：6 道练习题（90 分钟）

> 规则：**先自己写，卡住 10 分钟再看答案**。写在 `week01/` 目录下，每道一个文件。
> 不需要一次全做完，做完 4 道就算达标。

## 练习 1｜个人名片（热身，10 分钟）

文件：`week01/ex1_card.py`

要求：定义 4 个变量（姓名、专业、年级、一个爱好），用 **f-string** 打印成下面格式：

```
====================
姓名：小明
专业：人工智能
年级：大四
爱好：打篮球
====================
```

## 练习 2｜温度换算（15 分钟）

文件：`week01/ex2_temp.py`

要求：
- 用 `input()` 读入一个摄氏温度
- 转成华氏温度：`华氏 = 摄氏 * 9 / 5 + 32`
- 输出格式：`36.5°C = 97.7°F`（**保留 1 位小数**）

测试数据：输入 `36.5`，应输出 `36.5°C = 97.7°F`

## 练习 3｜字符串体检（20 分钟）

文件：`week01/ex3_str.py`

要求：给定 `s = "  Hello Python World  "`，输出：

```
原始长度：22
去空格后长度：18
大写：HELLO PYTHON WORLD
单词个数：3
是否包含 "Python"：True
```

> 提示：`len()`、`.strip()`、`.upper()`、`.split()`、`in`

## 练习 4｜用户输入清洗（20 分钟）

文件：`week01/ex4_clean.py`

要求：
- 用 `input()` 读入用户名字
- 去掉首尾空格
- 全部转成大写
- 打印 `欢迎你，XXX！`
- 如果用户输入为空（直接回车），打印 `名字不能为空`

测试：输入 `  张三  ` → 输出 `欢迎你，张三！`（这里你想一下：要保留中文原名还是转大写？两种都写一遍，想想哪种更合理）

## 练习 5｜BMI 计算器（20 分钟）

文件：`week01/ex5_bmi.py`

要求：
- 读入身高（米，如 `1.75`）和体重（公斤，如 `68`）
- BMI = 体重 / 身高²
- 输出：`BMI = 22.2`（保留 1 位小数）

> 提示：平方是 `**2`

## 练习 6｜变量交换（挑战，15 分钟）

文件：`week01/ex6_swap.py`

要求：不用第三个变量，把 `a = 1` 和 `b = 2` 交换过来，打印交换结果。

> 提示：Python 有一种非常简洁的写法，一行就能完成。想不到先写"用第三个变量"的版本也行。

---

# 第四步：收尾（15 分钟）

## 4.1 提交代码

```bash
cd ~/code/learning-journey
git add .
git commit -m "feat: Day1 环境搭建与 Python 基础练习"
```

## 4.2 建笔记文件

在 `week01/` 下建 `notes.md`，写 **3 行**（不要多写）：

```markdown
# Day 1 笔记

## 今天学会的 3 件事
1. 
2. 
3. 

## 踩到的坑
- 

## 还没懂的
- 
```

## 4.3 今日验收（全部打勾才算完成）

- [ ] `wsl -l -v` 能看到 Ubuntu，VERSION 是 2
- [ ] `python3 --version`、`git --version`、`uv --version` 都有输出
- [ ] `ssh -T git@github.com` 认证成功
- [ ] VS Code 左下角显示 `WSL: Ubuntu`
- [ ] 6 道练习题至少完成 4 道，能独立跑通
- [ ] 至少 1 次 git commit 成功
- [ ] 能不看资料说出：`/` 和 `//` 的区别、`input()` 返回什么类型

---

# 附：参考答案

> **先自己写完再看。**

<details>
<summary>练习 2 答案</summary>

```python
c = float(input("请输入摄氏温度："))
f = c * 9 / 5 + 32
print(f"{c}°C = {f:.1f}°F")
```
</details>

<details>
<summary>练习 3 答案</summary>

```python
s = "  Hello Python World  "
print(f"原始长度：{len(s)}")
cleaned = s.strip()
print(f"去空格后长度：{len(cleaned)}")
print(f"大写：{cleaned.upper()}")
print(f"单词个数：{len(cleaned.split())}")
print(f"是否包含 \"Python\"：{'Python' in cleaned}")
```
</details>

<details>
<summary>练习 4 答案</summary>

```python
name = input("请输入名字：").strip()

if name == "":
    print("名字不能为空")
else:
    # 方案 A：转大写（英文名适用）
    print(f"欢迎你，{name.upper()}！")
    # 方案 B：保留原样（中文名适用，更合理）
    print(f"欢迎你，{name}！")
```
**思考题**：中文没有大小写，`"张三".upper()` 返回 `"张三"` 本身，所以不报错。但如果是英文名，转大写就变了。**真实项目里"清洗"要按业务场景决定做什么，不能无脑转大写。** 这就是"数据清洗"的第一课。
</details>

<details>
<summary>练习 5 答案</summary>

```python
h = float(input("请输入身高（米）："))
w = float(input("请输入体重（公斤）："))
bmi = w / (h ** 2)
print(f"BMI = {bmi:.1f}")
```
</details>

<details>
<summary>练习 6 答案</summary>

```python
a = 1
b = 2
print(f"交换前：a={a}, b={b}")

a, b = b, a          # Python 的元组解包，一行搞定
print(f"交换后：a={a}, b={b}")
```
</details>

---

# 新手 5 大坑（今天一定会遇到至少 2 个）

| 坑 | 后果 | 怎么避免 |
|---|---|---|
| **中文标点**：用了 `“”`、`（）`、`，` | `SyntaxError: invalid character` | 确保输入法在英文状态，或在编辑器里设成英文标点 |
| **缩进混乱**：混用 Tab 和空格 | `IndentationError` | VS Code 设置：Tab Size = 4，勾选 Insert Spaces |
| **`input()` 忘了转换** | `TypeError: can only concatenate str` | 记住 `input()` 永远返回 str |
| **`=` 和 `==` 搞混** | 赋值变比较，逻辑错 | `=` 是赋值，`==` 是比较 |
| **`/` 和 `//` 搞混** | 结果多出小数 | `/` 返回 float，`//` 才是整除 |

**遇到报错的第一件事：从下往上读最后一行。** 它告诉你错误类型和行号。养成读报错的习惯，比什么都重要。

---

# 明天预告（Day 2）

- 条件判断 `if / elif / else`、比较运算符
- 循环 `for` / `while`、`range()`、`break` / `continue`
- **列表**：增删改查、切片、排序
- 练习：九九乘法表、判断素数、词频统计
