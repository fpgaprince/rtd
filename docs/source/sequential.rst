************************
Sequential Circuits
************************
Are circuits with memory.
Their output is a function of present and previous input; their is history, memory..
There is feedback.






Circuit Analysis
##########################


Clocking the Control Signal
####################################################
Up to now we've only referred to the control signal/enable signal.
While latches do not require a clock, they do have some sort of enable signal.
This enable signal determines when and when not to store information.

If, we instead, made this signal toggle periodically.. say, with a clock/oscillator.

It is when we add timing, things become interesting.
It allow us to create more sophisticated circuits, solving more complex problems.

Time and timing is everything in this world..
    We can synchornize multiple events.

    We can predetermine when things happen.

    We can expect things to happen at very specific times. We can predict.

    With a clock we establish a sense of time.


Clock Divider
####################################################


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