---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-02
---

# Fadd
- 来源：[Fadd - HDLBits](https://hdlbits.01xz.net/wiki/Fadd)

### Problem Statement
Create a full adder. A full adder adds three bits (including carry-in) and produces a sum and carry-out.

### Official Solution

```Verilog

```

### My Solution

```Verilog
module top_module( 
    input a, b, cin,
    output cout, sum );
	
    assign {cout, sum} = a + b + cin;
    
endmodule
```