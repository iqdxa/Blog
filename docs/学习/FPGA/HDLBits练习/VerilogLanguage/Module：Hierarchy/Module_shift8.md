---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Module shift8
- 来源：[Module shift8 - HDLBits](https://hdlbits.01xz.net/wiki/Module_shift8)

### Problem Statement
This exercise is an extension of module_shift. Instead of module ports being only single pins, we now have modules with vectors as ports, to which you will attach wire vectors instead of plain wires. Like everywhere else in Verilog, the vector length of the port does not have to match the wire connecting to it, but this will cause zero-padding or trucation of the vector. This exercise does not use connections with mismatched vector lengths.

You are given a module `my_dff8` with two inputs and one output (that implements a set of 8 D flip-flops). Instantiate three of them, then chain them together to make a 8-bit wide shift register of length 3. In addition, create a 4-to-1 multiplexer (not provided) that chooses what to output depending on `sel[1:0]`: The value at the input d, after the first, after the second, or after the third D flip-flop. (Essentially, `sel` selects how many cycles to delay the input, from zero to three clock cycles.)

The module provided to you is: `module my_dff8 ( input clk, input [7:0] d, output [7:0] q );`

The multiplexer is not provided. One possible way to write one is inside an `always` block with a `case` statement inside. (See also: mux9to1v)

[![](https://hdlbits.01xz.net/mw/images/7/76/Module_shift8.png)](https://hdlbits.01xz.net/wiki/File:Module_shift8.png)

### Official Solution

```Verilog

```

### My Solution

```Verilog

```

### Note

- 这道题会用到后面的知识，可以先跳过，等完成后面的练习再做。