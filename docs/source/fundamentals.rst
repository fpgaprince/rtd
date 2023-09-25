Fundamentals
************************
A background in these areas are helpful and probably the bare minimum. It is recommended to either learn or refresh.


Digital Electronics
============================================================
The world is analog. 

We understand and solve problem with math and science representing them through functions.

As problems became more complex/demanding/precision and the urgency to solve them became imperative/decisive/paramount, we needed better methods/means.

What started as analog, were no longer adequate. Thus the motivation, push/effort/drive/race for/towards digital techniques/methods/path/road and electronics.

We are in a digital era. 


Transistors
------------------
    A transistor is a semiconductor device that regulates or controls current/voltage. 
    It has operating regions, (cutoff, linear, active, saturdation).
    By driving a transistor into it's saturation region, we allow it to be fully on, driving whatever it's connected to.
    Conversely, removing the stimulus, we force it into the cutoff region, shutting off whatever it's connected to.
    Essentially, we use this as a switch. A switch to enable/disable on/off some other circuit.

Bits
------------------
    In the digital realm/digital system, everything is discrete as apposed to being continuous in its analog counterpart/realm/domain..
    We limit our quantization or representation of signal (data) to two discrete states.

    Something with only two states/parts/element, can be described as binary.
    In math, systems, numbers and notation can also be binary.
    Our math and arithmetic manipulation will all revolve around this and will lay the groundwork and foundation for digital systems.

    The states are quantize into two binary digits (BIT), 1 and 0. 
    Note, that this is simply a numerical representation.. 
    At the circuit level, there is no such thing as a 1 or a 0.
    
    What are we quantizing? Voltage levels.
    There are only voltage levels, commonly 5V, 3.3V, 2.5V, 1.8V. (depending on time and technology)


    What do we mean by states? The state of the transistor, on or off.
    By controling the voltage level, we determine whether one is on or off.
    

    


.. note::
    The math came first. Boolean and logical operations. Their realization in hardware, electrical circuit, switches.



Digital Logic
------------------
    By arranging transistors in specific ways and taking advantage of their saturation regions, we can create logical functions.




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


