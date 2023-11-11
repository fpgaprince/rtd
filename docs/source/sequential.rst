************************
Sequential Circuits
************************

Sequential circuits are circuits in which the output or result depend 
on the present/current input as well as the past/previous input.
This implies that the circuit has some form of memory or history..
It has the ability to track the inputs.

This is essentially accomplished through feedback.

Circuits with feedback were introduced in the previous
chapter, starting with the latch and building up to flip flops. 

These circuits were the simplest form of memory, 
enabling us to store/hold a digital bit, state or voltage.

They are fundamental building blocks for sequential circuits and systems.

flips are used to create registers and array of registers, roms and ram.



Circuit Analysis
##########################
Formal/Mathematical part..



Clocking the Control Signal
####################################################

We define sequential circuits simply as circuits with memory.
These feedback circuits only need control/enable signals to function/operate
and only so on their signal level. They are level senstive.

Over time there was an incentive for minimizing the time/window in which these
circuits would respond to changes in the input. We wanted it to be definitive.

To do this, the latch was proceeded by a pulse detector.
The resulting circuit became known as an edge triggered devices, the flip flop.

And instead of using an enable signal, a clock signal was introduced/substituted.
The clock signal is periodic and consistent?

It allowed us 

    We can synchornize multiple events.

    We can predetermine when things happen.

    We can expect things to happen at very specific times. We can predict.

    With a clock we establish a sense of time.

It is when we add timing, things become interesting.
It allow us to create more sophisticated circuits, solving more complex problems.



    Time and timing is everything in this world..



From this point onward, all sequential circuit implies memory/storage and a clock.
The smallest memory element, being the flip flop. D FF to be specific.




Shift Register
##########################

Shift register shifts the bits/vectors within the register left or right

serial in serial out
******************************************
because the bits, or vectors are shift with each clock or flop. you can think of it as a delay.
if we were doing serial in serial out. the number of flops chained together results in the total
cycle delay imposed on the signal.


parallel in serial out
******************************************
 which mean on the ADC internal/transmit side there is a parallel to serial converter.
or parallel to serial is like a serializer. you present a 32bit word, and transmit it one bit at a time.
maybe you're word is 64, 128 512 etc..

serial in parallel out
******************************************
serial in parallel out shift register, is like a serial to parallel "word" converter.
maybe like something in a SPI or i2c. as things are sent serially. you'll have to collect bits and then present words
words can be 8bit 12bit 14bit 24, 32 whatever.. this is what i did for getting ADC values.. which mean
on the ADC internal/transmit side there is a parallel to serial converter.

from the ADC, there is the DAC which is its complement.. it's receiver uses a serial to parallel converter.

parallel in parallel out
******************************************
similar to serial in serial out, it delays/buffers in the signal.


Shift Registers
:: 

    Vivado synthesis implements inferred Shift Registers on SRL-type resources such as:

    SRL16E
    SRLC32E

    Depending on the length of the Shift Register, Vivado synthesis does one of the following:

    Implements it on a single SRL-type primitive
    Takes advantage of the cascading capability of SRLC-type primitives
    Attempts to take advantage of this cascading capability if the rest of the design uses some intermediate positions of the Shift Register


sequence detection/detector
******************************************
taps are synonymouse with shift registers andor registers sequentially related to each other.
taps is terminology for having a way to inspect the data in between.
normally you just have the input and output, but you can 'tap' the signals in between.
if you have 4 registers, you can have 3 taps. basically with N registers, up to N-1 taps.



Counters
##########################


The counter is instrumental in sequential design and is found everywhere.
It is how we set specific and/or determine time, how much time has passed.
When to do something, when to do something else. 

Counters can have stop/reset condition.
Or it can be free running/wrap around. depending on your design needs.

BCD counters
******************************************
With a register, a clock and a combinational adder, we can create a counter.
    This is the typical one you'll use and see to create counter enables. and timing event to happen/occur.


Gray counters
******************************************
    I've only used this for clock domain crossing FIFOs.

Ring counters (one hot counter)
******************************************
I think this is the simplest form of a counter. It only requires registers.
    with a chain of registers, final flop is connected to the input of the first flop,
    we create the ring counter. where only one flop is hot.

Johnson counters
******************************************
    the johnson ring counter is similar, but the final flop output is negated/inverted before 
    returning to the input of the first flop.

    i've yet to use these..





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