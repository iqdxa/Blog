---
date:
  created: 2023-12-31
  updated: 2024-01-02
authors:
  - TFC
tags:
    - 教程
    - MkDocs
---

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

### 部署到Github
```shell
mkdocs gh-deploy
```

### 参考文档
- [Material for MkDocs - Material for MkDocs 中文文档](https://mkdoc-material.llango.com/)
- [最牛逼的Python文档生成工具——MkDocs，手把手教你搭建文档网站 | 极客之音](https://www.bmabk.com/index.php/post/311224.html)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)