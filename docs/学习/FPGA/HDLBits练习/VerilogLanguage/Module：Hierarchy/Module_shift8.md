---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-03
---
# Module shift8
- 来源：[Module shift8 - HDLBits](https://hdlbits.01xz.net/wiki/Module_shift8)

### Problem Statement
This exercise is an extension of module_shift. Instead of module ports being only single pins, we now have modules with vectors as ports, to which you will attach wire vectors instead of plain wires. Like everywhere else in Verilog, the vector length of the port does not have to match the wire connecting to it, but this will cause zero-padding or trucation of the vector. This exercise does not use connections with mismatched vector lengths.

You are given a module `my_dff8` with two inputs and one output (that implements a set of 8 D flip-flops). Instantiate three of them, then chain them together to make a 8-bit wide shift register of length 3. In addition, create a 4-to-1 multiplexer (not provided) that chooses what to output depending on `sel[1:0]`: The value at the input d, after the first, after the second, or after the third D flip-flop. (Essentially, `sel` selects how many cycles to delay the input, from zero to three clock cycles.)

The module provided to you is: `module my_dff8 ( input clk, input [7:0] d, output [7:0] q );`

The multiplexer is not provided. One possible way to write one is inside an `always` block with a `case` statement inside. (See also: mux9to1v)

[![](https://hdlbits.01xz.net/mw/images/7/76/Module_shift8.png)](https://hdlbits.01xz.net/wiki/File:Module_shift8.png)

### Official Solution

```Verilog
module top_module (
	input clk,
	input [7:0] d,
	input [1:0] sel,
	output reg [7:0] q
);

	wire [7:0] o1, o2, o3;		// output of each my_dff8
	
	// Instantiate three my_dff8s
	my_dff8 d1 ( clk, d, o1 );
	my_dff8 d2 ( clk, o1, o2 );
	my_dff8 d3 ( clk, o2, o3 );

	// This is one way to make a 4-to-1 multiplexer
	always @(*)		// Combinational always block
		case(sel)
			2'h0: q = d;
			2'h1: q = o1;
			2'h2: q = o2;
			2'h3: q = o3;
		endcase

endmodule
```

### My Solution

```Verilog
module top_module ( 
    input clk, 
    input [7:0] d, 
    input [1:0] sel, 
    output [7:0] q 
);
    wire [7:0] q1;
    wire [7:0] q2;
    wire [7:0] q3;
    
    my_dff8 u_my_dff8_1 (
        .clk(clk),
        .d(d),
        .q(q1)
    );
    
    my_dff8 u_my_dff8_2 (
        .clk(clk),
        .d(q1),
        .q(q2)
    );
    
    my_dff8 u_my_dff8_3 (
        .clk(clk),
        .d(q2),
        .q(q3)
    );
    
    always@(*)begin
        case(sel)
            2'b00:q = d;
            2'b01:q = q1;
            2'b10:q = q2;
            2'b11:q = q3;
        endcase
    end

endmodule
```

### Note

- 这道题会用到后面的知识，可以先跳过，等完成后面的练习再做。

- 使用always语句，在always语句里面使用case语句，对应每一种`sel`的可能对应一种`q`的值。