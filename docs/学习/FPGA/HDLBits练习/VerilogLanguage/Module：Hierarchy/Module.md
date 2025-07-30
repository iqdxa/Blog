---
authors:
  - TFC
tags:
  - HDLBits
  - Verilog
---
# Module
- 来源：[Module - HDLBits](https://hdlbits.01xz.net/wiki/Module)

### Problem Statement
By now, you're familiar with a `module`, which is a circuit that interacts with its outside through input and output ports. Larger, more complex circuits are built by _composing_ bigger modules out of smaller modules and other pieces (such as assign statements and always blocks) connected together. This forms a hierarchy, as modules can contain instances of other modules.

The figure below shows a very simple circuit with a sub-module. In this exercise, create one _instance_ of module `**mod_a**`, then connect the module's three pins (`in1`, `in2`, and `out`) to your top-level module's three ports (wires `a`, `b`, and `out`). The module `mod_a` is provided for you — you must instantiate it.

When connecting modules, only the ports on the module are important. You do not need to know the code inside the module. The code for module `mod_a` looks like this:

[![](https://hdlbits.01xz.net/mw/thumb.php?f=Module_moda.png&width=101)](https://hdlbits.01xz.net/wiki/File:Module_moda.png)

module mod_a ( input in1, input in2, output out );
    // Module body
endmodule

The hierarchy of modules is created by instantiating one module inside another, as long as all of the modules used belong to the same project (so the compiler knows where to find the module). The code for one module is not written _inside_ another module's body (Code for different modules are not nested).

You may connect signals to the module by port name or port position. For extra practice, try both methods.

  

[![](https://hdlbits.01xz.net/mw/images/c/c0/Module.png)](https://hdlbits.01xz.net/wiki/File:Module.png)
#### Connecting Signals to Module Ports

There are two commonly-used methods to connect a wire to a port: by position or by name.

##### By position

The syntax to connect wires to ports by position should be familiar, as it uses a C-like syntax. When instantiating a module, ports are connected left to right according to the module's declaration. For example:

`mod_a instance1 ( wa, wb, wc );`

This instantiates a module of type `mod_a` and gives it an _instance name_ of "instance1", then connects signal `wa` (outside the new module) to the **first** port (`in1`) of the new module, `wb` to the **second** port (`in2`), and `wc` to the **third** port (`out`). One drawback of this syntax is that if the module's port list changes, all instantiations of the module will also need to be found and changed to match the new module.

##### By name

Connecting signals to a module's ports _by name_ allows wires to remain correctly connected even if the port list changes. This syntax is more verbose, however.

`mod_a instance2 ( .out(wc), .in1(wa), .in2(wb) );`

The above line instantiates a module of type `mod_a` named "instance2", then connects signal `wa` (outside the module) to the port **named** `in1`, `wb` to the port **named** `in2`, and `wc` to the port **named** `out`. Notice how the ordering of ports is irrelevant here because the connection will be made to the correct name, regardless of its position in the sub-module's port list. Also notice the period immediately preceding the port name in this syntax.

### Official Solution

```Verilog
module top_module (
	input a,
	input b,
	output out
);

	// Create an instance of "mod_a" named "inst1", and connect ports by name:
	mod_a inst1 ( 
		.in1(a), 	// Port"in1"connects to wire "a"
		.in2(b),	// Port "in2" connects to wire "b"
		.out(out)	// Port "out" connects to wire "out" 
				// (Note: mod_a's port "out" is not related to top_module's wire "out". 
				// It is simply coincidence that they have the same name)
	);

/*
	// Create an instance of "mod_a" named "inst2", and connect ports by position:
	mod_a inst2 ( a, b, out );	// The three wires are connected to ports in1, in2, and out, respectively.
*/
	
endmodule
```

### My Solution

```Verilog
module top_module ( input a, input b, output out );

    mod_a u_mod_a(
        .in1(a),
        .in2(b),
        .out(out)
    );
    
endmodule
```