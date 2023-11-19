Advance
***********************

In the way you write HDL..

Speed
    Throughput 
        data or bits per cycel.
        sequential vs. pipelined.. shared resources vs. duplicating resources (increases area)

    Latency
        Cycle count.
        Remove pipeline registers reduces latency, because each register in the path introduces an additional cycle.
        Harder to meet timing

    Timing
        Pipeline the design. in otherwords.. Adding register layers.. 
            Pipelining increase fmax. Decrease delay requirements from register to register.
        Parallelize the design. Analyze function/algorithm, break up into smaller chunks/operations that can be done in parallel.
        Reducing logic level/stages.

Area
    not pipelining. sharing logic resources. remove duplicate logic. use/add control logic, state machine to share sources.
    there are different types of resources. there are the actual FF and LUT that are used to implement your combo logic.
    there are LUT made operations (ie. adder, multiplier, shift) that can be shared, 
    some resources can be pull up to a higher level/hierarchy and be shared across modules, from a global perspective. 
    so resource at the 'module' or component level like clocks and timers..
 
    you do not need a reset for every flip flop or sequential element, it depends what you are doing.
        for instance, you dont need to reset a shift register, if you know you're not going to get valid data until a later time.
        and the circuit/or whatever down stream knows this too. the shift will eventually shift out the initial values set by the FPGA.
        or the garbage input until you get valid.
    
    to use dedicated shift registers, you cannot have a reset signal, they dont have a reset signal. if you do, the tool will
    try to (synth/imp -> syn/imp -> symp) LUT+FF based shift registers. which will take up more resources/area than using dedicated hw.
    more area.

    
Power

FIFO
=======================
    This basic sequential circuit/component/module.. is increadibly important in many application. 
    It was probably first introduced in data structure with queue and stack alogorithm/data storage.
    Its write/read functionality are quite straightforward in nature when everything is within the same clock domain,
    But when the write is in one domain and the reads are in another, it complicates things a little, a little in the sense that
    is it a known issue, we are aware of it, and a way to handle it has been developed. The different domains complicate things
    because we need to track the pointer, which means we need to pass the pointer value back and forth when a write or a read 
    occurs.
    We'll keep it brief here and discuss it more in the CDC section.

Pipeline
=======================
*   Pipelining the design, can increase fmax.
*   Help with Timing
*   Increases latency
*   Increases area

Clock Domain Crossing
=======================
    What is a clock domain. A domain is basically what clock all the registers or set of registers/components/modules are clocked with.
    You have clock domain which are multiples/factors of the other. So they are synchronous.
    You have completely different clock domain in which the two are asynchronous, meaning neither have information on the other.
    The information, meaning the phase relationship between the two or more clock domains. 
    Meaning you can have two domains of the same frequency.. but if the phase information/relationship is unknown,
    you cannot guarantee the setup/hold time requirements for either domain clock edges to be met.
    Thus metastability is probable.

    Discuss metastability here again.

    Double Flop. Double Register. Synchronize Flip Flop. All the same, diff names.
    FIFO
    Phase Control, by using the FPGA's PLL/DLL, we can have multiples/factors of an input clock. The FPGA can monitor or determine the skew across the FPGA
    with finer granularity? or control. The jitter will not be an issue? because it is internal and pre-defined in the spec of the PLL/DLL.

    Create CDC blocks/modules to organize all CDC techniques. Have these modules between the two modules clock by different clocks. Partitioning.

Slower to faster
-----------------------

Faster to Slower
-----------------------


Reset 
=======================

    Dedicated BRAM and DSP should be synchronously reset because these are dedicated HW in the FPGA. They were 'fabricated' that way, so in order
    to use them correctly.. their resets should be syncrhronous.

    SRL, no reset. Likewise.. frabricated with NO reset pin/input. Therefore if you try to add one, the tool will synthesize extra surrounding logic
    to implement what you, the designer, wants.

    Using set/reset pins can prevent combinatorial logic optimization.

    Asynchronous Reset vs. Synchronous Reset
    Advantage/Disadvantages
    Asynchronous can happen anytime, you dont care about the clock edges. Synchronous is like all the other signals we've dealt with,
    the clock edge we register the reset signal.
    
    The problem with async reset is in releasing the reset signal, starting operation, in relation to the clock. The point is, there is no relation. So when it is released, 
    all the signals in the FPGA start going to work without knowledge of the clock, which creates a recipe for disaster in a synchronous design.
    When we dont have an idea of the clock periods, or edges, we cannot guarantee our setup/hold times, we that is not guaranteed,
    metastability is highly probable.

    The problem with sync reset, is the requirement for a clock. IF for some reason we lose the clock we wont register a reset. Or if logic is spread out through the FPGA
    such that the propagation of the clock is not equal in different areas, we wont reset all at the same time. This will create an uncertainty
    in our reset state/condition.

    So async issue is the end, and sync's issue is the beginning. To combat this, what is called 'async assertion, sync de-assertion' has been developed/created.
    Async assertion takes care of sync's beginning of requiring a clock to reset, and the sync de-assertion handles, the end of the async to ensure everything
    starts in a known state/value/ at the same time.

    Don't mix async and sync resets, because FF and registers are not fabricated in this way, you will create additional surrounding logic to implement such functionality.

    In regards to fully sync reset and asyc+sync, you need to always synchronize the reset signal the whatever clock domain it is being applied to. 



Clocking
=======================

Static Timing Analysis
=======================

Everything online always tells you.. setup time is the time data needs to be steady at the input pin of the flip flop before arrival of clock.
And yes that is true, but they not many discuss why this is so. I want to do it here. 
I add the equations later.
In order to understand why, we have to take a step back/do a deeper dive into..
what is the DFF/register used by the FPGA.

    I thik knowing why something is the way it is helps us better understand what or how.

    1. My experience with FPGA registers have all been with DFF.
    2. DFF in FPGAs are made with CMOS technology, not TTL.
    3. There are numerous ways to implement a DFF. 
        I will be referencing/using the Master-slave latch to speak of the edge triggered D flip flop.
        Which consists of CMOS inverters and transmission gates.


    4. The time for the master to latch the data IS the SETUP TIME.
    5. The shutting off of the first latch/TG is the HOLD TIME.
    6. The time for the input to traverse the inverters to the output is the CLOCK TO Q time.

In the diagram below, I have decreased the inverters slew rate (takes longer to change voltage, go from one state to the other), 
which increases the setup time.
which cuts into the total period and decreases and limits the max frequency.

In other words..

    for a given frequency, if i keep decreasing the slew rate, at some point i wont be able to latch data correctly.

In other words..

    for a given slew rate, if i keep increasing the frequency, eventually the period will be too short and i wont change in time or latch the data correctly!

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWEBOWkwHYwGYeIExgAcERGISCkFApgLRhgBQA7iACztHhj4dch87apCYBJChgBsPPlOGyoUNPD4JWgotyHV8WkNmwzRAJXDSDRkPMsyIaotAQz8TwW5FOmAGXN3e1uyK1BAAZgCGADYAzjQUUEwAHhTcGEEYSBjkQUIgACIa7GD+fJzcjHyioZrlFnrleih2HrD4TNX1HNr6yDLI5GAtkG1s+M6K+Bh8FQmjUxPzvbMGkEFL2KvBGhtBvNw7W2wHM0Uly2Nn+Lkzokf41EudS6IA5oLjmC4fyJUJZtj3JoGQHFJTUBRIETKdSjD6NC5+c7zPaCZEBW41cDwuHcUQST4Ta7o5TwOBqcSIwwuXJUsEqMDIRlM5ks7jqCQHWnYBB8WmeeAMllCpls7Y82wGKT7KwYya8qxXIJ87abWmdZVHKUSnnS4waHXvGTsR7jDEIAII818HTLY1fI3rTamChSXS5ZwhV1gjjUSF09RvO0rIJBgFQs1exUUeG5DFBm1lQQKM2cJO+urJ-Wpy3ZzNsBDZ925kT6i0Qi2xwqPcvWzPVA0Eg1R-rgIZteuNA5N8ZLQaQ1oU+S6CEZ8MqMkUQqgmYICw3fWdqwGg6y-Q2zoE1e1GQNiwYoy6yXcAT7rUCTonjRDtPWcY2jFSO8KR9nB8fAJEAFbABG4FTDBkDBDAMRkEl-NIkAA8BsCIXlQIxXgbBmXhe3RDREJyBQMMOLFzyw-AbHvDR+iNbgiCWS82BIo8UAsSiQHIuw5xwJi9TYRibw4zd0JYmjGCsFd0Mgd9pmIXY0PxIRtCwsSb35UlyWqfiZGOXiEV7Nt2h4KwCWUwRchbPsSRGHhNhtCphxLNgLJvGyowQsBxSjRgnLzHgnPfVyrPc2sQlkojrLAMysOElw3MYLVnLUys3kYVVNjipVARLMwIu0IktWKcMfXiMcYVMnJ33ioIHMBBE7PCtSisKtjaJUzLeIPZYuMaIgkMaDEtBCVqiD8yoNDa3ZWqQvcmDMH5uCWCbwGMJQIW9GAAwYkaZEG8AfjBYjGiWDjngGpCPy-ecqICZDhnE-qTumbbTrQq6gWQW7LoY3rFC6oFOoOvh3vnaoOIEXa+gGTS-t7CwWsm5p+2GISiWmUKcI4m0OI1XDylOgiLoSfFZOQqTghJBTJ2shGzqfEtf14PgGGE6DQPYK4EmSRCQAYTBzGQVnGBDJN8gAHWiAAxQWkj-GQ6HwTmjGwVmCI4XmAGEAFkAHkAGUBaV8JogAFxoAAnAXvHCHWAGMAAtRYyagJcmgtZaQTCQGV9WBbVyJwgANxoI2TYtjQ5QlQOmtleYmuokOA7DhV9FR5crBRmUrxkuQRKZv8cBQGWwHYXAgSdgBFCkULOFi+rpUlhmJ6CvWQhmsdEJW-zhv99Budx1GSBAZdwCBQNwHncgV7wAGkmAAewMGa5qCmXofgEjnDGJReQMCf5dBcFZ9y8dF6kZfdHl7B18zzeOG36GD8EaC18nuLp63qv+wgEImBgqfBYgGWgioG2IEF-WNAACOABXGgAA7U2ABPJgQA" 
            title="Ring Counter" >
        </iframe>
    </div>

---------
    

Timing Closure
=======================



Somewhere
=======================
Duplicate logic to reduce fan out (from a register)
    Helps with timing. easier to route, but increases area.

Logic flattening. Understanding the nature of the function/algorithm from a system level.
Knowing the range of input/output? 
Register balancing.

Clock gating
===============
    No clock gating in an FPGA. you just use enables. You enable/disable a flip flop/register.

Division
====================


Floating Point 
====================


