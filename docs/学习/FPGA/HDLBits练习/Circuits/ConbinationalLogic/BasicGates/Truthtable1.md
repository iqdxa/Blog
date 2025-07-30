---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Truthtable1
- 来源：[Truthtable1 - HDLBits](https://hdlbits.01xz.net/wiki/Truthtable1)

### Problem Statement
In the previous exercises, we used simple logic gates and combinations of several logic gates. These circuits are examples of _combinational_ circuits. Combinational means the outputs of the circuit is a function (in the mathematics sense) of only its inputs. This means that for any given input value, there is only one possible output value. Thus, one way to describe the behaviour of a combinational function is to explicitly list what the output should be for every possible value of the inputs. This is a truth table.

For a boolean function of N inputs, there are 2N possible input combinations. Each row of the truth table lists one input combination, so there are always 2N rows. The output column shows what the output should be for each input value.

| Row number | _Inputs_ |     |     | Outputs f |
| ---------- | -------- | --- | --- | --------- |
|            | x3       | x2  | x1  |           |
| 0          | 0        | 0   | 0   | 0         |
| 1          | 0        | 0   | 1   | 0         |
| 2          | 0        | 1   | 0   | 1         |
| 3          | 0        | 1   | 1   | 1         |
| 4          | 1        | 0   | 0   | 0         |
| 5          | 1        | 0   | 1   | 1         |
| 6          | 1        | 1   | 0   | 0         |
| 7          | 1        | 1   | 1   | 1         |

The above truth table is for a three-input, one-output function. It has 8 rows for each of the 8 possible input combinations, and one output column. There are four inputs combinations where the output is 1, and four where the output is 0.

### Synthesizing a circuit from a truth table

Suppose we want to build the above circuit, but we're limited to using only the set of standard logic gates. How would you build arbitrary logic functions (expressed as a truth table)?

One simple method to create a circuit that implements the truth table's function is to express the function in sum-of-products form. **Sum** (meaning OR) of **products** (meaning AND) means using one _N_-input AND gate per row of the truth table (to detect when the input matches each row), followed by an OR gate that chooses only those rows that result in a '1' output.

For the above example, the output is '1' if the input matches row 2 **or** row 3 **or** row 5 **or** row 7 (This is a 4-input OR gate). The input matches row 2 if x3=0 **and** x2=1 **and** x1=0 (This is a 3-input AND gate). Thus, this truth table can be implemented in canonical form by using 4 AND gates that are ORed together.

## A Bit of Practice

Create a combinational circuit that implements the above truth table.

  

[![](https://hdlbits.01xz.net/mw/images/f/f6/Truthtable1.png)](https://hdlbits.01xz.net/wiki/File:Truthtable1.png)

### Official Solution

```Verilog
module top_module (
	input x3,
	input x2,
	input x1,
	output f
);
	// This truth table has four minterms. 
	assign f = ( ~x3 & x2 & ~x1 ) | 
				( ~x3 & x2 & x1 ) |
				( x3 & ~x2 & x1 ) |
				( x3 & x2 & x1 ) ;
				
	// It can be simplified, by boolean algebra or Karnaugh maps.
	// assign f = (~x3 & x2) | (x3 & x1);
	
	// You may then notice that this is actually a 2-to-1 mux, selected by x3:
	// assign f = x3 ? x1 : x2;
	
endmodule
```

### My Solution

```Verilog
module top_module( 
    input x3,
    input x2,
    input x1,  // three inputs
    output f   // one output
);
    
    assign f = x1 & x3 | x2 & (~x3);

endmodule
```

### Note
- 根据真值表画出卡诺图

| x3/x2x1 | 00  | 01  | 11  | 10  |
| ------- | --- | --- | --- | --- |
| 0       | 0   | 0   | 1   | 1   |
| 1       | 0   | 1   | 1   | 0   |
- 根据卡诺图可以写出表达式：$f=x_1x_3 + x_2\overline{x_3}$
- 官方答案给出了使用条件操作符的代码，就使得代码更加的简洁。