---
authors:
  - TFC
tags:
  - Android
  - ADB
---
### ADB安装
#### 已安装Android Studio的情况
- 找到Android Studio SDK文件所在位置，SDK--->platform-tools--->找到adb的绝对路径。
- 添加系统环境变量。
#### 未安装Android Studio的情况
- 直接在官网下载ADB组件，官网：[SDK Platform Tools release notes  |  Android Studio  |  Android Developers](https://developer.android.google.cn/tools/releases/platform-tools?hl=en)
- 添加环境变量
### ADB使用
- 查看ADB版本
```
adb --version
```
- 进入交互模式
```
adb shell
```
- 查看连接的设备
```
adb devices
```
- 卸载命令
```
pm uninstall -k --user 0 软件包名
```
- 显示所有应用包名
```
pm list packages
```
### 常见软件卸载命令
- 华为音乐
```shell
pm uninstall -k --user 0 com.android.mediacenter
```
或者
```shell
pm uninstall -k --user 0 com.huawei.music
```
- 华为智慧
```shell
pm uninstall -k --user 0 com.huawei.intelligent
```
- 华为钱包
```shell
pm uninstall -k --user 0 com.huawei.wallet
```
- 百度输入法（华为版）
```shell
pm uninstall -k --user 0 com.baidu.input_huawei
```
- 华为视频
```shell
pm uninstall -k --user 0 com.huawei.himovie
```
- 快应用
```shell
pm uninstall -k --user 0 com.huawei.fastapp
```
- 智慧搜索
```shell
pm uninstall -k --user 0 com.huawei.search
```
- 小艺建议
```shell
pm uninstall -k --user 0 com.huawei.ohos.suggestion
```
- 锁屏杂志
```shell
pm uninstall -k --user 0 com.huawei.magazine
```
- 主题
```shell
pm uninstall --user 0 com.huawei.android.thememanager
```
- 我的华为
```shell
pm uninstall --user 0 com.huawei.phoneservice
```
- 华为浏览器
```bash
pm uninstall --user 0 com.huawei.browser
```
- 联系人
```shell
pm uninstall --user 0 com.huawei.contacts
```
- 华为应用市场
```shell
pm uninstall --user 0 com.huawei.appmarket
```