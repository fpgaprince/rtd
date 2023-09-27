************************
Fundamentals
************************
A background in these areas are helpful and probably the bare minimum. It is recommended to either learn or refresh.
Each of these topics are courses within their own right, but for brevity's sake and initial release, i will keep it minimal.


Digital Electronics
##########################
The world is analog. 

We understand and solve problem through math and science representing them with numbers and functions.

As problems became more complex/demanding/precision and the urgency to solve them became imperative/decisive/paramount, we needed better methods/means.

What started as analog, were no longer adequate. Thus the motivation, push/effort/drive/race for/towards digital techniques/methods/path/road and electronics.

We are in a digital era. 


Transistors
********************
    A transistor is a semiconductor device that regulates or controls current/voltage. 
    It has operating regions, (cutoff, linear, active, saturdation). 
    By driving a transistor into it's saturation region, we allow it to be fully on, driving whatever it's connected to.
    Conversely, removing the stimulus, we force it into the cutoff region, shutting off whatever it's connected to.
    Essentially, we use this as a switch. A switch to enable/disable on/off some other circuit.

Bits
********************
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
********************
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
********************








Numbering System
##########################
There are many number systems. It is a system we prescribe/use to quantify.


Representation
********************
    
Decimal
====================
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
====================
The binary system is used because it lends itself rather well to the nature of digital system where only two states are recognized, on or off, Vdd or GND and 1 or 0.
Furthermore, boolean algebra deals with logic operations/manipulation in which the values are only true or false or 1 or 0, again, two values/state.

Just as in a decimal system, each digit location/place carries a weight. 
In this case, a power of 2. The binary system only uses two digts to represent a value (often times a decimal value)
    0, 1


Convert from Binary to Decimal
--------------------------------------------
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


Convert from Decimal to Binary
--------------------------------------------
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
    



Hexadecimal
====================
The other numberal system used extensively is the hexadecimal system. hex- 16 digit/values are used and place/location are powers of 16.
        
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

Decimal values 10 through 15 are represented by alphabetical characters, A through F.
        
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F


Convert from Hexidecimal to Decimal
--------------------------------------------
I will show a couple hexadecimal value, and convert it to decimal. 

e.g. 0x32

.. math::

    0x32    &= \mathbf{(3)}16^1 + \mathbf{(2)}16^0\\
            &= \mathbf{(3)}16 + \mathbf{(2)}1\\
            &= 48 + 2\\
            &= 50\\
            &32_{16} \rightarrow 50_{10}

e.g. 0xDE

.. math::

    0xDE    &= \mathbf{(D)}16^1 + \mathbf{(E)}16^0\\
            &= \mathbf{(13)}16 + \mathbf{(14)}1\\
            &= 208 + 14\\
            &= 222\\
            &DE_{16} \rightarrow 222_{10}

e.g. 0xBEEF

.. math::

    0xBEEF      &= \mathbf{(B)}16^3 + \mathbf{(E)}16^2 + \mathbf{(E)}16^1 + \mathbf{(F)}16^0\\
                &= \mathbf{(11)}4096 + \mathbf{(14)}256 + \mathbf{(14)}16 + \mathbf{(15)}1\\
                &= 45056 + 3584 + 224 + 15\\
                &= 48,879\\
                &BEEF_{16} \rightarrow 48879_{10}

Notice that by using a larger base, the weights increases significantly. We are able to represent a larger decimal value with fewer digits/symbols.



Convert from Decimal to Hexidecimal
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Converting is from decimal to hex follows the same operation as in binary, except we divide by 16.
Because the weights are greater here, I'll use larger decimal numbers to convey the same idea in prior sections.

e.g. 3054

.. math::

    3054/16     &= 190\quad R\; 14\quad LSB\\
    190/16       &= 11\quad R\; 14\\
    11/16        &= 0\quad R\; 11\quad MSB\\
    \therefore \; &3054_{10} \rightarrow BEE_{16}

e.g. 27

.. math::

    27/16     &= 1\quad R\; 11\quad LSB\\
    1/16     &= 0\quad R\; 1\quad MSB\\
    \therefore \; &27_{10} \rightarrow 1B_{16}






Bit width and range of value
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Earlier, we use 4bits to represent a decimal value. How many values can we represent with 4bits?
To determine this, you raise 2 to the power of bits.

    2^4 = 16

This means.. you can represent up to 16 decimal values. 
Because we need to represent 0, we need to include it in the count, 
so we have to subtract 1 from the top end, 16.

    The range becomes [0, 1, ... , 14, 15]

If we use other bit widths, 
    
    2^8 = 256           , range [0, 1, ..., 254, 255]
    2^16 = 65536        , range [0, 1, ..., 65534, 65535]
    2^32 = 4294967296   , range [0, 1, ..., 4294967294, 4294967295]

Notice, the max value is always 2^bit - 1.

I've included these width, as you'll run across them frequently.

    2^2 = 4
    2^3 = 8
    2^4 = 16
    2^5 = 32
    2^6 = 64
    2^7 = 128
    2^8 = 512
    2^10 = 1024
    2^12 = 4096
    2^14 = 16384
    2^15 = 32768

Notice that with every increase of the width by 1 bit, you double the number of representable values.

When we spoke of hexadecimal representation, we said that each position of the hexadecimal value could be 1 of 16 decimal values (0 through 15, in which 10-15 are represented by A-F).

    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)

Remember that at the circuit/hardware/physical level, there is no such thing as hexadecimal. There is only binary.
Hexadecimal is just a system we apply for our own benefit, for us to represent and manipulate data.

So.. how is it related to binary. Well, we need to represent 16 decimal values.
In our previous example, we determined that 4 bits can represent 16 decimal values.

    Each position of a hex value requires 4bits to represent it.

*0xD,            requires 1x4 = 4bits.
*0xDE,           requires 2x4 = 8bits.
*0xDEA,          requires 3x4 = 12bits.
*0xDEAD,         requires 4x4 = 16bits.
*0xDEADB,        requires 5x4 = 20bits.
*0xDEADBE,       requires 6x4 = 24bits.
*0xDEADBEE,      requires 7x4 = 28bits.
*0xDEADBEEF,     requires 8x4 = 32bits.


If we list out all the binary values 4 bits produce, we can see the relation between the hex2dec and dec2bin values.

    hex	    Decimal	    4bit binary
    0	    0   	    0000
    1	    1   	    0001
    2	    2   	    0010
    3	    3   	    0011
    4	    4   	    0100
    5	    5   	    0101
    6	    6   	    0110
    7	    7	        0111
    8	    8	        1000
    9	    9	        1001
    A	    10	        1010
    B	    11	        1011
    C	    12	        1100
    D	    13	        1101
    E	    14	        1110
    F	    15  	    1111

Bare with me.. if we use the table above to convert from hex to 

    0xD,            0x1101
    0xDE,           0x1101_1110
    0xDEA,          0x1101_1110_1010
    0xDEAD,         0x1101_1110_1010_1101
    0xDEADB,        0x1101_1110_1010_1101_1011
    0xDEADBE,       0x1101_1110_1010_1101_1011_1110
    0xDEADBEE,      0x1101_1110_1010_1101_1011_1110_1110
    0xDEADBEEF,     0x1101_1110_1010_1101_1011_1110_1110_1111


Hexidecimal and Binary relationship
----------------------------------------------------------------------------------------------------------------------------------------------------------------




.. note::
    
    We use base-2, base-10, base-16. which is the same as radix-2, radix-10, radix-16.

Octal
====================


Fixed- and Floating-Point
****************************************

Binary Arithmetic
****************************************







Hardware Descriptive Language (VHDL or Verilog)
####################################################

            &\text{Sometimes you will see this base notation}\\