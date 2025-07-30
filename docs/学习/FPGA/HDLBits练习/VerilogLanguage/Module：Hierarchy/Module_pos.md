---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Module pos
- 来源：[Module pos - HDLBits](https://hdlbits.01xz.net/wiki/Module_pos)

### Problem Statement
This problem is similar to the previous one ([module](https://hdlbits.01xz.net/wiki/module "module")). You are given a module named `mod_a` that has 2 outputs and 4 inputs, in that order. You must connect the 6 ports _by position_ to your top-level module's ports `out1`, `out2`, `a`, `b`, `c`, and `d`, in that order.

You are given the following module:

```Verilog
module mod_a ( output, output, input, input, input, input );
```

  

[![](https://hdlbits.01xz.net/mw/images/b/b7/Module_pos.png)](https://hdlbits.01xz.net/wiki/File:Module_pos.png)

### My Solution

```Verilog
module top_module ( 
    input a, 
    input b, 
    input c,
    input d,
    output out1,
    output out2
);
    
    mod_a u_mod_a(out1, out2, a, b, c, d);

endmodule
```