# Zero
- 来源：[Zero - HDLBits](https://hdlbits.01xz.net/wiki/Zero)

### Problem Statement

Build a circuit with no inputs and one output that outputs a constant 0

### Solution
```Verilog
module top_module ( output zero );
	
	assign zero = 1'b0;
	
endmodule
```