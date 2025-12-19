# 将项目提交到GitHub指南

## 📋 前提条件

1. 已安装 Git
2. 已注册 GitHub 账号
3. 已配置 Git 用户信息（如果还没有）

```bash
# 配置Git用户信息（如果还没有配置）
git config --global user.name "dongxg"
git config --global user.email "964996448@qq.com"
```

## 🚀 步骤详解

### 步骤1：在GitHub上创建新仓库

1. 登录 GitHub
2. 点击右上角的 **"+"** 按钮，选择 **"New repository"**
3. 填写仓库信息：
   - **Repository name**: `pylearn`（或你喜欢的名字）
   - **Description**: Python学习计划demo代码库
   - **Visibility**: 选择 Public（公开）或 Private（私有）
   - **不要**勾选 "Initialize this repository with a README"（因为本地已有代码）
4. 点击 **"Create repository"**

### 步骤2：连接本地仓库到GitHub

创建仓库后，GitHub会显示设置说明。使用以下命令：

```bash
# 进入项目目录
cd /Users/sunny/SourceCode/pylearn

# 添加远程仓库（将 YOUR_USERNAME 替换为你的GitHub用户名）
git remote add origin https://github.com/xiaoguangdong/pylearn.git

# 或者使用SSH（如果你配置了SSH密钥）
# git remote add origin git@github.com:YOUR_USERNAME/pylearn.git

# 查看远程仓库配置
git remote -v
```

### 步骤3：推送代码到GitHub

```bash
# 推送代码到GitHub（首次推送）
git push -u origin main

# 如果遇到错误，可能需要先拉取（通常不需要，因为仓库是空的）
# git pull origin main --allow-unrelated-histories
```

### 步骤4：验证推送结果

1. 刷新GitHub仓库页面
2. 你应该能看到所有文件已经上传成功

## 📝 后续更新代码

当你修改代码后，使用以下命令更新GitHub：

```bash
# 1. 查看修改的文件
git status

# 2. 添加修改的文件到暂存区
git add .

# 或者只添加特定文件
# git add stage1_basics/01_environment_and_syntax.py

# 3. 提交更改
git commit -m "描述你的修改内容"

# 4. 推送到GitHub
git push
```

## 🔧 常见问题解决

### 问题1：推送时要求输入用户名和密码

**解决方案：使用Personal Access Token**

1. GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 生成新token，勾选 `repo` 权限
3. 推送时使用token作为密码

**或者使用SSH密钥（推荐）：**

```bash
# 生成SSH密钥（如果还没有）
ssh-keygen -t ed25519 -C "your.email@example.com"

# 复制公钥
cat ~/.ssh/id_ed25519.pub

# 添加到GitHub: Settings → SSH and GPG keys → New SSH key
```

### 问题2：分支名称不匹配

如果GitHub默认分支是 `master` 而本地是 `main`：

```bash
# 方法1：重命名本地分支
git branch -M master
git push -u origin master

# 方法2：推送main分支并设置GitHub默认分支为main
git push -u origin main
# 然后在GitHub设置中将默认分支改为main
```

### 问题3：.gitignore不生效

如果已经提交了应该忽略的文件：

```bash
# 从Git中移除但保留本地文件
git rm --cached -r .idea/
git commit -m "移除IDE配置文件"
git push
```

## 📚 Git常用命令速查

```bash
# 查看状态
git status

# 查看提交历史
git log --oneline

# 查看差异
git diff

# 撤销暂存区的文件
git restore --staged <file>

# 撤销工作区的修改
git restore <file>

# 创建新分支
git checkout -b feature-branch

# 切换分支
git checkout main

# 合并分支
git merge feature-branch

# 查看远程仓库
git remote -v

# 拉取最新代码
git pull
```

## ✅ 检查清单

- [ ] Git已安装并配置
- [ ] GitHub账号已注册
- [ ] 本地代码已提交（git commit）
- [ ] GitHub上已创建仓库
- [ ] 已添加远程仓库（git remote add）
- [ ] 代码已成功推送（git push）
- [ ] GitHub上可以查看所有文件

## 🎉 完成！

推送成功后，你的项目就可以在GitHub上访问了。其他人可以通过以下方式克隆你的项目：

```bash
git clone https://github.com/YOUR_USERNAME/pylearn.git
```

