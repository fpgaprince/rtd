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

    0101    &= \mathbf{(0)}\; 2^3   + \mathbf{(1)}\; 2^2    + \mathbf{(0)}\; 2^1    + \mathbf{(1)}\; 2^0\\
            &= \mathbf{(0)}\; 8     + \mathbf{(1)}\; 4      + \mathbf{(0)}\; 2      + \mathbf{(1)}\; 1\\
            &= 0 + 4 + 0 + 1\\
            &= 5         
             

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
    

::

    Decimal     4bit binary
    0           0000
    1           0001
    2           0010
    3           0011
    4           0100
    5           0101
    6           0110
    7           0111
    8           1000
    9           1001
    10          1010
    11          1011
    12          1100
    13          1101
    14          1110
    15          1111


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
========================================
Earlier, we use 4bits to represent a decimal value. How many values can we represent with 4bits?
To determine this, you raise 2 to the power of bits.

    2^4 = 16

This means.. you can represent up to 16 decimal values. 
Because we need to represent 0, we need to include it in the count, 
so we have to subtract 1 from the top end, 16.

    The range becomes [0, 1, ... , 14, 15]

If we use other bit widths, 

::

    2^8 = 256           , range [0, 1, ..., 254, 255]
    2^16 = 65536        , range [0, 1, ..., 65534, 65535]
    2^32 = 4294967296   , range [0, 1, ..., 4294967294, 4294967295]

Notice, the max value is always 2^bit - 1.

I've included these width, as you'll run across them frequently.

::
    
    2^2     = 4
    2^3     = 8
    2^4     = 16
    2^5     = 32
    2^6     = 64
    2^7     = 128
    2^8     = 512
    2^10    = 1024
    2^12    = 4096
    2^14    = 16384
    2^15    = 32768

Notice that with every increase of the width by 1 bit, you double the number of representable values.





Hexidecimal and Binary relationship
========================================
When we spoke of hexadecimal representation, we said that each position of the hexadecimal value could be 1 of 16 decimal values (0 through 15, in which 10-15 are represented by A-F).

    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)

Remember that at the circuit/hardware/physical level, there is no such thing as hexadecimal. There is only binary.
Hexadecimal is just a system we apply for our own benefit, for us to represent and manipulate data.

So.. how is it related to binary. Well, we need to represent 16 decimal values.
In our previous example, we determined that 4 bits can represent 16 decimal values.

    Each position of a hex value requires 4bits to represent it.

::

   0xD,            requires 1x4 = 4bits.
   0xDE,           requires 2x4 = 8bits.
   0xDEA,          requires 3x4 = 12bits.
   0xDEAD,         requires 4x4 = 16bits.
   0xDEADB,        requires 5x4 = 20bits.
   0xDEADBE,       requires 6x4 = 24bits.
   0xDEADBEE,      requires 7x4 = 28bits.
   0xDEADBEEF,     requires 8x4 = 32bits.    

If we list out all the binary values 4 bits produce, we can see the relation between the hex2dec and dec2bin values.

::

    hex     Decimal     4bit binary
    0	    0           0000
    1	    1           0001
    2	    2           0010
    3	    3           0011
    4	    4           0100
    5	    5           0101
    6	    6           0110
    7	    7           0111
    8	    8           1000
    9	    9           1001
    A	    10          1010
    B	    11          1011
    C	    12          1100
    D	    13          1101
    E	    14          1110
    F	    15          1111

Bare with me.. if we use the table above to convert from hex to 

::

    0xD,            0x1101
    0xDE,           0x1101_1110
    0xDEA,          0x1101_1110_1010
    0xDEAD,         0x1101_1110_1010_1101
    0xDEADB,        0x1101_1110_1010_1101_1011
    0xDEADBE,       0x1101_1110_1010_1101_1011_1110
    0xDEADBEE,      0x1101_1110_1010_1101_1011_1110_1110
    0xDEADBEEF,     0x1101_1110_1010_1101_1011_1110_1110_1111



We will now define a byte
    
    a byte is an 8 bit value, or consists of 8 bits.

A byte therefore consists of 2 hexadecimal values. A hex = 4 bits, 2*4 = 8.

::

    0xDE_AD_BE_EF,     0x11011110_10101101_10111110_11101111,       4bytes * 8bits = 32bits

::

    32 bit      /8 = 4 bytes
    64 bit      /8 = 8 bytes
    128 bit     /8 = 16 bytes
    256 bit     /8 = 32 bytes
    512 bit     /8 = 64 bytes
    1024 bit    /8 = 128 bytes


By this point, we should have a grasp of binary and hex in relation to the decimal numbering system and in relation to each other.
We've also showed how width and range determine/dictate data representation.

.. note::

    We have not yet made the connection/relation/translation of this to circuit/logic aside from defining/describing the bit in earlier section.
    Nor have we showed their application. Patience! we're building up to it.. this is all necessary!






Negative Representation
========================================

We are going to return to binary numbers for a minute.
Up to this point we've only spoke of/represented positive numbers.
We need to discuss negative numbers and how it is interpreted/implemented.
There are several approaches, but I will discuss what is called 2's complement
Note, our binary decimal conversions
in earlier section utilized this 2's complement.

    2's comp is probably the most commmon 
    interpretation and usage of binary numbers. 


With 2's complement, the MSB is defined/used as the sign bit.
It's power of two value is negated, while the rest remain positive.


Convert from Binary to Negative Decimal
-------------------------------------------------------------
We will use a 4bit binary value to illustrate. 

In 4bit binary, the 4th bit (3rd index) normally would have a weight of 8 (2^3),
but we're negating it, -8. 

Only showing the sum of the power of 2s.

e.g. 1100
= -8 + 4 + 0 + 0 = -4

e.g. 1001 
= -8 + 0 + 0 + 1 = -7

e.g. 1110
= -8 + 4 + 2 + 0 = -2


Remember that, a 4bit binary value gives us 16 unique combinations..
But because the MSB represents a sign, we lose half of our positive representation
to the new negative values. 
We will show how the bit width determines range again "applied to negative numbers"

See below.

::

    Decimal	    4bit binary     Negative
    0           0000            0
    1           0001            1
    2           0010            2
    3           0011            3
    4           0100            4
    5           0101            5
    6           0110            6
    7           0111            7
    8           1000            -8
    9           1001            -7
    10          1010            -6
    11          1011            -5
    12          1100            -4
    13          1101            -3
    14          1110            -2
    15          1111            -1

If it was..

5bits   = 32 max pos val, 32/2 = 16,    range: 0 to 15 and -16 to -1.

6bit    = 64 max pos val, 64/2 = 32,    range: 0 to 31 and -32 to -1.

7bit    = 128 max pos val, 128/2 = 64,  range: 0 to 63 and -64 to -1.

.. note::

    We will show this mathematically later.

Notice the MSB dictates/limits the most negative value you can represent.
Max neg val will always be MSB = 1, followed by all 0s.

::

    10      = -2
    100     = -4
    1000    = -8
    10000   = -16
    100000  = -32
    1000000 = -64
    etc..

If you want to represent -7, you need atleast 4 bits, 3 is insufficient.

If you want to represent -24, you need atleast 6 bits, 5 is insufficient.

Convert from Negative Decimal to Binary
-------------------------------------------------------------
To convert from a negative decimal value to binary..

#.  Determine how many bit you need/want. 
#.  Determine the maximum positive value for that number of bits.
#.  Add that max value to your negative value.
#.  Convert the 'positive' value to its binary representation.

we're using 4bits, so the max value is 2^4 = 16.

-5 + 16 = 11, convert 11 as you had previously.
::

    11/2    = R1, LSB
    5/2     = R1
    2/2     = R0
    0/2     = R1, MSB
    -5      = 1011


-4 + 16 = 12, convert 12 as you had previously.
::

    12/2    = R0, LSB
    6/2     = R0
    3/2     = R1
    1/2     = R1, MSB
    -4      = 1100

-2 + 16 = 14, convert 14 as you had previously.
:: 

    14/2    = R0, LSB
    7/2     = R1
    3/2     = R1
    1/2     = R1, MSB
    -2      = 1110

-8 + 16 = 8, convert 8 as you had previously.
:: 

    8/2     = R0, LSB
    4/2     = R0
    2/2     = R0
    1/2     = R1, MSB
    -8      = 1000
    

-1 + 16 = 15, convert 15 as you had previously.
:: 

    15/2    = R1, LSB
    7/2     = R1
    3/2     = R1
    1/2     = R1, MSB
    -1      = 1111
    

Had we used 5bits for our 2's complement, our max value would have been 32 instead of 16.
And our steps would have resulted in a different conversion value. 

For instance -8.

-8 + 32 = 24
:: 

    24/2    = R0, LSB
    12/2    = R0
    6/2     = R0
    3/2     = R1
    1/2     = R1, MSB
    -8      = 11000

-1 with 5 bits is 11111

-1 for any number of bits will be all 1's.


.. note::
    
    We use base-2, base-10, base-16. which is the same as radix-2, radix-10, radix-16.



1's complement. 
========================================
Later..

And sign and magnitude.
========================================
Later..

Octal
========================================
Later..



Fixed-Point
****************************************

We briefly touched on this topic when talking about fractional decimal numbers.

Thus far we've dealt with only whole numbers, integers.

To represent fractional decimal numbers in binary, we mentally set where the decimal is the value.
In the system which uses the fixed point value, we set this up ahead of time, so that it knows
where the decimal is. Basically, we define how many bits we're using to the left and to the right of the decimal point.

::

    mmmm.nnnn       mmmm.nn         mmmmmmmmm.nnn
    Q4.4            Q4.2            Q8.4

The bits to the left represent the integer as we've been dealing with. nothing different. same rules.
the right is similar, but the weights are different.. the powers of 2's are negative, creating fractional weights.
A 1 or 0 will determine whether or not we add the fraction.

Qm.n is a notation used to represent fixed point numbers. The left m value represents the number of bits used to represent
the integer, and the n bit on the right represents how many bits to represent the fractional portion.

If our bit width is set, the placement of the decimal point determines the range of the integer 
as well as the range of the fraction. The fraction is also called precision.
More precision means more bits dedicated to its value. Less precision, means less precise. lol..
Precisely..

.. math::
    
    &= \mathbf{(b_1)}\; 2^{-1}  + \mathbf{(b_2)}\; 2^{-2}   + \mathbf{(b_3)}\; 2^{-3}   + \mathbf{(b_4)}\; 2^{-4}   + \ldots +  \mathbf{(b_n)}\; 2^{-n}\\
    &= \mathbf{(b_1)}\; 1/2^1   + \mathbf{(b_2)}\; 1/2^2    + \mathbf{(b_3)}\; 1/2^3    + \mathbf{(b_4)}\; 1/2^4    + \ldots +  \mathbf{(b_n)}\; 1/2^n\\
    &= \mathbf{(b_1)}\; 0.5     + \mathbf{(b_2)}\; 0.25     + \mathbf{(b_3)}\; 0.125    + \mathbf{(b_4)}\; 0.0625   + \ldots +  \mathbf{(b_n)}\; 2^{-n}


.. math::

    .0101   &= \mathbf{(0)}\; 2^{-1}    + \mathbf{(1)}\; 2^{-2} + \mathbf{(0)}\; 2^{-3} + \mathbf{(1)}\; 2^{-4}\\
            &= \mathbf{(0)}\; 0.5       + \mathbf{(1)}\; 0.25   + \mathbf{(0)}\; 0.125  + \mathbf{(1)}\; 0.0625\\
            &= 0 + 0.25 + 0 + 0.0625\\
            &= 0.3125         

If we wrote instead 0101.0101, then it becomes 5.3125

These are a few of the fractional weights.
::

    -1      -2      -3      -4      -5          -6          -7          -8              
    0.5     0.25    0.125   0.0625  0.03125     0.015625    0.0078125   0.00390625      


.. math::

    .0110   &= \mathbf{(0)}\; 0.5 + \mathbf{(1)}\; 0.25 + \mathbf{(1)}\; 0.125 + \mathbf{(1)}\; 0.0625\\
            &= 0 + 0.25 + 0.125 + 0\\
            &= 0.375         

If we wrote 0111.0110, then it becomes 7.375

One more!

.. math::

    .011011     &= \mathbf{(0)}\; 0.5 + \mathbf{(1)}\; 0.25 + \mathbf{(1)}\; 0.125 + \mathbf{(0)}\; 0.0625 + \mathbf{(1)}\; 0.03125 + \mathbf{(1)}\; 0.015625\\
                &= 0 + 0.25 + 0.125 + 0 + 0.03125 + 0.015625\\
                &= 0.421875       

If we wrote 0110.0110, then it becomes 6.421875

Notice the furthest bit to the right in the fraction is the LSB. and determines the granularity of our fraction.
For instance if we used 3 fractional bits.. the granularity would be 0.125

::

    .000    = 0.0
    .001    = 0.125
    .010    = 0.25
    .011    = 0.375
    .100    = 0.5
    .101    = 0.625
    .110    = 0.75
    .111    = 0.875

If we used 4 bits.. we'd have 0.0625 granularity
::

    .0000   = 0.0
    .0001   = 0.0625
    .0010   = 0.125
    .0011   = 0.1875
    .0100   = 0.25
    .0101   = 0.3125
    .0110   = 0.375
    .0111   = 0.4375
    .1000   = 0.5
    .1001   = 0.5625
    .1010   = 0.625
    .1011   = 0.6675
    .1100   = 0.75
    .1101   = 0.8125
    .1110   = 0.875
    .1111   = 0.9375

.. attention::

    Notice, there are only a discrete number of fractional values we can represent.
    If whatever decimal value we are trying to use does not match up exactly, it
    will be rounded to the closest. Rounding is another subject.


Convert Decimal Fraction to Binary
-------------------------------------------------------------
Say we want 4bit precision..

::

    0.4375/0.0625   = 7 ,   = 0.0111
    0.875/0.0625    = 14,   = 0.1110
    0.375/0.0625    = 6,    = 0.0110

    0.380/0.0625    = 6.08  = 0.0110,   drop the fractional decimal, it cannot be represented..
    0.4/0.0625      = 6.4   = 0.0110,   drop the fractional decimal, it cannot be represented..

    oh oh... the last two values equated to the same fractional representation.
    we did not have enough precision to represent it!

    0.888/0.0625    = 14.208    = 0.1110
    0.880/0.0625    = 14.08     = 0.1110

    same thing again!

so the question is.. if we wanted to represent some fractional decimal value..
how much granularity and thus bits do we need.

recall.. 
::

    -1      -2      -3      -4      -5          -6          -7          -8              
    0.5     0.25    0.125   0.0625  0.03125     0.015625    0.0078125   0.00390625          

is the fractional decimal divisible by the LSB fractional value.
LOL.. we should really start throwing in the math.. to be more precise and consise..
typing so much words................

.. warning::

    say i wanted to represent 0.4, at 9 fractional bits.. i can get close to 0.4,
    but not EXACT. this is an issue!



.. note::

    reminder to self: log(decimal value) / log(2) because base2. binary...
   
Fixed-point rounding
****************************************
sigh.............


Floating-Point
****************************************
Later... a little more advance topic..


Binary Arithmetic
****************************************

2s comp
====================

sign extension
====================

1s comp
====================

sign magnitude
====================




Hardware Descriptive Language (VHDL or Verilog)
####################################################

            &\text{Sometimes you will see this base notation}\\