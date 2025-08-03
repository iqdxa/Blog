---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-08-02
---

# Adder3
- 来源：[Adder3 - HDLBits](https://hdlbits.01xz.net/wiki/Adder3)

### Problem Statement
Now that you know how to build a [full adder](https://hdlbits.01xz.net/wiki/Fadd "Fadd"), make 3 instances of it to create a 3-bit binary ripple-carry adder. The adder adds two 3-bit numbers and a carry-in to produce a 3-bit sum and carry out. To encourage you to actually instantiate full adders, also output the carry-out from _each_ full adder in the ripple-carry adder. cout[2] is the final carry-out from the last full adder, and is the carry-out you usually see.

### My Solution

```Verilog
module top_module( 
    input [2:0] a, b,
    input cin,
    output [2:0] cout,
    output [2:0] sum );
	
    always@(*)begin
        for(int i=0; i<3;i++)begin
            if(i == 0)
                {cout[i], sum[i]} = a[i] + b[i] + cin;
            else
            {cout[i], sum[i]} = a[i] + b[i] + cout[i-1];
        end
    end
endmodule
```

### Note
- 使用循环的实现方法，无论多少位都可以解决。