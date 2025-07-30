---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Vector5
- 来源：[Vector5 - HDLBits](https://hdlbits.01xz.net/wiki/Vector5)

### Problem Statement
Given five 1-bit signals (a, b, c, d, and e), compute all 25 pairwise one-bit comparisons in the 25-bit output vector. The output should be 1 if the two bits being compared are equal.
```Verilog
out[24] = ~a ^ a;   // a == a, so out[24] is always 1.
out[23] = ~a ^ b;
out[22] = ~a ^ c;
...
out[ 1] = ~e ^ d;
out[ 0] = ~e ^ e;
```

[![](https://hdlbits.01xz.net/mw/images/a/ac/Vector5.png)](https://hdlbits.01xz.net/wiki/File:Vector5.png)

As the diagram shows, this can be done more easily using the [replication](https://hdlbits.01xz.net/wiki/Vector4 "Vector4") and concatenation operators.

- The top vector is a concatenation of 5 repeats of each input
- The bottom vector is 5 repeats of a concatenation of the 5 inputs

### Official Solution

```Verilog
module top_module (
	input a, b, c, d, e,
	output [24:0] out
);

	wire [24:0] top, bottom;
	assign top    = { {5{a}}, {5{b}}, {5{c}}, {5{d}}, {5{e}} };
	assign bottom = {5{a,b,c,d,e}};
	assign out = ~top ^ bottom;	// Bitwise XNOR

	// This could be done on one line:
	// assign out = ~{ {5{a}}, {5{b}}, {5{c}}, {5{d}}, {5{e}} } ^ {5{a,b,c,d,e}};
	
endmodule
```

### Note

- 这道题目没有做出来。