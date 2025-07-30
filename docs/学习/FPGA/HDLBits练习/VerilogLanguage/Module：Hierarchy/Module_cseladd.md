---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-07-30
---

# Module cseladd
- 来源：[Module cseladd - HDLBits](https://hdlbits.01xz.net/wiki/Module_cseladd)

### Problem Statement
One drawback of the ripple carry adder (See [previous exercise](https://hdlbits.01xz.net/wiki/module_add "module_add")) is that the delay for an adder to compute the carry out (from the carry-in, in the worst case) is fairly slow, and the second-stage adder cannot begin computing _its_ carry-out until the first-stage adder has finished. This makes the adder slow. One improvement is a carry-select adder, shown below. The first-stage adder is the same as before, but we duplicate the second-stage adder, one assuming carry-in=0 and one assuming carry-in=1, then using a fast 2-to-1 multiplexer to select which result happened to be correct.

In this exercise, you are provided with the same module `add16` as the previous exercise, which adds two 16-bit numbers with carry-in and produces a carry-out and 16-bit sum. You must instantiate _three_ of these to build the carry-select adder, using your own 16-bit 2-to-1 multiplexer.

Connect the modules together as shown in the diagram below. The provided module `add16` has the following declaration:

`module add16 ( input[15:0] **a**, input[15:0] **b**, input **cin**, output[15:0] **sum**, output **cout** );`

  

[![](https://hdlbits.01xz.net/mw/images/3/3e/Module_cseladd.png)](https://hdlbits.01xz.net/wiki/File:Module_cseladd.png)

### My Solution

```Verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);
    reg [15:0] sum1;
    reg [15:0] sum2;
    reg [15:0] sum3;
    wire cout1;
    
    add16 u_add16_1 (
        .a(a[15:0]),
        .b(b[15:0]),
        .cin(0),
        .sum(sum1),
        .cout(cout1)
  	);
    
    add16 u_add16_2 (
        .a(a[31:16]),
        .b(b[31:16]),
        .cin(0),
        .sum(sum2),
        .cout()
  	);
    
    add16 u_add16_3 (
        .a(a[31:16]),
        .b(b[31:16]),
        .cin(1),
        .sum(sum3),
        .cout()
  	);
    
    assign sum = {cout1 ? sum3 : sum2, sum1};

endmodule
```