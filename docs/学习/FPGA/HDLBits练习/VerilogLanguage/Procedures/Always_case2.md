---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-07-31
---

# Always case2
- 来源：[Always case2 - HDLBits](https://hdlbits.01xz.net/wiki/Always_case2)

### Problem Statement
A _priority encoder_ is a combinational circuit that, when given an input bit vector, outputs the position of the first 1 bit in the vector. For example, a 8-bit priority encoder given the input 8'b10010000 would output 3'd4, because bit[4] is first bit that is high.

Build a 4-bit priority encoder. For this problem, if none of the input bits are high (i.e., input is zero), output zero. Note that a 4-bit number has 16 possible combinations.

??? tip
	Using hexadecimal (4'hb) or decimal (4'd11) number literals would save typing vs. binary (4'b1011) literals.

### Official Solution

```Verilog
module top_module (
	input [3:0] in,
	output reg [1:0] pos
);

	always @(*) begin			// Combinational always block
		case (in)
			4'h0: pos = 2'h0;	// I like hexadecimal because it saves typing.
			4'h1: pos = 2'h0;
			4'h2: pos = 2'h1;
			4'h3: pos = 2'h0;
			4'h4: pos = 2'h2;
			4'h5: pos = 2'h0;
			4'h6: pos = 2'h1;
			4'h7: pos = 2'h0;
			4'h8: pos = 2'h3;
			4'h9: pos = 2'h0;
			4'ha: pos = 2'h1;
			4'hb: pos = 2'h0;
			4'hc: pos = 2'h2;
			4'hd: pos = 2'h0;
			4'he: pos = 2'h1;
			4'hf: pos = 2'h0;
			default: pos = 2'b0;	// Default case is not strictly necessary because all 16 combinations are covered.
		endcase
	end
	
	// There is an easier way to code this. See the next problem (always_casez).
	
endmodule
```

### My Solution

```Verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input [3:0] in,
    output reg [1:0] pos  );

    always@(*)begin
        case(in)
            4'h0: pos <= 2'd0;
            4'h1: pos <= 2'd0;
            4'h2: pos <= 2'd1;
            4'h3: pos <= 2'd0;
            4'h4: pos <= 2'd2;
            4'h5: pos <= 2'd0;
            4'h6: pos <= 2'd1;
            4'h7: pos <= 2'd0;
            4'h8: pos <= 2'd3;
            4'h9: pos <= 2'd0;
            4'ha: pos <= 2'd1;
            4'hb: pos <= 2'd0;
            4'hc: pos <= 2'd2;
            4'hd: pos <= 2'd0;
            4'he: pos <= 2'd1;
            4'hf: pos <= 2'd0;
        endcase
    end
endmodule
```

### Note
- 虽然使用十六进制减少了打字的数量，但是在判断第一个出现的高电平的位置时不容易进行判断。