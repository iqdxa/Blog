---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-07-30
---

# Module addsub
- 来源：[Module addsub - HDLBits](https://hdlbits.01xz.net/wiki/Module_addsub)

### Problem Statement
An adder-subtractor can be built from an adder by optionally negating one of the inputs, which is equivalent to inverting the input then adding 1. The net result is a circuit that can do two operations: (a + b + 0) and (a + ~b + 1). See [Wikipedia](https://en.wikipedia.org/wiki/Adder%E2%80%93subtractor) if you want a more detailed explanation of how this circuit works.

Build the adder-subtractor below.

You are provided with a 16-bit adder module, which you need to instantiate twice:

`module add16 ( input[15:0] **a**, input[15:0] **b**, input **cin**, output[15:0] **sum**, output **cout** );`

Use a 32-bit wide XOR gate to invert the b input whenever sub is 1. (This can also be viewed as b[31:0] XORed with sub replicated 32 times. See [replication operator](https://hdlbits.01xz.net/wiki/vector4 "vector4").). Also connect the sub input to the carry-in of the adder.

  

[![](https://hdlbits.01xz.net/mw/images/a/ae/Module_addsub.png)](https://hdlbits.01xz.net/wiki/File:Module_addsub.png)

??? tip
	An XOR gate can also be viewed as a programmable inverter, where one input controls whether the other should be inverted. The following two circuits are both XOR gates: [![](https://hdlbits.01xz.net/mw/images/7/74/Module_addsub_xor.png)](https://hdlbits.01xz.net/wiki/File:Module_addsub_xor.png)

### My Solution

```Verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    input sub,
    output [31:0] sum
);
    reg [15:0] sum1;
    reg [15:0] sum2;
    wire cout1;
    
    add16 u_add16_a (
        .a(a[15:0]),
        .b({16{sub}} ^ b[15:0]),
        .cin(sub),
        .sum(sum1),
        .cout(cout1)
     );
    
    add16 u_add16_b (
        .a(a[31:16]),
        .b({16{sub}} ^ b[31:16]),
        .cin(cout1),
        .sum(sum2),
        .cout()
     );
    
    assign sum = {sum2, sum1};

endmodule
```