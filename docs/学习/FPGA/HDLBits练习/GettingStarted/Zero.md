---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Zero
- 来源：[Zero - HDLBits](https://hdlbits.01xz.net/wiki/Zero)

### Problem Statement

Build a circuit with no inputs and one output that outputs a constant 0

Now that you've worked through the previous problem, let's see if you can do a simple problem without the hints.

!!! Note
    HDLBits uses Verilog-2001 ANSI-style port declaration syntax because it's easier to read and reduces typos. You may use the older Verilog-1995 syntax if you wish. For example, the two module declarations below are acceptable and equivalent:
    ```Verilog
    module top_module ( zero );
        output zero;
        // Verilog-1995
    endmodule
    ```

    ```Verilog
    module top_module ( output zero ); 

        // Verilog-2001
    endmodule
    ```

??? tip
    Fun fact: For Quartus synthesis, not assigning a value to a signal usually results in 0. This problem is actually easier than the previous one.

### Official Solution
```Verilog
module top_module ( output zero );
	
	assign zero = 1'b0;
	
endmodule
```

### My Solution
```Verilog
module top_module(
    output zero
);// Module body starts after semicolon
    
    assign zero = 0;

endmodule
```