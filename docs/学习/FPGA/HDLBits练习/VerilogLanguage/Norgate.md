# Norgate
- 来源：[Norgate - HDLBits](https://hdlbits.01xz.net/wiki/Norgate)

### Problem Statement
Create a module that implements a NOR gate. A NOR gate is an OR gate with its output inverted. A NOR function needs two operators when written in Verilog.

An `assign` statement drives a wire (or "net", as it's more formally called) with a value. This value can be as complex a function as you want, as long as it's a _combinational_ (i.e., memory-less, with no hidden state) function. An `assign` statement is a _continuous assignment_ because the output is "recomputed" whenever any of its inputs change, forever, much like a simple logic gate.

### My Solution

```Verilog
module top_module( 
    input a, 
    input b, 
    output out );

    assign out = ~(a|b);

endmodule
```

### 笔记

- 运算符是有优先级的，最开始写成`~a|b`，就不能得到的正确的结果，因为这种写法会先运算`~a`，再运算`(~a)|b`

- 不同操作符的优先级是不同的。当没有圆括号时，Verilog会根据操作符优先级对表达式进行计算

- 在不确定优先级时，建议用圆括号将表达式区分开来

| 操作符    | 操作符号               | 优先级 |
| ------ | ------------------ | --- |
| 单目运算   | + - ! ~            | 最高  |
| 乘、除、取模 | * / %              |     |
| 加减     | + -                |     |
| 移位     | <<  >>             |     |
| 关系     | <  <=  >  >=       |     |
| 等价     | ==  !=  \===  !=== |     |
| 归约     | & ~&               |     |
|        | ^ ~^               |     |
|        | \| ~\|             |     |
| 逻辑     | &&                 |     |
|        | \|                 |     |
| 条件     | ?:                 | 最低  |


