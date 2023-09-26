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

The decimal system uses 10 digits, hence dec-, to represent a value. They are
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9

We use it so much without thinking about it, but each digit/pace in a number, 1024 holds a weight.
From right to left, we have the ones place, the tens place, the hundreds, and the thousands.

.. math::

    1024    &= 1 \times 1000 + 0 \times 100 + 2 \times 10 + 4 \times 1\\
            &= 1 \times 10^3 + 0 \times 10^2 + 2 \times 10^1 + 4 \times 10^0

A number can be fractional.
1024.275

In which .275 is the fractional part. From left to right we have the tenths place, hundredths, thousandths, and so on.
Notice the "th" here to represent fraction when we speak of it in comparison to the whole number in the ladder.

.. math::

    .275    & = 2 \times 0.1 + 7 \times 0.01 + 5 \times 0.001\\
            &= 2 \times 10^-1 + 7 \times 10^-2 + 5 \times 10^-3

The number of places to the right of the decimal, represents how precise we want to be and is called precision.

Each place is a power of 10. 

There are 3 other systems we use, binary, hexadecimal and otcal. Although I have not really ever used octal, but have seen it.. 
the other two are heavily and extensively used. 


    A little more depth is provided.



Binary
^^^^^^^^^^^^^^
The binary system is used because it lends itself rather well to the nature of digital system where only two states are recognized, on or off, Vdd or GND and 1 or 0.
Furthermore, boolean algebra deals with logic operations/manipulation in which the values are only true or false or 1 or 0, again, two values/state.

Just as in a decimal system, each digit location/place carries a weight. 
In this case, a power of 2. The binary system only uses two digts to represent a value (often times a decimal value)
    0, 1

A binary number can look like this, 0101

.. math::

    0101    &= \mathbf{(0)}\; 2^3 + \mathbf{(1)}\; 2^2 + \mathbf{(0)}\; 2^1 + \mathbf{(1)}\; 2^0\\
            &= \mathbf{(0)}\; 8 + \mathbf{(1)}\; 4 + \mathbf{(0)}\; 2 + \mathbf{(1)}\; 1\\
            &= 0 + 4 + 0 + 1\\
            &= 5

.. math::


            
             

This 4 bit binary value represents a decimal value of 5. 

Let's try another one.. 0111

.. math::

    0111    &= \mathbf{\underline{0}} \times 2^3 + \mathbf{\underline{1}} \times 2^2 + \mathbf{\underline{1}} \times 2^1 + \mathbf{\underline{1}} \times 2^0\\
            &= \mathbf{\underline{0}} \times 8 + \mathbf{\underline{1}} \times 4 + \mathbf{\underline{1}} \times 2 + \mathbf{\underline{1}} \times 1\\
            &= 0 + 4 + 2 + 1\\
            &= 7

It helps to remember the results of the power of two (8,4,2,1) and their indices.

You'll naturally know it when you work with it enough.. 

    (1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1)

If you have to write it out, just start with '1' (on the far right) and keep multiplying by 2, working leftwards..

Notice the weight is greatest to the left and least to the right, we describe the bit on the left as the most significant bit (MSB)
and the right most, the least significant bit (LSB).

For the example above, the exponent values are 

    (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

And also resemble/coincide with an array's indices.
I personally prefer to start array indices with '0' for this reason and just for consistency sake, I'll name circuits, channels, DUTs likewise.



One more

.. math::

    01110111    &= 0 \times 2^7 + 1 \times 2^6 + 1 \times 2^5 + 1 \times 2^4 + 0 \times 2^3 + 1 \times 2^2 + 1 \times 2^1 + 1 \times 2^0\\
                &= 0 \times 128 + 1 \times 64 + 1 \times 32 + 1 \times 16 + 0 \times 8 + 1 \times 4 + 1 \times 2 + 1 \times 1\\
                &= 64 + 32 + 16 + 4 + 2 + 1\\
                &= 119
                
Here, we used 8 bits to represent a number. The more bits you have, the greater the range of numbers you can represent.
This is closely tied to 32bit vs 64bit processing speak with computers.

Notice also that the result of a binary representation is always an integer, a whole number. We'll go into fractions in a bit.


To go from from an arbitrary decimal value to its binary representation, you'll want to divide by 2 and track the remainder.
The first remainder of the division represents the LSB. The last, the MSB.

e.g. 9

.. math::

    9/2 &= 4\quad R\; 1\quad LSB\\
    4/2 &= 2\quad R\; 0\\
    2/2 &= 1\quad R\; 0\\
    1/2 &= 0\quad R\; 1\quad MSB\\
    \therefore \; 9   &\rightarrow\quad 1001


e.g. 12

.. math::

    12/2    &= 6\quad R\; 0\quad LSB\\
    6/2     &= 3\quad R\; 0\\
    3/2     &= 1\quad R\; 1\\
    1/2     &= 0\quad R\; 1\quad MSB\\
    \therefore \; 12      &\rightarrow\quad 1100

e.g. 7

.. math::

    7/2 &= 3\quad R\; 1\quad LSB\\
    3/2 &= 1\quad R\; 1\\
    1/2 &= 0\quad R\; 1\quad MSB\\
    \therefore \; 7   &\rightarrow\quad 111 
    
Notice 9 and 12 requires 4 bits to represent it while 7 only requires 3 bits. You can sign extend (discussed later) and represent 
7 with 4bits, it will be 0111. 

Lets try a larger number

e.g. 36

.. math::

    36/2    &= 18\quad R\; 0\quad LSB\\
    18/2    &= 9\quad R\; 0\\
    9/2     &= 4\quad R\; 1\\
    4/2     &= 2\quad R\; 0\\
    2/2     &= 1\quad R\; 0\\
    1/2     &= 0\quad R\; 1\quad MSB\\
    \therefore \; 12      &\rightarrow\quad 100100

This time 6 bits are required to represent the decimal value.
For compeletness..

.. math::

    100100  &= 1 \times 32 + 0 \times 16 + 0 \times 8 + 1 \times 4 + 0 \times 2 + 0 \times 1\\
            &= 32 + 4\\
            &= 36


.. note::
    
    Windows has programmer mode in its calculator app. It is very useful for doing conversions or checking your work.
    Or whip them up in excel. they have dec2bin or bin2dec, and you can create a table.
    


Lends itself to..

Hexadecimal
^^^^^^^^^^^^^^
The other numberal system used extensively is the hexadecimal system. hex- 16 digit/values are used and place/location are powers of 16.
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

Decimal values 10 through 15 are represented by alphabetical characters, A through F.
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

Because the weights are greater here, I'll use larger decimal numbers to convey the same idea from previous sections..
I will show a couple hexadecimal value, and convert it to decimal. 

e.g. 0x32

.. math::

    
    0x32    &= \mathbf{(3)}16^1 + \mathbf{(2)}16^0\\
            &= \mathbf{(3)}16 + \mathbf{(2)}1\\
            &= 48 + 2\\
            &= 50\\
            &\text{Sometimes notated as}\\
            &(32)_{16} \rightarrow (50)_{10}

This is base notation.





    I will show how to convert from decimal to hexidecimal.
----------------------------------------------------------------------------------------------------------------------------------------------------------------
    I will show how hexadcimal is related to binary. and the conversion between the two.
----------------------------------------------------------------------------------------------------------------------------------------------------------------

.. note::
    
    We use base-2, base-10, base-16. which is the same as radix-2, radix-10, radix-16.


Notice that as the weights increase, or by using a larger base, we can represent a larger decimal value through a smaller representation/ less digits.


Octal
^^^^^^^^^^^^^^


Fixed- and Floating-Point
--------------------------------

Binary Arithmetic
--------------------------------






Hardware Descriptive Language (VHDL or Verilog)
============================================================


