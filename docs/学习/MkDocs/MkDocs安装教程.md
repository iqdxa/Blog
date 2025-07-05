
### 安装 MkDocs
- 使用以下命令进行安装MkDocs
```shell
pip install mkdocs
```
- 安装`material`主题
```shell
pip install mkdocs-material
```
- 安装完成后验证是否安装成功
```shell
mkdocs --version
```
### 创建 MkDocs 项目
```shell
mkdocs new <项目名称>
```
### 启动本地服务器
```shell
mkdocs serve
```
- 在浏览器打开 `http://127.0.0.1:8000`进行预览。
### 生成静态文件
```shell
mkdocs build
```
### 使用GitHub Actions
- 在根目录下创建文件`.github/workflows/ci.yml`，并加入下列代码
```yml
name: ci
on:
  push:
    branches:
      - master
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```
### 部署到Github
```shell
mkdocs gh-deploy
```

### 参考文档
- [Material for MkDocs - Material for MkDocs 中文文档](https://mkdoc-material.llango.com/)
- [最牛逼的Python文档生成工具——MkDocs，手把手教你搭建文档网站 | 极客之音](https://www.bmabk.com/index.php/post/311224.html)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)