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
There are many number systems. It is a system we prescribe/use to quantify.


Representation
--------------------------------
    
Decimal
^^^^^^^^^^^^^^
The most commmonly known one, taught at an early age is the decimal system.
It is a most convenient one we use day to day.

We use it so much without thinking about it, but each digit/pace in a number, 1024 holds a weight.
From right to left, we have the ones place, the tens place, the hundreds, and the thousands.

.. math::

    1024    = 1*1000 + 0*100 + 2*10 + 4*1

            = 1*10^3 + 0*10^2 + 2*10^1 + 4*10^0

A number can be fractional.
1024.275

In which .275 is the fractional part. From left to right we have the tenths place, hundredths, thousandths, and so on.
Notice the "th" here to represent fraction when we speak of it in comparison to the whole number in the ladder.

.. math::

    .275    = 2*0.1 + 7*0.01 + 5*0.001

            = 2*10^-1 + 7*10^-2 + 5*10^-3

The number of places to the right of the decimal, represents how precise we want to be and is called precision.

Each place is a power of 10.

There are 3 other systems we use, binary, hexadecimal and otcal. Although I have not really ever used octal, but have seen it.. the other two are heavily used. 




Binary
^^^^^^^^^^^^^^
The binary system is used because it lends itself rather well to the nature of digital system where only two states are recognized, on or off, Vdd or GND and 1 or 0.
Furthermore, boolean algebra deals with logic operations/manipulation in which the values are only true or false or 1 or 0, again, two values/state.

Just as in a decimal system, each digit location/place carries a weight. In this case, a power of 2.

A binary number can look like this, 0101, and it actually represents some decimal value.

.. math::

    0101    = 0*2^3 + 1*2^2 + 0*2^1 + 1*2^0

            = 0*8 + 1*4 + 0*2 + 1*1

            = 4 + 1

            = 5

This 4 bit binary value represents a decimal value of 5. Let's try another one..
    
    0111    = 0*2^3 + 1*2^2 + 1*2^1 + 1*2^0

            = 0*8 + 1*4 + 1*2 + 1*1

            = 4 + 2 + 1

            = 7



Lends itself to..
Hexadecimal
^^^^^^^^^^^^^^

Octal
^^^^^^^^^^^^^^


Fixed- and Floating-Point
--------------------------------

Binary Arithmetic
--------------------------------






Hardware Descriptive Language (VHDL or Verilog)
============================================================


