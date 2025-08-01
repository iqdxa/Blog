---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-01
---

# Mux256to1
- 来源：[Mux256to1 - HDLBits](https://hdlbits.01xz.net/wiki/Mux256to1)

### Problem Statement
Create a 1-bit wide, 256-to-1 multiplexer. The 256 inputs are all packed into a single 256-bit input vector. sel=0 should select in[0], sel=1 selects bits in[1], sel=2 selects bits in[2], etc.

??? tip
	- With this many options, a case statement isn't so useful.
	- Vector indices can be variable, as long as the synthesizer can figure out that the width of the bits being selected is constant. In particular, selecting one bit out of a vector using a variable index will work.

### Official Solution

```Verilog
module top_module (
	input [255:0] in,
	input [7:0] sel,
	output  out
);

	// Select one bit from vector in[]. The bit being selected can be variable.
	assign out = in[sel];
	
endmodule
```

### My Solution

```Verilog
module top_module( 
    input [255:0] in,
    input [7:0] sel,
    output out );
    
    assign out = in[sel];

endmodule
```