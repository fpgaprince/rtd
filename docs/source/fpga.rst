FPGA
************************

At the time of writing, focused on Xilinx FPGAs.

What is an FPGA
==================
Field Programmable Gate Arrays (FPGAs) are semiconductor devices with pre-defined available logic blocks and programmable interconnect, referred to as its architecture. 
By developing and defining the relationship between the blocks and interonnections (in other words, the logic), 
we can create tasks, functions and/or algorithms specific to an application. 



Why FPGA
==================
Reconfigurability, parallelism, throughput.
I think we have to say throughput, because there are chips faster, but they don't or aren't capable of taking advantage of parallism.

When FPGA
==================
In general, it depends on your application, performance requirements and cost constraints.

FPGA vs MCU vs CPU vs GPU vs ASIC vs SOC
------------------------------------





FPGA Architecture
=======================
These are the core components in an FPGA, regardless of vendors.

CLB
---------------------

LUT
^^^^^^^^^^^^^^^^^^^^^

Flip Flops (FF)
^^^^^^^^^^^^^^^^^^^^^

Shift Registers (SRL)
^^^^^^^^^^^^^^^^^^^^^

MUX
^^^^^^^^^^^^^^^^^^^^^

Carry Logic
^^^^^^^^^^^^^^^^^^^^^



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
=======================
As the technology advanced and they're able to fit more onto a die, FPGAs began absorbing various hardware it would often interface with, making them internally dedicated.
While they are common these days, not every FPGA family or model will have it. Thus listed here.



DSP (extra)
---------------------
While pretty common these days, I'll leave it here.


XADC (extra)
---------------------

Tranceivers (extra)
---------------------

PCIe (extra)
---------------------

Hardprocessor
---------------------
As appose to soft processor or soft core IP. They're able to fit a CPU on the same die as the FPGA, reducing external pin interconnections. 


