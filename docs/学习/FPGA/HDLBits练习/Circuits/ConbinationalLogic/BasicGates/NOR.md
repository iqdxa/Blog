# Exams/m2014 q4e
- 来源：[Exams/m2014 q4e - HDLBits](https://hdlbits.01xz.net/wiki/Exams/m2014_q4e)

### Problem Statement
Implement the following circuit:

[![](https://hdlbits.01xz.net/mw/images/e/e9/Exams_m2014q4e.png)](https://hdlbits.01xz.net/wiki/File:Exams_m2014q4e.png)

### My Solution

```Verilog
module top_module (
    input in1,
    input in2,
    output out);

    assign out = ~(in1|in2);
    
endmodule
```

### Note
- 注意运算顺序。