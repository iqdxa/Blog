---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Vectorr
- 来源：[Vectorr - HDLBits](https://hdlbits.01xz.net/wiki/Vectorr)

### Problem Statement
Given an 8-bit input vector [7:0], reverse its bit ordering.

??? tip
	assign out[7:0] = in[0:7]; does not work because Verilog does not allow vector bit ordering to be flipped.
	The concatenation operator may save a bit of coding, allowing for 1 assign statement instead of 8.

### Official Solution

```Verilog
module top_module (
	input [7:0] in,
	output [7:0] out
);
	
	assign {out[0],out[1],out[2],out[3],out[4],out[5],out[6],out[7]} = in;
	
	/*
	// I know you're dying to know how to use a loop to do this:

	// Create a combinational always block. This creates combinational logic that computes the same result
	// as sequential code. for-loops describe circuit *behaviour*, not *structure*, so they can only be used 
	// inside procedural blocks (e.g., always block).
	// The circuit created (wires and gates) does NOT do any iteration: It only produces the same result
	// AS IF the iteration occurred. In reality, a logic synthesizer will do the iteration at compile time to
	// figure out what circuit to produce. (In contrast, a Verilog simulator will execute the loop sequentially
	// during simulation.)
	always @(*) begin	
		for (int i=0; i<8; i++)	// int is a SystemVerilog type. Use integer for pure Verilog.
			out[i] = in[8-i-1];
	end


	// It is also possible to do this with a generate-for loop. Generate loops look like procedural for loops,
	// but are quite different in concept, and not easy to understand. Generate loops are used to make instantiations
	// of "things" (Unlike procedural loops, it doesn't describe actions). These "things" are assign statements,
	// module instantiations, net/variable declarations, and procedural blocks (things you can create when NOT inside 
	// a procedure). Generate loops (and genvars) are evaluated entirely at compile time. You can think of generate
	// blocks as a form of preprocessing to generate more code, which is then run though the logic synthesizer.
	// In the example below, the generate-for loop first creates 8 assign statements at compile time, which is then
	// synthesized.
	// Note that because of its intended usage (generating code at compile time), there are some restrictions
	// on how you use them. Examples: 1. Quartus requires a generate-for loop to have a named begin-end block
	// attached (in this example, named "my_block_name"). 2. Inside the loop body, genvars are read only.
	generate
		genvar i;
		for (i=0; i<8; i = i+1) begin: my_block_name
			assign out[i] = in[8-i-1];
		end
	endgenerate
	*/
	
endmodule
```

### My Solution

```Verilog
module top_module( 
    input [7:0] in,
    output [7:0] out
);
    assign {out[7],out[6],out[5],out[4],out[3],out[2],out[1],out[0]} = {in[0],in[1],in[2],in[3],in[4],in[5],in[6],in[7]};

endmodule
```

### Note

- 看来答案，发现我的代码有点冗余。

- 官方代码的注释里面提到用循环，这是个好办法。