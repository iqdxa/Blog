---
authors:
  - TFC
tags:
  - IDE
  - Vivado
  - Verilog
time: 2025-08-01
---

# Vivado常见报错及解决办法

### 参考资料：
- DeepSeek
- [Verilog 常见 Error - 知乎](https://zhuanlan.zhihu.com/p/640496707)
- [vivado2020在编译过程中报错总结_[common 17-69] command failed: placer could not pl-CSDN博客](https://blog.csdn.net/wkonghua/article/details/112585742)
- [vivado综合出现ambiguous clock in event control](https://zhuanlan.zhihu.com/p/340107497)

有时候Vivado提示的地方不是发生错误的地方，所以需要查看提示信息，根据提示信息进行修改，这里列举一些常见的错误以便以后查阅。

## Synthesis阶段
### [Synth 8-91] ambiguous clock in event control
#### 原因
- always敏感变量没有得到使用
#### 解决
- 删除或使用对应的敏感变量。

## Implementation阶段
### [Place 30-494] The design is empty Resolution
- [Place 30-494] The design is empty Resolution: Check if opt_design has removed all the leaf cells of your design. Check whether you have instantiated and connected all of the top level ports.
#### 错误原因
- 缺少输出端口：如果设计中没有任何输出端口，Vivado的综合工具可能会优化掉所有逻辑，导致设计为空。
- 未实例化或连接顶层端口：如果顶层端口没有正确实例化或连接，设计也会被认为是空的。
#### 解决办法
- 添加输出信号：在设计中添加至少一个输出信号，确保综合工具不会优化掉所有逻辑。 
- 使用DONT_TOUCH属性：在需要保留的信号上添加`(* DONT_TOUCH = "TRUE" *)`属性，以防止综合工具优化掉这些信号。