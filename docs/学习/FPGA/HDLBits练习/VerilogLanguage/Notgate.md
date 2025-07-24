# Notgate
- 来源：[Notgate - HDLBits](https://hdlbits.01xz.net/wiki/Notgate)

### Problem Statement
Create a module that implements a NOT gate.

This circuit is similar to wire, but with a slight difference. When making the connection from the wire `in` to the wire `out` we're going to implement an inverter (or "NOT-gate") instead of a plain wire.

Use an assign statement. The `assign` statement will _continuously drive_ the inverse of `in` onto wire `out`.

  

[![](https://hdlbits.01xz.net/mw/images/9/9e/Notgate.png)](https://hdlbits.01xz.net/wiki/File:Notgate.png)

### Official Solution
```Verilog
module top_module(
	input in,
	output out
);
	
	assign out = ~in;
	
endmodule
```

### My Solution
```Verilog
module top_module( input in, output out );

    assign out = ~in;
    
endmodule
```