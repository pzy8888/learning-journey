=================================================================================================
*什么是git？
一种版本控制系统，git仓库存有所有的版本信息，能记录每一次修改的信息，如果想要分享仓库就需要从本地仓库发送到远端仓库，GitHub则是最大的免费远端仓库

git用法:
git 保存的是快照也就是commit
每提交一次，都会保存当时仓库的版本快照，随着commit越来越多，最终会形成可随时回溯的版本历史，能看到每一次版本的改动。

1.怎么判断仓库是不是正常的，运行git status -sb查看仓库当前状态
输出：
main...origin/main → 已关联远程，状态正常
main...origin/main [ahead 1] → 有 1 个提交还没推
main → 完全没有关联，push 从来没成功过 

2.怎么查看仓库的根目录 ---->输入git rev-parse --show-toplevel

3.查看当前分支 -->输入git branch 
什么是分支 branch？ ---类似于书签，是记录某个commit的指针，能够帮助查找特定的commit版本
怎么切换分支？ --git switch
那什么是HEAD？ ---类似现在所在的位置

4.如何建立git仓库？-->使用git init（让文件夹变成Git仓库）

5.本地仓库有哪些区域？ 工作区--> 暂存区 -->本地仓库
git add //把改动从“工作区”放进“暂存区”，为下一次 commit 做准备
git commit //把暂存区的内容打包，存进“本地仓库”变成一个历史版本
事例：
git add main.py          # 把 main.py 的修改放入暂存区
git add assets/          # 把 assets 目录下所有变化加入暂存区
git add .                # 把当前目录所有变更都加入暂存区

如果要把暂存的放在仓库：
git commit -m "实现坦克移动和开火功能"-->一次commit应该包含文件的版本，提交人，提交时间，提交说明（做了什么）
这样在后续回退的时候能清晰看到不同commit的记录。

例如输入：git commit -m "feat: Day1 环境搭建笔记与6道基础练习"
再利用git log查询提交历史：
Author: pzy <a2105464732@qq.com>
Date:   Thu Nov 5 19:52:08 2026 +0800

    feat: Day1 环境搭建笔记与6道基础练习

日常使用git的流程：
进->看->放->记->送
cd ~/code/learning-journey      # ① 进仓库
git status -sb                  # ② 看现状，输入后查看是否远程连接
git add .                       # ③ 将文件放到暂存区
git commit -m "feat: 说明"       # ④ 拍快照，记录到本地仓库
git push                        # ⑤ 推到 GitHub

额外流程：
git pull     --从远程仓库拉取最新更新，并自动合并到本地仓库。
git restore  --将仓库版本覆盖到工作区
git fetch    --把远程最新情况拿回来，但不修改当前分支,pull=fetch + merge，是否合并由用户决定。
git merge    --把另一条开发线的成果合并进当前分支
git reflog   --记录本地仓库 HEAD 和分支的操作历史，帮助恢复误操作或追踪历史状态。
git commit --amend 修改最后一次提交时的说明

作业流程：
练习 1｜走一遍四区流转（10 分钟）
cd ~/code/learning-journey 
*每次先进终端都要移动到仓库，不移动到仓库所在目录是没办法查看和记录的

echo "第一行" > week01/lab.txt
*echo指用于在终端中显示文本或变量的值，这里是创建一个TXT文件并把“第一行”写进去。

git status            # 观察：untracked（未跟踪）
查看暂存区的状态，如果还修改文件了还没有git add就会提示，暂存后也会显示提交的文件
git add week01/lab.txt
将文件送到暂存区

git commit -m "chore: 测试四区流转"
提交到本地仓库，本次修改的名称为"chore: 测试四区流转"，同时本次快照会记录时间和修改人以及修改信息。

git status            # 观察：nothing to commit
提交到本地仓库后暂存区就没有了
git log --oneline     # 看到新提交
在本地仓库查看快照记录
同类型命令：git log 详细记录   git log --oneline --graph --all 查看修改记录的分支树，通常用于分支合并的情况


练习2 撤销一次提交
echo "第二行" >> week01/lab.txt
在原来文件上再次修改内容

git add . && git commit -m "chore: 测试撤销"
将二次修改的新文件提交到暂存区并记录到本地仓库

git reset --soft HEAD~1
撤销本地仓库的提交记录并保留文件到暂存区

git status            # 观察：改动还在暂存区
撤销后暂存区仍能看到文件记录

git log --oneline     # 观察：那次提交没了
撤销后看不到本地仓库的记录

git commit -m "chore: lab.txt 追加第二行"

练习三 撤回并不暂存
echo "第三行" >> week01/lab.txt
同上，修改文件内容
git add . && git commit -m "chore: 再测一次"
暂存并提交
git reset --mixed HEAD~1
与soft不同，这里撤回后本地仓库的记录消失，文件也不暂存（本地磁盘的文件不变）        
git status                # 观察：改到工作区了，没暂存

练习小结：
练习2,3的不同之处在于撤销本地仓库提交记录后文件的去向，是否暂存？是否丢弃文件？

练习1则是基本的提交流程

练习2,3的注意事项：撤回后本地仓库会回退到上一次提交的时刻，而不是上一个文件提交的时刻，比如文件多次修改且 提交，某次撤回后本次仓库的文件会回到最近一次提交的时刻（最新版的文件也许会存在暂存区，但无论是否在暂存区，磁盘文件都不会改变，除了用hard真丢弃）

*reset = 搬指针。soft 只搬指针；mixed 搬指针 + 清暂存区；hard 连你的代码一起搬。只有 --hard 会动磁盘。

我一开始以为 reset 会让文件回到上一次提交的版本。实际上 reset 只回退提交历史，不碰磁盘文件；lab.txt 之所以变成 untracked，是因为撤销的那次提交正是它被首次创建的提交，退回后 Git 就不认识它了

HEAD~1 的意思是「往上一个提交」，HEAD~3 是往上三个。~n 的 n 就是往前数几个

练习四：冲突解决
确保在 main 上，且是干净的
git switch main
创建或移动到某个分支上（不同分支上是互相看不到提交记录的，切不同分支上提交的修改文件也可能不同）

git status
查看暂存区

git switch -c feature-a
创建名为“feature-a”的分支

echo "这是分支A的改动" > week01/conflict.txt
在相同文件上修改对应内容，便于后续产生冲突，冲突也可以是某个对应数字上的不同

git add . && git commit -m "feat: 分支A添加conflict.txt"
提交记录

git switch main
移动到main分支上
echo "这是main的改动" > week01/conflict.txt
同上修改内容

git add . && git commit -m "feat: main添加conflict.txt"
同一文件，不同分支上的内容不同，现在分别提交到本地仓库的不同分支，再融合就会冲突

git merge feature-a
进行融合，如果没有冲突内容就直接合并

Auto-merging week01/conflict.txt
CONFLICT (add/add): Merge conflict in week01/conflict.txt
Automatic merge failed; fix conflicts and then commit the result.
文件合并报错，报错后要手动打开磁盘文件进行修改，取舍。格式如下：

<<<<<<< HEAD
这是main的改动
=======
这是分支A的改动
>>>>>>> feature-a
**解决方式**：手动编辑这个文件，删掉 `<<<<<<<`、`=======`、`>>>>>>>` 这三行标记，留下你想要的最终内容（或者两者都留）：

*修改后到主分支上进行二次暂存，提交即可。
提交后用git log --oneline --graph --all 能看到冲突的分叉树
注：解决冲突后再主分支能看到其他分支的提交记录，但是其他分支看不到主分支的记录

练习 五｜stash 临时保存（10 分钟）
修改到一半时需要改变方向，去别的分支修东西就用 stash把没修改完的文件收起来即可，后续完成了再用 git stash pop取出来，也能用git stash list 查看收起来的文件列表

流程如下：
echo "半成品代码" >> week01/lab.txt
git status                    # 有未提交的改动

git stash                     # 收起来
git status                    # 干净了
git stash list                # 看到刚才存的

git stash pop                 # 取回来，继续干
git status                    # 改动回来了

练习 6｜用 blame 和 log -S 查问题（10 分钟）

每一行是谁在哪个提交改的
git blame week01/lab.txt

查出"哪次提交引入/删除包含某段文字"
git log -S "第二行" --oneline

看某次提交的完整改动
git show 提交号



易错点：三种撤回方式的不同：
git reset --soft HEAD~n  将commit指针回退到n个版本前，期间提交的文件存入暂存区
git reset --mixed（默认） HEAD~n  将commit指针回退到n个版本前，期间提交的文件离开暂存区，磁盘上的不动
git reset --hard  HEAD~n  将commit指针回退到n个版本前，期间提交的文件会直接删除，磁盘上的也会消失

怎么恢复在本地仓库撤销并删除的文件（未push）
先使用git reflog去查看所有的提交记录，包括撤回的记录和移动到分支的记录
再用：git reset --hard 版本号 重新回退到某个未删除的版本

如果已经push到远程仓库了怎么办？
使用git revert HEAD ：新增一个对应步骤的提交来替换掉撤回的这个改动，类似于生成个反向修改去替换原来的操作，HEAD指撤销最近的一次修改
git revert commit1..commit2：撤销commit1到commit2之间的改动。也是左闭右开
*push 之前用 reset，push 之后用 revert。 如果你 push 了绝不能再用 reset进行修改
另外：git switch -c 里的 -c 是 create（创建），git switch xx 是移动到某个分支，git switch -c xx 是生成新分支xx

远程恢复也可能冲突，
*revert 可能产生冲突，需要手动解决
git revert commit_id
*解决冲突后
git add .
git revert --continue
*或者放弃 revert
git revert --abort

注：撤销是可以撤销某次撤销的结果的，即反反得正

本地撤回
git restore --->撤回本地的修改，会丢失暂存区的文件
git restore --staged xx  -->撤销暂存区的xx文件


统一格式：git commit -m 'type(scope): 描述(#issue)'
init:初始化修改
feat:新特性
fix:本次提交解决了问题
refactor:重新优化了代码
docs:文档修改
style:代码格式修改
test:测试用修改
build:构建项目
chore：其他修改


.gitignore是什么？用来让git忽略某些文件的文件夹，将需要忽略的文件填进.gitignore里面，git会自动忽略它

什么是__pycache：源代码编译为字节码后，字节码缓存的文件，目的是提高编译效率
什么是venv： python运行的独立虚拟环境，可以实现不同版本python软件之间互不干扰
什么是env:配置文件，用来存储环境变量，（比如数据库，或者api这种不能公开的信息）
什么是*.log :操作系统或程序使用的日志


git diff:比较文件的不同，即比较文件在暂存区和工作区的差异

git diff file :查看工作区与暂存区之间的不同

git diff --cached/staged 查看上一次提交在本地仓库的与缓存区的不同

git status告诉我们哪些文件改了
git diff 告诉我们文件改了哪里

git branch -d xx 删除某个分支 d指delete
对比git switch -c xx c指创建