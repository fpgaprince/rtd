************************
Sequential Circuits
************************
Are circuits with memory.
Their output is a function of present and previous input; there is history, memory..
There is feedback.


Circuit Analysis
##########################
Formal/Mathematical part..



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


From this point onward, all sequential circuit implies memory/storage and a clock.
The smallest memory element, being the flip flop. D FF to be specific.




Shift Register
##########################

Shift register shifts the bits within the register left or right

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

::
        
    serial in serial out. 
    parallel in serial out
    serial in parallel out
    parallel in parallel out

because the bits, or vectors are shift with each clock or flop. you can think of it as a delay.
if we were doing serial in serial out. the number of flops chained together results in the total
cycle delay imposed on the signal.
    if the chain is long enough and the final flop is connected to the input of the first flop,
    we create the ring counter. where only one flop is hot.

    the johnson ring counter is similar, but the final flop output is negated/inverted before 
    returning to the input of the first flop.


serial in parallel out shift register, is like a serial to parallel "word" converter.
    maybe like something in a SPI or i2c. as things are sent serail. you'll have to collect bits and then present words
    words can be 8bit 12bit 14bit 24, 32 whatever.. this is what i did for getting ADC values.. which mean
    on the ADC internal/transmit side there is a parallel to serial converter.

from the ADC, there is the DAC which is its complement.. it's receiver uses a serial to parallel converter.

or parallel to serial is like a serializer. you present a 32bit word, and transmit it one bit at a time.
maybe you're word is 64, 128 512 etc..

Counters
##########################

With a register, a clock and a combinational adder, we can create a counter.
The counter is instrumental in sequential design and is found everywhere.
It is how we set specific and/or determine time, how much time has passed.
When to do something, when to do something else. 

Counters can have stop/reset condition.
Or it can be free running/wrap around. depending on your design needs.

::

    BCD counters
    Gray counters
    Ring counters
    One Hot counters
    Johnson counters


Clock Divider
####################################################
Frequency Divider
While we're often taught the inverter flip flop combo for divide by 2.
This is a digital logic/design thing..

You don't want to do this in an FPGA.
What results is either a flip flop with an inverter or logic through LUTs.

What this means is that your clock signal is passing through other components?
and makes it harder to guarantee the cleanliness of your clock signals.

Clock signals are supposed to be clean, minimal skew and minimal jitter.

When it goes through other components before driving flops and registers.
It is harder for the tool to guarantee or create an implementation
that will provide the above.

What you want to do is create a counter that triggers an enable signal.
This signal is used to enable/disable flip flop/registers.


FSM Finite State Machine
##########################

State Machine's give order and organization to sequential tasks.
It is like a controller. The brains. Inside all CPU/processors are some form of FSM.
You may have seen..
    Fetch -> Decode -> Do something -> Store/Update

In this simple example, that could be a 4 state, state machine.

There are two types Moore and Mealy. 
Moore is less. Mealy is more.

Moore outputs depend only on current state of FSM.
Mealy depends on current state and input.


Can be coded/dev using one or two process.
I usually prefer one, because it makes sense in my head.
Sometimes, I'll do two. Or I'll start with two.. and then put it all together later.
In the two process, one is clocked and is responsible for updating the state transitions.
The other process handles the output/combinational logic.

Be weary of the simulation waveforms in the one process.





MAC?
=========================
Multiplay Accumulate
It belongs here because it requires storage, register and registers require clocks.