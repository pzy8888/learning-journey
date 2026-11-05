# Git 入门实操课（Day 1 补充）

> 目标：90 分钟内不仅能敲命令，而且真的理解 Git 在干什么
> 前提：你的 `learning-journey` 仓库已经能 `push` 了

---

## 一、一句话心智模型

> **Git 不是"保存文件"，是"给整个项目的状态拍快照，并且这些快照连成一棵树"。**

理解这一句，你就理解 Git 了。后面所有命令都只是在操作这棵树。

三个关键概念：

| 概念 | 是什么 | 类比 |
|---|---|---|
| **commit** | 一次快照，包含当时所有文件的内容 + 作者 + 时间 + 说明 + 父提交 | 一张存档 |
| **分支（branch）** | 指向某个 commit 的**可移动指针** | 书签，会跟着你走 |
| **HEAD** | 指向"你现在在哪个分支/哪个快照" | 你站的位置 |

注意：**分支只是指针，不是文件夹拷贝。** 创建分支几乎瞬间完成，因为只写了一个 41 字节的引用。这就是为什么 Git 鼓励你随便开分支。

---

## 二、四个区域（这是最重要的图）

```
工作区                 暂存区                 本地仓库              远程仓库
(Working Dir)    →    (Staging/Index)   →    (Repository)   →    (Remote/GitHub)
   你正在改的文件        git add 之后           git commit 之后        git push 之后
                     
                     ← git restore          ← git reset           
```

**一句话记住每个命令把东西在哪两个区之间搬：**

| 命令 | 把东西从 → 搬到 |
|---|---|
| `git add` | 工作区 → 暂存区 |
| `git commit` | 暂存区 → 本地仓库 |
| `git push` | 本地仓库 → 远程仓库 |
| `git pull` / `fetch` | 远程仓库 → 本地仓库（+ 工作区） |
| `git restore` | 用本地仓库的版本覆盖工作区（**丢弃修改**） |

**为什么要"暂存区"这一层？** 因为它允许你**挑着提交**：改了 5 个文件，但只想提交其中 2 个相关的。这在真实项目里非常有用（一次提交只做一件事）。

---

## 三、命令分层（按你实际使用频率）

### 🥇 第一层：每天都用（占 80% 操作）

```bash
git status                  # 看现在什么情况（最高频，多敲没坏处）
git diff                    # 看还没 add 的改动内容
git diff --staged           # 看已经 add 的改动内容
git add 文件名               # 添加单个文件
git add .                   # 添加所有改动
git commit -m "说明"         # 提交
git log --oneline           # 看提交历史（一行一条）
git push                    # 推到 GitHub
```

**新手建议：每次 `git add` / `commit` / `push` 之前，先敲一次 `git status`。** 养成肌肉记忆，能避免 90% 的"我怎么推上去一堆不该推的东西"。

### 🥈 第二层：每周都用

```bash
git log --oneline --graph --all    # 看分支树（好看且有用）
git log -p 文件名                  # 看某文件的每次改动细节
git show 提交号                    # 看某次提交改了什么
git blame 文件名                   # 每一行是谁在哪次提交改的（查 bug 神器）
git stash                          # 临时把手上的改动存起来
git stash pop                      # 取回来
git branch                         # 列出分支
git switch -c 新分支名              # 建并切到新分支
git switch 分支名                   # 切分支
git merge 分支名                    # 把某分支合并到当前分支
```

### 🥉 第三层：偶尔用但必须懂（撤销相关，见下一节）

```bash
git restore 文件名
git restore --staged 文件名
git reset --soft HEAD~1
git revert 提交号
git reset --hard 提交号     # ⚠️ 危险
```

---

## 四、撤销三兄弟（最容易搞混，务必看懂这张表）

**先问自己一个问题：改动走到哪一步了？**

| 改动的状态 | 想撤销怎么办 | 危险度 |
|---|---|---|
| **① 改了文件，还没 `add`** | `git restore 文件名` | 安全（丢弃修改） |
| **② 已经 `add`，还没 `commit`** | `git restore --staged 文件名`（取消暂存，改动还在） | 安全 |
| **③ 已经 `commit`，还没 `push`** | `git reset --soft HEAD~1`（撤销提交，改动留在暂存区） | 安全 |
| **④ 已经 `commit` 且已经 `push`** | `git revert 提交号`（生成一个"反向提交"来抵消） | 安全 ✅ 推荐 |
| ❌ 任何情况 | `git reset --hard 提交号` | **⚠️ 会永久丢代码** |

### `git reset` 三兄弟的区别（面试常问）

```bash
git reset --soft HEAD~1    # 撤销 commit，改动全部留在暂存区（最安全，推荐）
git reset --mixed HEAD~1   # 撤销 commit + 取消暂存，改动留在工作区（默认行为）
git reset --hard HEAD~1    # 撤销 commit + 取消暂存 + 丢弃改动（代码没了）
```

`HEAD~1` 的意思是"上一个提交"。`HEAD~3` 就是往前三个。

### `reset` 和 `revert` 的本质区别

- **`reset`**：**改写历史** —— 假装那个提交从来没发生过。只适合**还没 push** 的情况。如果你 push 了还 reset，别人拉代码会炸。
- **`revert`**：**新增一个提交** —— 历史的记录还在，只是又加了一笔把之前的改动抵消掉。**已经 push 了就用这个。**

> **背下来这条规则：push 之前用 reset，push 之后用 revert。**

### 如果已经 `--hard` 丢了代码怎么办？

别急，Git 通常还没真删，试试：

```bash
git reflog
```

`reflog` 记录了 HEAD 的每一次移动（包括你认为"丢了"的那次）。找到丢失前的提交号，然后：

```bash
git reset --hard 那个提交号
```

**`reflog` 是后悔药。** 记住它。

---

## 五、commit message 怎么写（这一条会影响面试）

面试官看你的 GitHub，**提交历史是第二份简历**。一堆 `update`、`fix`、`111`、`asdf`，会直接拉低印象。

用 **Conventional Commits** 规范，格式：

```
类型: 简短说明（不超过 50 字）
```

| 类型 | 什么时候用 |
|---|---|
| `feat` | 新功能 |
| `fix` | 修 bug |
| `docs` | 只改文档 |
| `refactor` | 重构（不改功能） |
| `test` | 加测试 |
| `chore` | 杂务（改配置、装依赖） |
| `style` | 格式调整（空格、缩进） |

**好例子：**

```
feat: 实现温度换算练习
fix: 修正 BMI 公式的运算优先级错误
docs: 补充切片左闭右开的说明
refactor: 把字符串处理逻辑拆成独立函数
test: 为 BMI 计算补充边界用例
```

**坏例子：** `update`、`修改`、`1`、`终于好了`、`aaa`

为什么值得花 30 秒写清楚？因为**半年后你会靠这些信息找回"当时为什么这么改"**，那时候你早就忘了。

---

## 六、⚠️ 三个必须现在就养成的安全习惯

### 1. API Key 绝对不能进 Git

你后面写 AI 项目一定会拿到 DeepSeek / OpenAI 的 API Key。**一旦 commit 并 push 到公开仓库，几分钟内就会被爬虫扫走，有人一晚上被刷几千块。**

**正确做法：**

```bash
# 1. 建 .env 文件放密钥
echo "DEEPSEEK_API_KEY=sk-xxxxxx" > .env

# 2. 在 .gitignore 里加一行 .env
echo ".env" >> .gitignore

# 3. 建一个 .env.example 提交上去，告诉别人需要哪些变量（但值留空）
echo "DEEPSEEK_API_KEY=" > .env.example
```

```python
# 4. 代码里这样读
import os
api_key = os.getenv("DEEPSEEK_API_KEY")
```

**如果已经不小心提交了**：立刻去平台**吊销那个 Key**（最重要！），然后才处理 Git 历史。只删文件没用，历史里还在。

### 2. 该忽略的文件

```bash
# .gitignore
__pycache__/
*.pyc
.venv/
venv/
.env
.DS_Store
*.log
.idea/
.vscode/
data/          # 大文件不要进 Git
```

### 3. 不要 commit 大文件

Git 不擅长处理二进制大文件（视频、数据集、模型权重）。一旦提交，仓库体积会永久膨胀。超过 10MB 的文件先想想要不要进 Git。

---

## 七、实操练习（今天就做，60 分钟）

> 在你的 `~/code/learning-journey` 目录里做。**每一步都敲一次 `git status` 和 `git diff` 观察变化。**

### 练习 1｜走一遍四区流转（10 分钟）

```bash
cd ~/code/learning-journey

# 建个文件
echo "第一行" > week01/lab.txt
git status            # 观察：untracked（未跟踪）

git add week01/lab.txt
git status            # 观察：Changes to be committed（已暂存）

git commit -m "chore: 测试四区流转"
git status            # 观察：nothing to commit

git log --oneline     # 看到新提交
```

**要观察到的**：同一个文件，在 `git status` 里出现了**三种不同状态**。这就是三个区域。

### 练习 2｜撤销一次提交（15 分钟）

```bash
# 追加内容并提交
echo "第二行" >> week01/lab.txt
git add . && git commit -m "chore: 测试撤销"

# 现在想把"测试撤销"这次提交退掉，但保留改动
git reset --soft HEAD~1
git status            # 观察：改动还在暂存区
git log --oneline     # 观察：那次提交没了

# 重新提交（换个更好的说明）
git commit -m "chore: lab.txt 追加第二行"
```

**再试一次 `--mixed`：**

```bash
echo "第三行" >> week01/lab.txt
git add . && git commit -m "chore: 再测一次"
git reset HEAD~1          # 不写 = --mixed
git status                # 观察：改到工作区了，没暂存
```

### 练习 3｜制造并解决一次合并冲突（15 分钟）★最有价值

冲突是新手最怕的事，但**你至少要在学习环境里主动踩一次**。

```bash
# 确保在 main 上，且是干净的
git switch main
git status

# 建分支并改文件
git switch -c feature-a
echo "这是分支A的改动" > week01/conflict.txt
git add . && git commit -m "feat: 分支A添加conflict.txt"

# 切回 main，改同一个文件的同一行
git switch main
echo "这是main的改动" > week01/conflict.txt
git add . && git commit -m "feat: main添加conflict.txt"

# 合并 —— 冲突来了
git merge feature-a
```

你会看到：

```
Auto-merging week01/conflict.txt
CONFLICT (add/add): Merge conflict in week01/conflict.txt
Automatic merge failed; fix conflicts and then commit the result.
```

打开 `week01/conflict.txt`，会看到：

```
<<<<<<< HEAD
这是main的改动
=======
这是分支A的改动
>>>>>>> feature-a
```

**解决方式**：手动编辑这个文件，删掉 `<<<<<<<`、`=======`、`>>>>>>>` 这三行标记，留下你想要的最终内容（或者两者都留）：

```
这是main的改动
这是分支A的改动
```

然后：

```bash
git add week01/conflict.txt
git commit -m "merge: 合并feature-a，解决conflict.txt冲突"
git log --oneline --graph --all      # 看分支树，很直观
```

**记住一句话：冲突不是错误，是 Git 让你做决定。**

### 练习 4｜stash 临时保存（10 分钟）

场景：代码改到一半，突然要切分支修别的东西。

```bash
echo "半成品代码" >> week01/lab.txt
git status                    # 有未提交的改动

git stash                     # 收起来
git status                    # 干净了
git stash list                # 看到刚才存的

git stash pop                 # 取回来，继续干
git status                    # 改动回来了
```

### 练习 5｜用 blame 和 log -S 查问题（10 分钟）

```bash
# 每一行是谁在哪个提交改的
git blame week01/lab.txt

# 查出"哪次提交引入/删除包含某段文字"
git log -S "第二行" --oneline

# 看某次提交的完整改动
git show 提交号
```

**这两个命令在真实工作中用来"这行莫名其妙的代码是谁写的、为什么写的"，非常好用。**

### 练习 6｜配好 .gitignore 和别名（5 分钟）

```bash
cd ~/code/learning-journey

cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.venv/
venv/
.env
.DS_Store
*.log
EOF

git add .gitignore
git commit -m "chore: 添加 .gitignore"

# 设几个别名，省打字
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.last "log -1 --stat"

# WSL 里必须设这个，否则 Windows 换行符会搞乱一切
git config --global core.autocrlf input

git push
```

以后 `git st` 就等于 `git status`，`git lg` 就是那个好看的分支树。

---

## 八、常见坑速查

| 现象 | 原因 | 解决 |
|---|---|---|
| `fatal: not a git repository` | 不在仓库目录里 | `cd` 到正确目录，或 `git init` |
| `rejected - non-fast-forward` | 远程有你本地没有的提交 | 先 `git pull` 再 push |
| `Permission denied (publickey)` | SSH 钥匙没用上 | 检查公钥是否加到 GitHub，`ssh -T git@github.com` |
| 每次 `git status` 一堆文件被修改 | Windows/WSL 换行符 | `git config --global core.autocrlf input` |
| `detached HEAD` | 切到了某个提交而不是分支 | `git switch main` 回主分支 |
| 提交了不该提交的文件 | 忘了 .gitignore | `git rm --cached 文件名`（从版本库移出，文件本身保留） |
| 想改最后一次提交的说明 | — | `git commit --amend -m "新说明"` |
| 想把某个提交单独摘到当前分支 | — | `git cherry-pick 提交号` |

---

## 九、工作里 Git 的标准协作流程（了解即可）

你现在是单人开发，但上班后大概是这样：

```
1. 从 main 拉最新：        git switch main && git pull
2. 开功能分支：            git switch -c feature/xxx
3. 开发，多次小提交：      git add . && git commit -m "feat: ..."
4. 推分支：                git push -u origin feature/xxx
5. 在 GitHub 提 Pull Request（PR）
6. 同事 Code Review，你改
7. 合并进 main，删掉分支
```

**注意第 3 步：小步提交。** 一天一个大提交（500 行改动）是最糟糕的实践——出问题无法定位，也没人看得懂你的 PR。

**面试常问**：`git merge` 和 `git rebase` 的区别？
> 答：都会整合分支。`merge` 保留完整历史并生成一个合并提交（历史真实但有分叉）；`rebase` 把你的提交"搬到"目标分支末尾，历史变成一条直线（干净但改写了提交号）。**铁律：只对还没 push 的本地提交做 rebase。**

---

## 十、今晚的验收

- [ ] 练习 1~6 全部做完
- [ ] 成功制造并解决了一次合并冲突
- [ ] `git lg` 能看到分叉和合并的图形
- [ ] `.gitignore` 里包含 `.env`、`__pycache__/`、`.venv/`
- [ ] 能不看笔记回答：
  - `git add` 和 `git commit` 分别把东西搬到哪个区？
  - 已经 push 的提交想撤销，用 `reset` 还是 `revert`？为什么？
  - `git reset --hard` 之后代码还能找回吗？用什么命令？
  - 分支到底是什么？（答案：一个指向提交的指针）
