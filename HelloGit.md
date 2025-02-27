# 常用 Git 命令清单

Git 是一款分布式版本控制系统，广泛用于代码管理和协作开发。
以下是一些常用的 Git 命令，帮助您高效地管理代码库。

## 一、新建代码库

- **初始化当前目录为 Git 仓库：**

  
```bash
  git init
  ```


- **克隆远程仓库到本地：**

  
```bash
  git clone <repository-url>
  git clone https://github.com/karlzz-bit/Programming-Basics.git
  git clone git@github.com:karlzz-bit/Programming-Basics.git
  
  ```


## 二、配置

- **显示当前的 Git 配置：**

  
```bash
  git config --list
  ```


- **设置用户信息：**

  
```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  git config --global user.name "karlzz-bit"
  git config --global user.email "194922620+karlzz-bit@users.noreply.github.com"

  ```


## 三、增加/删除文件

- **添加文件到暂存区：**

  
```bash
  git add <file1> <file2> ...
  git add .
  ```


- **删除文件并将删除操作添加到暂存区：**

  
```bash
  git rm <file1> <file2> ...
  git rm
  ```


- **停止追踪文件，但保留工作区中的文件：**

  
```bash
  git rm --cached <file>
  git rm --cached
  ```


## 四、代码提交

- **提交暂存区的更改：**

  
```bash
  git commit -m "Commit message"
  ```


- **修改上一次提交的提交信息：**

  
```bash
  git commit --amend -m "New commit message"
  ```


## 五、分支管理

- **列出所有本地分支：**

  
```bash
  git branch
  ```


- **创建新分支并切换到该分支：**

  
```bash
  git checkout -b <branch-name>
  ```


- **切换到指定分支：**

  
```bash
  git checkout <branch-name>
  ```


- **合并指定分支到当前分支：**

  
```bash
  git merge <branch-name>
  ```


- **删除本地分支：**

  
```bash
  git branch -d <branch-name>
  ```


## 六、查看信息

- **查看当前工作区和暂存区的状态：**

  
```bash
  git status
  ```


- **查看提交历史：**

  
```bash
  git log
  ```


- **查看文件的提交历史：**

  
```bash
  git log --follow <file>
  ```


## 七、远程操作

- **查看远程仓库信息：**

  
```bash
  git remote -v
  ```


- **从远程仓库获取最新更改并合并：**

  
```bash
  git pull <remote> <branch>
  ```


- **将本地分支推送到远程仓库：**

  
```bash
  git push <remote> <branch>
  ```


- **删除远程分支：**

  
```bash
  git push <remote> --delete <branch-name>
  ```


## 八、撤销操作

- **撤销工作区的文件修改：**

  
```bash
  git checkout -- <file>
  ```


- **撤销暂存区的文件修改：**

  
```bash
  git reset <file>
  ```


- **重置当前分支到指定提交：**

  
```bash
  git reset --hard <commit-hash>
  ```


- **撤销上一次提交，但保留工作区的更改：**

  
```bash
  git reset --soft HEAD^
  ```


- **撤销上一次提交，并丢弃工作区的更改：**

  
```bash
  git reset --hard HEAD^
  ```


这些命令涵盖了 Git 的基本操作，帮助您高效地管理代码版本。
对于更详细的命令列表和使用说明，您可以参考以下资源：

- [常用 Git 命令清单](https://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html)
- [Git 命令参考](https://git-scm.com/doc)

这些资源提供了 Git 命令的详细解释和示例，帮助您深入了解和掌握 Git 的使用。 