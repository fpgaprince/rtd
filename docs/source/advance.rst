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

Pipeline
=======================
*   Pipelining the design, can increase fmax.
*   Help with Timing
*   Increases latency


Clock Domain Crossing
=======================

Reset 
=======================

Clocking
=======================

Static Timing Analysis
=======================

Timing Closure
=======================



Somewhere
=======================
Duplicate logic to reduce fan out (from a register)
    Helps with timing. easier to route, but increases area.

Logic flattening. Understanding the nature of the function/algorithm from a system level.
Knowing the range of input/output? 
Register balancing.