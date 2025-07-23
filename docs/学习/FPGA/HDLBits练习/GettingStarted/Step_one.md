# Step_one
- 来源：[Step one - HDLBits](https://hdlbits.01xz.net/wiki/Step_one)

### Problem Statement

We're going to start with a small bit of HDL to get familiar with the interface used by HDLBits. Here's the description of the circuit you need to build for this exercise:

Build a circuit with no inputs and one output. That output should always drive 1 (or logic high).

### Official Solution
```Verilog
module top_module( output one );
	
	assign one = 1'b1;
	
endmodule
```

### My Solution
```Verilog
module top_module( output one );

// Insert your code here
    assign one = 1;

endmodule

```