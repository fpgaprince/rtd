************************
Sequential Circuits
************************
Consists of storage elements and clocking. Introducing timing element.

Allow us to create more sophisticated circuits, solving more complex problems.

Time and timing is everything in this world..




Circuit Analysis
##########################


Timing/Clocking
##########################
While all the memory devices above can function/live w/o a clock.
It is when we add timing, things become interesting.

Previously, they just require a "transition." So that does not necessarily 
imply periodic.

Shift Register
##########################

Shift Registers
:: 

    A static Shift Register usually involves:

        A clock
        An optional clock enable
        A serial data input
        A serial data output

    Vivado synthesis implements inferred Shift Registers on SRL-type resources such as:

    SRL16E
    SRLC32E

    Depending on the length of the Shift Register, Vivado synthesis does one of the following:

    Implements it on a single SRL-type primitive
    Takes advantage of the cascading capability of SRLC-type primitives
    Attempts to take advantage of this cascading capability if the rest of the design uses some intermediate positions of the Shift Register



Counters
##########################


FSM Finite State Machine
##########################




MAC?
=========================
Multiplay Accumulate
It belongs here because it requires storage, register and registers require clocks.