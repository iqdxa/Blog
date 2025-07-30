---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Xnorgate
- 来源：[Xnorgate - HDLBits](https://hdlbits.01xz.net/wiki/Xnorgate)

### Problem Statement
Create a module that implements an XNOR gate.

??? tip
    The bitwise-XOR operator is ^. There is no logical-XOR operator.

### My Solution

```Verilog
module top_module( 
    input a, 
    input b, 
    output out );
	
    assign out = ~(a^b);
    
endmodule
```

### Note

- XOR是异或门，输出在输入不同时为1，在输入相同时为0

- XNOR是同或门，输出在输入相同时为1，在输入不同时为0

- Verilog没有XNOR运算符，所以同或运算是在异或运算符`^`的基础上取反