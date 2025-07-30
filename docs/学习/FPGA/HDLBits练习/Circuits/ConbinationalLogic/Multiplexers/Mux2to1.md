---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Mux2to1
- 来源：[Mux2to1 - HDLBits](https://hdlbits.01xz.net/wiki/Mux2to1)

### Problem Statement
Create a one-bit wide, 2-to-1 multiplexer. When sel=0, choose a. When sel=1, choose b.

??? tip
	The ternary operator (cond ? iftrue : iffalse) is easier to read.
### Official Solution

```Verilog
module top_module (
	input a,
	input b,
	input sel,
	output out
);

	assign out = (sel & b) | (~sel & a);	// Mux expressed as AND and OR
	
	// Ternary operator is easier to read, especially if vectors are used:
	// assign out = sel ? b : a;
	
endmodule
```

### My Solution

```Verilog
module top_module( 
    input a, b, sel,
    output out ); 
	
    assign out = sel ? b : a;
    
endmodule
```