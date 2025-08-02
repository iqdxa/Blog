---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-01
---

# Vector100r
- 来源：[Vector100r - HDLBits](https://hdlbits.01xz.net/wiki/Vector100r)

### Problem Statement
Given a 100-bit input vector [99:0], reverse its bit ordering.

??? tip
	A for loop (in a combinational always block or generate block) would be useful here. I would prefer a combinational always block in this case because module instantiations (which require generate blocks) aren't needed.

### Official Solution

```Verilog
module top_module (
	input [99:0] in,
	output reg [99:0] out
);
	
	always @(*) begin
		for (int i=0;i<$bits(out);i++)		// $bits() is a system function that returns the width of a signal.
			out[i] = in[$bits(out)-i-1];	// $bits(out) is 100 because out is 100 bits wide.
	end
	
endmodule
```

### My Solution

```Verilog
module top_module( 
    input [99:0] in,
    output [99:0] out
);
    genvar i;
    generate
        for (i = 0; i < 100; i = i + 1) begin : reverse
            assign out[i] = in[99-i];
        end
    endgenerate

endmodule
```