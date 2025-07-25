# Vector3
- 来源：[Vector3 - HDLBits](https://hdlbits.01xz.net/wiki/Vector3)

### Problem Statement
Part selection was used to select portions of a vector. The concatenation operator {a,b,c} is used to create larger vectors by concatenating smaller portions of a vector together.

```Verilog
{3'b111, 3'b000} => 6'b111000
{1'b1, 1'b0, 3'b101} => 5'b10101
{4'ha, 4'd10} => 8'b10101010     // 4'ha and 4'd10 are both 4'b1010 in binary
```

Concatenation needs to know the width of every component (or how would you know the length of the result?). Thus, {1, 2, 3} is illegal and results in the error message: unsized constants are not allowed in concatenations.

The concatenation operator can be used on both the left and right sides of assignments.

```Verilog
input [15:0] in;
output [23:0] out;
assign {out[7:0], out[15:8]} = in;         // Swap two bytes. Right side and left side are both 16-bit vectors.
assign out[15:0] = {in[7:0], in[15:8]};    // This is the same thing.
assign out = {in[7:0], in[15:8]};       // This is different. The 16-bit vector on the right is extended to
                                        // match the 24-bit vector on the left, so out[23:16] are zero.
                                        // In the first two examples, out[23:16] are not assigned.
```

#### A Bit of Practice

Given several input vectors, concatenate them together then split them up into several output vectors. There are six 5-bit input vectors: a, b, c, d, e, and f, for a total of 30 bits of input. There are four 8-bit output vectors: w, x, y, and z, for 32 bits of output. The output should be a concatenation of the input vectors followed by two 1 bits:

[![](https://hdlbits.01xz.net/mw/images/0/0c/Vector3.png)](https://hdlbits.01xz.net/wiki/File:Vector3.png)

### My Solution

```Verilog
module top_module (
    input [4:0] a, b, c, d, e, f,
    output [7:0] w, x, y, z );//

    // assign { ... } = { ... };
    assign {w,x,y,z} = {a,b,c,d,e,f,2'b11};
endmodule
```

### Note

- 输入的位数只有30位，输出的位数有32位，所以需要输入在末尾增加两位`2'b11`。

- 运行结果出现警告：
```
Warning (13024): Output pins are stuck at VCC or GND

This warning says that an output pin never changes (is "stuck"). This can sometimes indicate a bug if the output pin shouldn't be a constant. If this pin is not supposed to be constant, check for bugs that cause the value being assigned to never change (e.g., assign a = x & ~x;)
```

表明某些输出引脚始终保持在VCC(高电平)或GND(低电平)状态，从未变化。

忽略掉这个警告。