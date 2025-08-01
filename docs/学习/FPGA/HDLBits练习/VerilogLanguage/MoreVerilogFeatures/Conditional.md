---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-01
---

# Conditional
- 来源：[Conditional - HDLBits](https://hdlbits.01xz.net/wiki/Conditional)

### Problem Statement
Verilog has a ternary conditional operator ( ? : ) much like C:
```Verilog
(condition ? if_true : if_false)
```

This can be used to choose one of two values based on _condition_ (a mux!) on one line, without using an if-then inside a combinational always block.

Examples:
```Verilog
(0 ? 3 : 5)     // This is 5 because the condition is false.
(sel ? b : a)   // A 2-to-1 multiplexer between a and b selected by sel.

always @(posedge clk)         // A T-flip-flop.
  q <= toggle ? ~q : q;

always @(*)                   // State transition logic for a one-input FSM
  case (state)
    A: next = w ? B : A;
    B: next = w ? A : B;
  endcase

assign out = ena ? q : 1'bz;  // A tri-state buffer

((sel[1:0] == 2'h0) ? a :     // A 3-to-1 mux
 (sel[1:0] == 2'h1) ? b :
                      c )
```

## A Bit of Practice

Given four unsigned numbers, find the minimum. Unsigned numbers can be compared with standard comparison operators (a < b). Use the conditional operator to make two-way _min_ circuits, then compose a few of them to create a 4-way _min_ circuit. You'll probably want some wire vectors for the intermediate results.

### My Solution

```Verilog
module top_module (
    input [7:0] a, b, c, d,
    output [7:0] min);//

    // assign intermediate_result1 = compare? true: false;
    assign min = ((a < b ? a : b) < c ? (a < b ? a : b) : c) < d ? ((a < b ? a : b) < c ? (a < b ? a : b) : c) : d;
    
endmodule
```

### Note
- 本来最开始写的是以下代码：
```Verilog
assign min = a < b ? a : b;
assign min = min < c ? min : c;
assign min = min < d ? min : d;
```
- 结果报类似如下的错误：
```
Error (10028): Can't resolve multiple constant drivers for net "min[7]" at top_module.v(8)
```
- 但是不想使用中间变量，所以就把三行合成一行。