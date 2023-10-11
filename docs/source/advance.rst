Advance
***********************

Speed vs. Latency





Throughput 
    data or bits per cycel.
    sequential vs. pipelined.. shared resources vs. duplicating resources (increases area)

Latency
    Cycle count.
    Remove pipeline registers reduces latency, because each register in the path introduces an additional cycle.
    Harder to meet timing

Speed/Timing
    Pipeline the design. in otherwords.. Adding register layers.. 
        Pipelining increase fmax. Decrease delay requirements from register to register.
    Parallelize the design. Analyze function/algorithm, break up into smaller chunks/operations that can be done in parallel.

Area
Power

FIFO
=======================

Pipeline
=======================
*   Pipeline the design, can increase fmax.
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