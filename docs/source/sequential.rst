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
circuits would respond to changes in the input. We wanted it to be definitive, precise.

To do this, the pulse detector/edge detector was introduced.
Its ciruit would preceed the latch.
The resulting circuit became known as the flip flop, an edge triggered device/latch.

Instead of using an enable signal, a clock signal was also introduced/substituted.

The clock signal is periodic signal. It allowed us to..

    synchornize circuits and events with respect to time and each other.

    predetermine/predefine/predict events.

With timing, things become more interesting, allowing us to create more sophisticated circuits, 
and thus.. solve more complex/complicated problems.

    Time and timing is everything in this world..



From this point onward, all sequential circuit implies memory/storage and a clock.

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKABkLCrsEUQAWYoRA8+VKgDMAhgBsAznWqR2nKvzDDBmjVF3T5ipMoCyIQnjwi8-EBl5WbVFNAQsAkqpH2ul0bphIrh4IXAI6PmHC4i4ULADuZvhefBHY5lDxib7phCg2aZbKCRHqwiVwGcVJ-BW5NjXiLGDeeQ5mFm1O1K4A9rqEjmGQ2FCw8Bi5xNjE-AjYYChGY3BkhCGLumIiLH0QA7rqw6PwkBMoUzNzC0snq+tGIHwQ2DuPZoOHfEsQVKxAA" 
            title="DFF" >
        </iframe>
    </div>

---------


.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="600" 
            height="400" 
            src="http://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWEA2aAWB8CcBmSy0AOBBAdkJE0sskoFMBaMMAKAGMQAmNWsZWnr35QoseBAYxknHAjSz8WTnNLlRcVgCcQg8MN2dCFWrJYB5HXD20EYTtZGQWAc0u1DFXTk61fLMKTuPA4+FHwmXLzw1DCsAPY6eiI8WBRIMPCQWKTICNLpXIk4IACWAHYsCfZ8yVkUnNDpYnDZufngHXEArgAuLAAWIMUQTkA" 
            title="WTFFFFF" >
        </iframe>
    </div>

---------



Shift Register
##########################
Previously we introduced the register, a collection of flip flop to hold information.

Shift register shifts the bits/vectors within the register/flip flop left or right.

There are different flavors of shift registers as well as sizes.


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
    similar to serial in serial out, it delays/buffers in the signal. this is no different than your normal/regular register.
    if you hold the information, instead of shifting.. it is just your regular/typical register.


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


.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="560" 
            height="315" 
            src="http://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKDASRQUJDyoBYwPPlChtiPfhN5VC+GSBQhsbDou7hiSwTzBbRkVZw25+IHcshnaLAO7KESkVOFVD97I81LseM3qV3ZT9vYP8wQLtzaWYfENixDy9TcyFLayiLFIswfgz7HLzo3SKghH00PBBCFDNKxOraxXkas2xI+1blJQDuht720JSggat1HmGolCaqaf99IMINWZmGpd0MHnWDKPKezeqNMAOgrh4GQbOFRbwqi6Ur+7Xb8CLCF6ey-Vyzd6qfhpzUJXXqGABK4Dkymwugi0N0imQs2gnBRBhRUSEVASILhIyhCSxihmUw0QKJQNOJhhkKo2Bp+LpNIpJMExBAm3+cK0XMC5iiXXqnOaVUWRwOwuOPBu-yKktKLAAMsVFPwBPwqrU3OAQAAzACGABsAM50aiGZUuEXmDXW7UGk1mpAWlVSm3-E6iB2m80sAAe5k80PIGC4yjV5lVIAAggARWMALgAOsbTQAXFMAIRQABpM2A85AU2mAPYpyA5iusAP8bBtHAclDYZQHOpmADKAFVM8nU3QM8bs3mC5mi8bSymC1OWCX1NVrKlIM3nbB4GR1mHZnOVLOm-PRIIl+bV3B19xN4i9zvNPuBGAjyv4JAzzVnYi9MoZ+AIIQF4fl1AJ7Pps55vj0EAqEAA" 
            title="BCD Counter" >
        </iframe>
    </div>

---------


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


