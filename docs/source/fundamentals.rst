Fundamentals
************************
A background in these areas are helpful and probably the bare minimum. It is recommended to either learn or refresh.

Digital Electronics
============================================================
The world is analog. 

We understand and solve problem with math and science representing them through functions.

As problems became more complex and the urgency to solve them became more critical, we needed better methods.

What started out as analog, was no longer adequate.

Transistors
------------------
    A transistor has its operating region.
    By driving a transistor into it's saturation region, we allow it to be fully on, driving whatever it's connected to.
    Conversely, removing the stimulus, we shut it and whatever off.
    Essentially, we use this as a switch. A switch to enable/disable on/off some other circuit.

Bits
------------------
    In the digital realm/digital system, everything is discrete as apposed to being continuous in its analog counterpart/realm/domain..
    We limit our quantization or representation of data to two discrete states.

    But what are we quantizing? Voltage levels.
    
    And thus we are limiting the transistors to two states, on or off.

    In math, a system in which only two states are used is binary.
    Our math and arithmetic manipulation will all revolve around this.

    We quantize these states into two binary digits (BIT), 1 and 0. 
    Note, that this is simply a numerical representation.. 
    At the circuit level, there is no such thing as 1 or 0.
    
    There are only voltage levels, commonly 5V, 3.3V, 2.5V, 1.8V. (depending on time and technology)


.. note::
    The math came first. Boolean and logical operations. Their realization in hardware, electrical circuit, switches.



Digital Logic
------------------



Digital Design
------------------
    FPGAs and ASICs share a common nature, that is, digital design logic and elements.. and so many terminology are shared, 
    but one must recognize the differences in how they are realized.

    We often talk about and show examples with gates in Digital Design, but one must remember, in an FPGA, we are not using gates (although NOT gates do exist in CLBs and throughout to flip bits and help with optimization)
    That is.. we're not connecting gates. We are only capturing the logic functionality or behavior.
    This functionality can be represented in a truth table (boolean equation) or state equation.
    FPGA tools will synthesize and map these equation to LUTs and other digital circuits/elements.

    In ASIC Design, designers will deal with gates. 






Numbering System
============================================================
Representation
--------------------------------

Fixed- and Floating-Point
--------------------------------

Binary Arithmetic
--------------------------------






Hardware Descriptive Language (VHDL or Verilog)
============================================================


