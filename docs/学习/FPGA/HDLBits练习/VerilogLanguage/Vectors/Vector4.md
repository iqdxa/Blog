# Vector4
- 来源：[Vector4 - HDLBits](https://hdlbits.01xz.net/wiki/Vector4)

### Problem Statement

The [concatenation operator](https://hdlbits.01xz.net/wiki/Vector3 "Vector3") allowed concatenating together vectors to form a larger vector. But sometimes you want the same thing concatenated together many times, and it is still tedious to do something like assign a = {b,b,b,b,b,b};. The replication operator allows repeating a vector and concatenating them together:

{num{vector}}

This replicates _vector_ by _num_ times. _num_ must be a constant. Both sets of braces are required.

Examples:
```Verilog
{5{1'b1}}           // 5'b11111 (or 5'd31 or 5'h1f)
{2{a,b,c}}          // The same as {a,b,c,a,b,c}
{3'd5, {2{3'd6}}}   // 9'b101_110_110. It's a concatenation of 101 with
                    // the second vector, which is two copies of 3'b110.
```
## A Bit of Practice

One common place to see a replication operator is when sign-extending a smaller number to a larger one, while preserving its signed value. This is done by replicating the sign bit (the most significant bit) of the smaller number to the left. For example, sign-extending 4'b**0**101 (5) to 8 bits results in 8'b**0000**0101 (5), while sign-extending 4'b**1**101 (-3) to 8 bits results in 8'b**1111**1101 (-3).

Build a circuit that sign-extends an 8-bit number to 32 bits. This requires a concatenation of 24 copies of the sign bit (i.e., replicate bit[7] 24 times) followed by the 8-bit number itself.

### Official Solution

```Verilog
module top_module (
	input [7:0] in,
	output [31:0] out
);

	// Concatenate two things together:
	// 1: {in[7]} repeated 24 times (24 bits)
	// 2: in[7:0] (8 bits)
	assign out = { {24{in[7]}}, in };
	
endmodule
```

### My Solution

```Verilog
module top_module (
    input [7:0] in,
    output [31:0] out );//

    // assign out = { replicate-sign-bit , the-input };
    assign out = { in[7] ? {24{1'b1}} : {24{1'b0}} , in };

endmodule
```

### Note

- 最开始使用的是if语句，结果一直都无法编译通过，一直报错：
```
Error (10759): Verilog HDL error at top_module.v(7): object in declared in a list of port declarations cannot be redeclared within the module body File: /home/h/work/hdlbits.5429460/top_module.v Line: 7
```
- 在[求教，verilog里面能在if语句中使用assign吗 - 数字IC设计讨论(IC前端|FPGA|ASIC) - EETOP 创芯网论坛 (原名：电子顶级开发网) -](https://bbs.eetop.cn/thread-308613-1-1.html)发现有人说：
	- verilog 中可综合的只有always 和 assign两种语句，if else只能用在always语句块里面。
	- assign 用于连续赋值语句，if-else用于RTL级描述中，被赋值的变量都是reg类型。  
	- reg类型赋值分blocked和nonblocked，即=和<=，不需要再使用assign
- 所以最后使用的是`?:`语句。
- 我的代码比较冗余。