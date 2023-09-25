FPGA
************************

At the time of writing, focused on Xilinx FPGAs.

What is an FPGA
==================
Field Programmable Gate Arrays (FPGAs) are semiconductor devices with prearranged digital circuits and programmable interconnects. 
By developing and defining the relationship between theses blocks, interconnections and optionally, dedicated hardware, 
we can create various tasks, complex functions and/or algorithms specific for an application. 



Why FPGA
==================
Parallelism and reconfigurability are major highlights/features for using an FPGA.

*   Parallelism allows us to increase data throughput per clock period.. 
    In a sequential system (MCU/CPU), one generally tries to increase the clock rate.

*   Reconfigurability allows us to re-purpose the same FPGA for different applications.
    This feature is useful for prototyping as well as creating a flexible product platform in comparison to ASICs.


When FPGA
==================
In general, it depends on your application, performance requirements and cost constraints.

FPGA vs MCU vs CPU vs GPU vs ASIC vs SOC
-------------------------------------------------------------------

CPU and MCU are similar in there sequential nature when executing a program. 
MCU may require less resource in terms of memory because you dont need an OS.
I think programming at the high level is easier, you dont have to be as concerned about how the hardware works.
Generally, a faster clock rate will execute your code faster.


GPU exploit parallelism like FPGA. At the moment it is not clear to me which is better.
If we were to say we wanted to do some image/video processing application. GPUs are great for such work,
and FPGAs can be developed for specific processing tasks.. so where is the cross over?

ASICs are specific to your application. They make use of the entire chip, there is no excess gates/hardware in the chip.
Everything serves a purpose. An FPGA gives you building blocks, and it is up to you to determine what to use.
Most of the time you never use up 100% of the available resources. It isn't common practice to do that.
FPGAs are more forgiving though, in terms of you can reconfigure if there is a flaw in the design.
An ASIC would require a respin, costing significant amount of money.



FPGA Architecture
=======================
These are the core components in an FPGA, regardless of vendors. They are the available digital circuits/hardware avaialble to us.

Configurable Logic Blocks (CLB)
------------------------------------------
Generally consists of the below components. The number of each, how they are placed and their IO are vendor specific.
Each vendor has their own rationale for choosing implementing their architecture. 



Look up Table (LUT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Flip Flops (FF)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multiplexer (MUX)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Carry Logic (CL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Shift Registers (SRL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IO
---------------------

Interconnect
---------------------

Distributed RAM
---------------------

BRAM
---------------------

Clock MGMT
---------------------


FPGA Dedicated Hardware
=================================
As the technology advanced and they're able to fit more onto a die, FPGAs began absorbing various hardware it would often interface with, making them internally dedicated.
While they are common these days, not every FPGA family or model will have it. Thus listed here.



DSP (extra)
-------------------------------
While pretty common these days, I'll leave it here.


XADC (extra)
-------------------------------

Tranceivers (extra)
-------------------------------

PCIe (extra)
-------------------------------

Hardprocessor
-------------------------------
As appose to soft processor or soft core IP. They're able to fit a CPU on the same die as the FPGA, reducing external pin interconnections. 




Organize
Xilinx organizes their CLBs into two types, SLICEM and SLICEL.
SLICEL (L=logic)
SLICEM (M=memory) - distributed memory/ram or shift register