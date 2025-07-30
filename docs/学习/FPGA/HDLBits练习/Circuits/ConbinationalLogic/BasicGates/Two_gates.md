---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Exams/m2014 q4g
- 来源：[Exams/m2014 q4g - HDLBits](https://hdlbits.01xz.net/wiki/Exams/m2014_q4g)

### Problem Statement
Implement the following circuit:

[![](https://hdlbits.01xz.net/mw/images/e/e6/Exams_m2014q4g.png)](https://hdlbits.01xz.net/wiki/File:Exams_m2014q4g.png)

### My Solution

```Verilog
module top_module (
    input in1,
    input in2,
    input in3,
    output out);

    assign out = in3 ^ (~(in1 ^ in2));
    
endmodule
```

### Note
- 图中左边是同或门，右边是异或门
- 异或门使用`^`运算符