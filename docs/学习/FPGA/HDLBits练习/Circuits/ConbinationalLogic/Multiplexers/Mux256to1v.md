---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-01
---

# Mux256to1v
- 来源：[Mux256to1v - HDLBits](https://hdlbits.01xz.net/wiki/Mux256to1v)

### Problem Statement
Create a 4-bit wide, 256-to-1 multiplexer. The 256 4-bit inputs are all packed into a single 1024-bit input vector. sel=0 should select bits in[3:0], sel=1 selects bits in[7:4], sel=2 selects bits in[11:8], etc.

??? tip
	- With this many options, a case statement isn't so useful.
	- Vector indices can be variable, as long as the synthesizer can figure out that the width of the bits being selected is constant. It's not always good at this. An error saying "... is not a constant" means it couldn't prove that the select width is constant. In particular, in[ sel*4+3 : sel*4 ] does not work.
	- Bit slicing ("Indexed vector part select", since Verilog-2001) has an even more compact syntax.
### Official Solution

```Verilog
module top_module (
	input [1023:0] in,
	input [7:0] sel,
	output [3:0] out
);

	// We can't part-select multiple bits without an error, but we can select one bit at a time,
	// four times, then concatenate them together.
	assign out = {in[sel*4+3], in[sel*4+2], in[sel*4+1], in[sel*4+0]};

	// Alternatively, "indexed vector part select" works better, but has an unfamiliar syntax:
	// assign out = in[sel*4 +: 4];		// Select starting at index "sel*4", then select a total width of 4 bits with increasing (+:) index number.
	// assign out = in[sel*4+3 -: 4];	// Select starting at index "sel*4+3", then select a total width of 4 bits with decreasing (-:) index number.
	// Note: The width (4 in this case) must be constant.

endmodule
```

### My Solution

```Verilog
module top_module( 
    input [1023:0] in,
    input [7:0] sel,
    output [3:0] out );
    
    assign out = in[sel * 4 +: 4];

endmodule
```

### Note
- `+:`是 Verilog 中的一种位选择操作符，称为"位宽指定选择"(bit-slice selection with a width)。它用于从指定的起始位开始选择固定宽度的位向量。

```verilog
signal[start_index +: width]
```
其中：
- start_index 是起始位的索引（可以是变量或表达式）
- width 是要选择的位宽（必须是常量）
- +: 表示从 start_index 开始向高位方向选择 width 位