---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Vector2
- 来源：[Vector2 - HDLBits](https://hdlbits.01xz.net/wiki/Vector2)

### Problem Statement
A 32-bit vector can be viewed as containing 4 bytes (bits [31:24], [23:16], etc.). Build a circuit that will reverse the _byte_ ordering of the 4-byte word.

AaaaaaaaBbbbbbbbCcccccccDddddddd => DdddddddCcccccccBbbbbbbbAaaaaaaa

This operation is often used when the [endianness](https://en.wikipedia.org/wiki/Endianness) of a piece of data needs to be swapped, for example between little-endian x86 systems and the big-endian formats used in many Internet protocols.

??? tip
	Part-select can be used on both the left side and right side of an assignment.

### Official Solution

```Verilog
module top_module (
	input [31:0] in,
	output [31:0] out
);

	assign out[31:24] = in[ 7: 0];	
	assign out[23:16] = in[15: 8];	
	assign out[15: 8] = in[23:16];	
	assign out[ 7: 0] = in[31:24];	
	
endmodule
```

### My Solution

```Verilog
module top_module( 
    input [31:0] in,
    output [31:0] out );//

    // assign out[31:24] = ...;
    assign out = {in[7:0],in[15:8],in[23:16],in[31:24]};
endmodule
```

### Note

- 这道题使用拼接符`{}`就很方便。