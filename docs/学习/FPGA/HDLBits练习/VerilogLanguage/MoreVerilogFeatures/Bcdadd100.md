---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-03
---

# Bcdadd100
- 来源：[Bcdadd100 - HDLBits](https://hdlbits.01xz.net/wiki/Bcdadd100)

### Problem Statement
You are provided with a BCD one-digit adder named bcd_fadd that adds two BCD digits and carry-in, and produces a sum and carry-out.
```Verilog
module bcd_fadd (
    input [3:0] a,
    input [3:0] b,
    input     cin,
    output   cout,
    output [3:0] sum );
```

Instantiate 100 copies of bcd_fadd to create a 100-digit BCD ripple-carry adder. Your adder should add two 100-digit BCD numbers (packed into 400-bit vectors) and a carry-in to produce a 100-digit sum and carry out.

??? tip
	An instance array or generate statement would be useful here.

### Official Solution

```Verilog

```

### My Solution

```Verilog
module top_module( 
    input [399:0] a, b,
    input cin,
    output cout,
    output [399:0] sum 
);
	
    reg [99:0] out;
    genvar i;
    generate for(i = 0; i < 100; i++) begin:inst
        bcd_fadd u_bcd_fadd (
            .a(a[(4*i)+:4]),
            .b(b[4*i+:4]),
            .cin((i == 0) ? cin : out[i-1]),
            .cout(out[i]),
            .sum(sum[4*i+:4])
        );
    end
    assign cout = out[99];
    endgenerate
    
endmodule
```

### Note
- 最开始的代码如下：
```Verilog
reg [99:0] out;
genvar i;
generate for(i = 0; i < 100; i++) begin:inst
    bcd_fadd u_bcd_fadd (
        .a(a[(4*i)+：4]),
        .b(b[4*i+：4]),
        .cin((i == 0) ? cin : out[i-1]),
        .cout(out[i]),
        .sum(sum[4*i+：4])
    );
end
assign cout = out[99];
endgenerate
```
- 报错：`Error (10170): Verilog HDL syntax error at top_module.v(12) near text: �. Check for and fix any syntax errors that appear immediately before or at the specified keyword. `
- 问了DeepSeek，才发现是使用的中文`：`，而不是英文`:`，这个也太难发现了。