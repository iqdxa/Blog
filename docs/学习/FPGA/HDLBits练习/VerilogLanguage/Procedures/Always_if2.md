---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-07-31
---

# Always if2
- 来源：[Always if2 - HDLBits](https://hdlbits.01xz.net/wiki/Always_if2)

### Problem Statement
#### A common source of errors: How to avoid making latches

When designing circuits, you _must_ think first in terms of circuits:

- I want this logic gate
- I want a _combinational_ blob of logic that has these inputs and produces these outputs
- I want a combinational blob of logic followed by a set of flip-flops

What you _must not_ do is write the code first, then hope it generates a proper circuit.

- If (cpu_overheated) then shut_off_computer = 1;
- If (~arrived) then keep_driving = ~gas_tank_empty;

Syntactically-correct code does not necessarily result in a reasonable circuit (combinational logic + flip-flops). The usual reason is: "What happens in the cases other than those you specified?". Verilog's answer is: Keep the outputs unchanged.

This behaviour of "keep outputs unchanged" means the current state needs to be _remembered_, and thus produces a _latch_. Combinational logic (e.g., logic gates) cannot remember any state. Watch out for Warning (10240): ... inferring latch(es)" messages. Unless the latch was intentional, it almost always indicates a bug. Combinational circuits must have a value assigned to all outputs under all conditions. This usually means you always need else clauses or a default value assigned to the outputs.

#### Demonstration

The following code contains incorrect behaviour that creates a latch. Fix the bugs so that you will shut off the computer only if it's really overheated, and stop driving if you've arrived at your destination or you need to refuel.

  

[![](https://hdlbits.01xz.net/mw/images/d/d1/Always_if2.png)](https://hdlbits.01xz.net/wiki/File:Always_if2.png)

This is the circuit described by the code, not the circuit you want to build.
```verilog
always @(*) begin
    if (cpu_overheated)
       shut_off_computer = 1;
end

always @(*) begin
    if (~arrived)
       keep_driving = ~gas_tank_empty;
end
```

### My Solution

```Verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input      cpu_overheated,
    output reg shut_off_computer,
    input      arrived,
    input      gas_tank_empty,
    output reg keep_driving  ); //

    always @(*) begin
        if (cpu_overheated)
           shut_off_computer <= 1;
        else
            shut_off_computer <= 1'b0;
    end

    always @(*) begin
        if (~arrived)
           keep_driving <= ~gas_tank_empty;
        else
            keep_driving <= 1'b0;
    end

endmodule
```

### Note
- 为了避免产生锁存器（latch），需要避免以下几种情况：
	- if语句没有有else分支
	- case语句没有列举所有情况且无default分支
	- 输出变量赋值给自己