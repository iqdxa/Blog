---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Module shift
- 来源：[Module shift - HDLBits](https://hdlbits.01xz.net/wiki/Module_shift)

### Problem Statement
You are given a module `my_dff` with two inputs and one output (that implements a D flip-flop). Instantiate three of them, then chain them together to make a shift register of length 3. The `clk` port needs to be connected to all instances.

The module provided to you is: `module my_dff ( input clk, input d, output q );`

Note that to make the internal connections, you will need to declare some wires. Be careful about naming your wires and module instances: the names must be unique.

[![](https://hdlbits.01xz.net/mw/images/6/60/Module_shift.png)](https://hdlbits.01xz.net/wiki/File:Module_shift.png)

### Official Solution

```Verilog
module top_module (
	input clk,
	input d,
	output q
);

	wire a, b;	// Create two wires. I called them a and b.

	// Create three instances of my_dff, with three different instance names (d1, d2, and d3).
	// Connect ports by position: ( input clk, input d, output q)
	my_dff d1 ( clk, d, a );
	my_dff d2 ( clk, a, b );
	my_dff d3 ( clk, b, q );

endmodule
```

### My Solution

```Verilog
module top_module ( input clk, input d, output q );

    wire q1,q2;
    my_dff u_my_dff_1( 
        .clk(clk),
        .d(d),
        .q(q1)
    );
    
    my_dff u_my_dff_2( 
        .clk(clk),
        .d(q1),
        .q(q2)
    );
    
    my_dff u_my_dff_3( 
        .clk(clk),
        .d(q2),
        .q(q)
    );
    
endmodule
```

### Note
- 如是采用根据名称进行例化，像这种需要例化很多个模块的情况，就很繁琐，有没有快捷的方法？比如这道题使用根据位置进行例化？比如让AI进行例化？