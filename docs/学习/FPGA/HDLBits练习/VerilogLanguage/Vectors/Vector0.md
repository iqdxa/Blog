---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Vector0
- 来源：[Vector0 - HDLBits](https://hdlbits.01xz.net/wiki/Vector0)

### Problem Statement

Vectors are used to group related signals using one name to make it more convenient to manipulate. For example, wire [7:0] w; declares an 8-bit vector named w that is functionally equivalent to having 8 separate wires.

Notice that the _declaration_ of a vector places the dimensions _before_ the name of the vector, which is unusual compared to C syntax. However, the _part select_ has the dimensions _after_ the vector name as you would expect.

```Verilog
wire [99:0] my_vector; // Declare a 100-element vector 
assign out = my_vector[10]; // Part-select one bit out of the vector
```

Build a circuit that has one 3-bit input, then outputs the same vector, and also splits it into three separate 1-bit outputs. Connect output `o0` to the input vector's position 0, `o1` to position 1, etc.

In a diagram, a tick mark with a number next to it indicates the width of the vector (or "bus"), rather than drawing a separate line for each bit in the vector.

[![](https://hdlbits.01xz.net/mw/images/a/ae/Vector0.png)](https://hdlbits.01xz.net/wiki/File:Vector0.png)


### Official Solution

```Verilog
module top_module(
	input [2:0] vec, 
	output [2:0] outv,
	output o2,
	output o1,
	output o0
);
	
	assign outv = vec;

	// This is ok too: assign {o2, o1, o0} = vec;
	assign o0 = vec[0];
	assign o1 = vec[1];
	assign o2 = vec[2];
	
endmodule

```

### My Solution

```Verilog
module top_module ( 
    input wire [2:0] vec,
    output wire [2:0] outv,
    output wire o2,
    output wire o1,
    output wire o0  ); // Module body starts after module declaration

    assign outv = vec;
    assign o2 = vec[2];
    assign o1 = vec[1];
    assign o0 = vec[0];
    
endmodule
```