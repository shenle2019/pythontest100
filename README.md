#Demo

git 使用步骤:

1.Debian 系列：apt-get install git
Fedora 上：yum install git-core

2.新建仓库

3.mkdir pythontest100
cd pythontest100
gedit README.md

4.你只需在 pythontest100 目录中，输入 git init 即可。

5.创建或修改 本地文件
使用 git add 命令，将创建或修改的文件添加到本地的 暂存区，这里保存的是你的临时更改 git status查看
使用 git commit 命令，提交文件到 本地仓库
使用 git push 命令，将本地代码库同步到 远端仓库

6.git config --global user.name "shenle"
git config --global user.email "305030951@qq.com"

7.git commit -m "first commit"

8.git remote add origin 仓库链接
https://github.com/shenle2019/pythontest100.git
git remote add origin https://github.com/shenle2019/pythontest100.git

9.git push origin master

10.克隆项目
cd /home/ubuntu/
git clone https://github.com/shenle2019/pythontest100.git
