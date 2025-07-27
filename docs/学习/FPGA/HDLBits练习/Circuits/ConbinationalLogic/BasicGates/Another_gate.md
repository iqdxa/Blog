# Exams/m2014 q4f
- 来源：[Exams/m2014 q4f - HDLBits](https://hdlbits.01xz.net/wiki/Exams/m2014_q4f)

### Problem Statement
Implement the following circuit:

[![](https://hdlbits.01xz.net/mw/images/b/b6/Exams_m2014q4f.png)](https://hdlbits.01xz.net/wiki/File:Exams_m2014q4f.png)

### My Solution

```Verilog
module top_module (
    input in1,
    input in2,
    output out);

    assign out = in1 & (~in2);

endmodule
```