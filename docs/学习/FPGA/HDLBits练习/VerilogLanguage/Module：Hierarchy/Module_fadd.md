---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
time: 2025-07-30
---
# Module fadd
- 来源：[Module fadd - HDLBits](https://hdlbits.01xz.net/wiki/Module_fadd)

### Problem Statement
In this exercise, you will create a circuit with two levels of hierarchy. Your `top_module` will instantiate two copies of `add16` (provided), each of which will instantiate 16 copies of `add1` (which you must write). Thus, you must write _two_ modules: `top_module` and `add1`.

Like module_add, you are given a module `add16` that performs a 16-bit addition. You must instantiate two of them to create a 32-bit adder. One `add16` module computes the lower 16 bits of the addition result, while the second `add16` module computes the upper 16 bits of the result. Your 32-bit adder does not need to handle carry-in (assume 0) or carry-out (ignored).

Connect the `add16` modules together as shown in the diagram below. The provided module `add16` has the following declaration:
```Verilog
module add16 ( 
	input[15:0] a, 
	input[15:0] b, 
	input cin, 
	output[15:0] sum, 
	output cout 
);
```


Within each `add16`, 16 full adders (module `add1`, not provided) are instantiated to actually perform the addition. You must write the full adder module that has the following declaration:
```Verilog
module add1 ( input a, input b, input cin, output sum, output cout );
```

Recall that a full adder computes the sum and carry-out of a+b+cin.

In summary, there are three modules in this design:

- `top_module` — Your top-level module that contains two of...
- `add16`, provided — A 16-bit adder module that is composed of 16 of...
- `add1` — A 1-bit full adder module.

  
If your submission is missing a `module add1`, you will get an error message that says `Error (12006): Node instance "user_fadd[0].a1" instantiates undefined entity "add1"`.

  

[![](https://hdlbits.01xz.net/mw/images/f/f3/Module_fadd.png)](https://hdlbits.01xz.net/wiki/File:Module_fadd.png)

??? tip
	Full adder equations:  
	sum = a ^ b ^ cin  
	cout = a&b | a&cin | b&cin

### My Solution

```Verilog
module top_module (
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);//
    reg [15:0] sum1;
    reg [15:0] sum2;
    wire cout;
    
    add16 u_add16_1(
        .a(a[15:0]),
        .b(b[15:0]),
        .cin(0),
        .cout(cout),
        .sum(sum1)
    );
    
    add16 u_add16_2(
        .a(a[31:16]),
        .b(b[31:16]),
        .cin(cout),
        .cout(),
        .sum(sum2)
    );

    assign sum = {sum2, sum1};
    

endmodule

module add1 ( input a, input b, input cin,   output sum, output cout );

	// Full adder module here
    assign sum = a ^ b ^ cin;
    assign cout = a & b | a & cin | b & cin;
    
endmodule
```

### Note
- 最开始实现的是：一个16位加法器和16个1位加法器，提交以后总是报错。
- 于是在网上搜索答案，看到这篇文章：[HDLBits 题目打卡module fadd、module cseladd-CSDN博客](https://blog.csdn.net/weixin_44157994/article/details/113545312)，才发现是实现例化两个16位的加法器和实现一个1位加法器。看来连题目都没有理解清除。