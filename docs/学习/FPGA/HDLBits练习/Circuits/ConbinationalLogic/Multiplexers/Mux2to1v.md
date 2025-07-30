---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Mux2to1v
- 来源：[Mux2to1v - HDLBits](https://hdlbits.01xz.net/wiki/Mux2to1v)

### Problem Statement
Create a 100-bit wide, 2-to-1 multiplexer. When sel=0, choose a. When sel=1, choose b.

??? tip
	The ternary operator (cond ? iftrue : iffalse) is easier to read.

### Official Solution

```Verilog
module top_module (
	input [99:0] a,
	input [99:0] b,
	input sel,
	output [99:0] out
);

	assign out = sel ? b : a;
	
	// The following doesn't work. Why?
	// assign out = (sel & b) | (~sel & a);
	
endmodule
```

### My Solution

```Verilog
module top_module( 
    input [99:0] a, b,
    input sel,
    output [99:0] out );

    assign out = sel ? b : a;
    
endmodule
```