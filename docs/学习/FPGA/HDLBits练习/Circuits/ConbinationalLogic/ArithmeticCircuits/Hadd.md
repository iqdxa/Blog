---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-02
---

# Hadd
- 来源：[Hadd - HDLBits](https://hdlbits.01xz.net/wiki/Hadd)

### Problem Statement
Create a half adder. A half adder adds two bits (with no carry-in) and produces a sum and carry-out.

### My Solution

```Verilog
module top_module( 
    input a, b,
    output cout, sum );

    reg [1:0] c;
    assign c = a + b;
    assign sum = c[0];
    assign cout = c[1];
    
endmodule
```

### Note
- 使用拼接语法还可以简化代码：
```Verilog
module top_module( 
    input a, b,
    output cout, sum );

    assign {cout, sum} = a + b;
    
endmodule
```