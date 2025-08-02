---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-02
---

# Popcount255
- 来源：[Popcount255 - HDLBits](https://hdlbits.01xz.net/wiki/Popcount255)

### Problem Statement
A "population count" circuit counts the number of '1's in an input vector. Build a population count circuit for a 255-bit input vector.

??? tip
	So many things to add... How about a for loop?

### Official Solution

```Verilog
module top_module (
	input [254:0] in,
	output reg [7:0] out
);

	always @(*) begin	// Combinational always block
		out = 0;
		for (int i=0;i<255;i++)
			out = out + in[i];
	end
	
endmodule
```

### My Solution

```Verilog
module top_module( 
    input [254:0] in,
    output [7:0] out );

    always @(*) begin
        out = 8'b0;
        for (int i = 0;i < 255; i++)begin
            if(in[i] == 1'b1)
                out = out + 1'b1;
        end
	end
endmodule
```