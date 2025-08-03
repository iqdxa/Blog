---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-03
---

# Adder100i
- 来源：[Adder100i - HDLBits](https://hdlbits.01xz.net/wiki/Adder100i)

### Problem Statement
Create a 100-bit binary ripple-carry adder by instantiating 100 [full adders](https://hdlbits.01xz.net/wiki/Fadd "Fadd"). The adder adds two 100-bit numbers and a carry-in to produce a 100-bit sum and carry out. To encourage you to actually instantiate full adders, also output the carry-out from _each_ full adder in the ripple-carry adder. cout[99] is the final carry-out from the last full adder, and is the carry-out you usually see.

??? tip
	There are many full adders to instantiate. An instance array or generate statement would help here.

### My Solution

```Verilog
module top_module( 
    input [99:0] a, b,
    input cin,
    output [99:0] cout,
    output [99:0] sum );
	
    always@(*)begin
        for(int i = 0; i < 100; i++)begin
            {cout[i], sum[i]} = a[i] + b[i] + ((i == 0) ? cin : cout[i-1]);
        end
    end
endmodule
```

### Note
- 最开始写的代码如下：
```Verilog
always@(*)begin
    for(int i = 0; i < 100; i++)begin
        {cout[i],sum[i]} = a[i] + b[i] + i?cout[i-1]:cin;
    end
end
```
- 报错：`index -1 cannot fall outside the declared range [99:0] for vector "cout"`
- 问了DeepSeek，给出了以下说明：
  - 主要问题：当 i=0 时，代码尝试访问 cout[i-1] 即 cout[-1]，这超出了向量 cout 的声明范围 [99:0]。
  - 逻辑错误：在三元运算符的条件部分使用了 i?cout[i-1]:cin，这意味着：
    - 当 i≠0 时使用 cout[i-1]
    - 当 i=0 时使用 cin
    - 但条件判断应该是 (i != 0) 而不是 i，因为 i=0 时 i 的值是 0（false）。
  - 运算符优先级问题：加法运算符 (+) 的优先级高于三元条件运算符 (? :)，所以表达式会被错误地分组。
- 所以这个代码有好几处错误。