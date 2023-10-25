************************
Sequential Circuits
************************
Are circuits with memory.
Their output is a function of present and previous input; their is history, memory..
There is feedback.






Circuit Analysis
##########################







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

With a register, a clock and a combinational adder, we can create a counter.
The counter is instrumental in sequential design and is found everywhere.
It is how we set specific and/or determine time, how much time has passed.
When to do something, when to do something else. 







FSM Finite State Machine
##########################




MAC?
=========================
Multiplay Accumulate
It belongs here because it requires storage, register and registers require clocks.