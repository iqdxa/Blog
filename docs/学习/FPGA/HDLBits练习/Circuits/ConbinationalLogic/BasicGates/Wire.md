---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Exams/m2014 q4h
- 来源：[Exams/m2014 q4h - HDLBits](https://hdlbits.01xz.net/wiki/Exams/m2014_q4h)

### Problem Statement
Implement the following circuit:

[![](https://hdlbits.01xz.net/mw/images/d/d7/Exams_m2014q4h.png)](https://hdlbits.01xz.net/wiki/File:Exams_m2014q4h.png)

### My Solution

```Verilog
module top_module (
    input in,
    output out);
	
    assign out = in;
endmodule
```