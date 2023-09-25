Fundamentals
************************
A background in these areas are helpful and probably the bare minimum. It is recommended to either learn or refresh.
Each of these topics are courses within their own right, but for brevity's sake and initial release, i will keep it minimal.


Digital Electronics
============================================================
The world is analog. 

We understand and solve problem through math and science representing them with numbers and functions.

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
    In math.. systems, numbers and notation can also be binary.
    Our math and arithmetic manipulation will all revolve around this and will lay the groundwork and foundation for digital systems.

    The states are quantized into two binary digits (BIT), 1 and 0. 
    A bit is defined as the smallest or most basic unit in digital systems.
    And we often speak of bits, but note that it is simply a numerical representation for something else.
    It is a system we have defined and agreed upon, symbolic, no different than the language we speak.


    Because..
    At the hardware/circuit/physical level, there is no such thing as a 1 or a 0.
    So then What are we quantizing exactly? and what do we mean by states?
    
        Electrical signals, voltages, and specifically in relation to transistors and thus their operating region, sate of on or off.

    In digital devices, these voltages (5V, 3.3V, 2.5V, 1.8V, depending on technology at the time) have commonly represented '1' and an on state while 
    0V represents '0' and an off state.

    

    


.. note::
    The math came first. Boolean and logical operations. Their realization in hardware, electrical circuit, switches.



Digital Logic
------------------
    By arranging transistors in specific ways and taking advantage of their saturation regions, we are able to realize/conceive/materialize? logical functions.

    This arrangement of transistors produce what are called Logic gates, circuits which perform logical operations. 
    These logical function/operation, take root in Boolean Algebra, which revolve around these core operation (NOT, AND, OR, XOR) and their variations.
    
    These logic gates become the fundamental building blocks and foundation of digital circuits.
    
    And digital circuits, ultimately are the constructs of modern digital systems.


.. note::
   FPGAs and ASICs share a common nature, that is, digital design logic and elements.. and so many terminology are shared, but one must recognize the differences 
   in how they are realized and/or implemented.    In an FPGA, we are not using gates (although NOT gates do exist in CLBs and throughout to flip bits and help with optimization). 
   That is.. we're not connecting gates. We are only capturing the logic functionality or behavior. This functionality can be represented in a truth table 
   (boolean equation) or state equation. FPGA tools will synthesize and map these equation to LUTs and other digital circuits/elements.


Digital Design
------------------








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


