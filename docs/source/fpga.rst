
************************
FPGA
************************

At the time of writing, focused on Xilinx FPGAs.


What is an FPGA
##########################
    Field Programmable Gate Arrays (FPGAs) are semiconductor devices, integrated circuits, with configurable logic(circuit) blocks, programmable interconnects
    and some dedicated. 
    By developing and defining the relationship between theses blocks, interconnections and optionally, dedicated hardware, 
    we can create various tasks, complex functions and/or algorithms specific for an application. 



Why use an FPGA
##########################
    Parallelism and reconfigurability are major highlights/features for using an FPGA.

    *   Parallelism allows us to increase data throughput per clock period.. 
        In a sequential system (MCU/CPU), one generally tries to increase the clock rate.

    *   Reconfigurability allows us to re-purpose the same FPGA for different applications.
        This feature is useful for prototyping as well as creating a flexible platform in comparison to an ASIC.

    What I mean by not unique is that..
    Parallelism has been exploited by GPUs for ages and is nothing new  
    Reconfiguring is no different than recompiling program and repurposing an MCU/CPU.


When to use an FPGA
##########################
    In general, it depends on your application, performance requirements and cost constraints.

    Application and complexity
    Performance and as result, power
    Cost

FPGA vs MCU vs CPU
========================

    CPU and MCU are similar in there sequential nature when executing a program. 
    MCU may require less resource in terms of memory because you dont need an OS.

    I think programming at the high level is easier, you dont have to be as concerned about how the hardware works.
    Generally, a faster clock rate will execute your code faster.

FPGA vs GPU 
========================
    GPU exploit parallelism like FPGA. At the moment it is not clear to me which is better.
    If we were to say we wanted to do some image/video processing application. GPUs are great for such work,
    and FPGAs can be developed for specific processing tasks.. so where is the cross over?

FPGA vs ASIC
========================
    ASICs are specific to your application. They make use of the entire chip, there is no excess gates/hardware in the chip.
    Everything serves a purpose. An FPGA gives you building blocks, and it is up to you to determine what to use.
    Most of the time you never use up 100% of the available resources. It isn't common practice to do that.
    FPGAs are more forgiving though, in terms of you can reconfigure if there is a flaw in the design.
    An ASIC would require a respin, costing significant amount of money.

SOC
========================
    Essentially a CPU combo'd with other processors, can be FPGA, network, DSP.
    Zynq 7000, uses A9
    MPSoC, RFSoC,  and so does Altera's stratix use A53
    and Versal uses the ARM Cortex A72



FPGA Architecture
##########################
    These are the core components in an FPGA, regardless of vendors. They are the available digital circuits/hardware avaialble to us within the FPGA.
    Whatever we code up in HDL and synthesize/implement.. gets mapped to these digital components. I list our the common if not all here.
    We will talk about digital logic and digital design in the broad/general sense, but i will also emphasize whether or not they are applicable to FPGAs.
    

Configurable Logic Blocks (CLB)
================================================
    A CLB is an organization of the below components. The number of each, how they are placed and their IO are vendor specific.
    Each vendor has their own rationale for choosing implementing their architecture. 

    CLB is further divided into slices. There is SLICEL and SLICEM
    
    Organize
    Xilinx organizes their CLBs into two types, SLICEM and SLICEL.
    SLICEL (L=logic)  - 4LUT,8FF -> CLB = 2SLICES -> 8LUT 16FF
    SLICEM (M=memory) - distributed memory/ram or shift register
    LUT, LUTRAM, CARRY, MUX, SRL. Storage (FF)


Look up Table (LUT)
------------------------------------------
The LUTs inside an FPGA are implemented as asynchronous ROMs (i.e. ROMs without a clock): they are actual SRAM based.
SRAM meaning that they are volatile and will be wiped/reprogrammed when rebooted.
At configuration time, the RAM is written to with the BIT file (often stored elsewhere), defining the logical function the FPGA needs to perform.
The inputs are treated as address lines, and the output usually has the width of one bit or two bits is the "content" at that address line.

The number of inputs to these LUTs is 4 or 6 in almost all FPGAs in the market, so the number of memory cells in each LUT is either 16 or 64.
can be 2-6. The input determine the combinatorial function it can represnt. LUT2 for example, can represent all the basic 2 input gates, AND OR XOR.

    LUT1-6

Carry Logic (CL)
------------------------------------------
    CARRY8

Multiplexer (MUX)
------------------------------------------
    MUXF7/MUXF7/MUXF9

Shift Registers (SRL)
------------------------------------------
    SRL16/32

Storage Elements 
================================================

Registers/ Flip Flops (FF)
------------------------------------------
    FDCE FDPE
    FDRE FDSE

Distributed RAM (LUTRAM)
------------------------------------------

BRAM
---------------------
    RAM18/36
    FIFO18/36
    URAM




IO
================================================

Interconnect
================================================

Clock MGMT
================================================


FPGA Dedicated Hardware
================================================
    As the technology advanced and they're able to fit more onto a die, FPGAs began absorbing various hardware it would often interface with, making them internally dedicated.
    While they are common these days, not every FPGA family or model will have it. Thus listed here.



DSP (extra)
-------------------------------
    While pretty common these days, I'll leave it here.

In general, the DSP slice supports both sequential and cascaded operations due to the
dynamic OPMODE and cascade capabilities. Fast Fourier Transforms (FFTs), floating
point, computation (multiply, add/sub, divide), counters, and large bus multiplexers are
some applications of the DSP slice. 

The DSP blocks within the AMD devices can perform many different functions, including:

Multiplication
Addition and subtraction
Comparators
Counters
General logic

DSP58 slice registers within AMD devices contain only resets, and not sets. Accordingly, unless necessary, do not code a set (value equals logic 1 upon an applied signal) around multipliers, adders, counters, or other logic that can be implemented within a DSP58 slice.

DSP58 blocks use a signed arithmetic implementation. AMD recommends code using signed values in the HDL source to best match the resource capabilities and, in general, obtain the most efficient mapping. If unsigned bus values are used in the code, the synthesis tools may still be able to use this resource, but might not obtain the full bit precision of the component due to the unsigned-to-signed conversion.

If the target design is expected to contain a large number of adders, AMD recommends that you evaluate the design to make greater use of the DSP58 slice pre-adders and post-adders. For example, with FIR filters, the adder cascade can be used to build a systolic filter rather than using multiple successive add functions (adder trees). If the filter is symmetric, you can evaluate using the dedicated pre-adder to further consolidate the function into both fewer LUTs and flip-flops and also fewer DSP slices as well (in most cases, half the resources).





XADC (extra)
-------------------------------
    SYSMON

Tranceivers (extra)
-------------------------------
    GTH/GTY


Hardprocessor
-------------------------------
    As appose to soft processor or soft core IP. They're able to fit a CPU on the same die as the FPGA, reducing external pin interconnections. 
    ARM Cortex-A9 and A53 seems to be the common one found in current FPGAs from both xilinx and altera.
    There is also the Cortex-R5.
    This is pretty huge.
    ARM processors are RISC ISA based. Your Intel i5 i7 i9 and AMD x whatever are based on x86 ISA
    Your apple is based on ARM architecture, so RISC.
    Anything ARM is RISC. they were the contrasting philosophy/idea/approach of x86, CISC ISA processors.
    ARM = Advanced RISC Machines


PCIe (extra)
-------------------------------

Soft Processor
================================================
Since I mentioned hard processors and all that i should also talk about the soft processors for the FPGA.
These are processors IP cores each vendor have developed for their FPGAs.
Xilinx has the microblaze and Altera has the NIOS. They are both based on RISC V ISA.
while they are RISC and so are ARM. These soft processors were developed in house by these vendors using
the RISC ISA, which is avaialabe to everyone. They are developed in house and catered to their FPGA.
Whereas ARM takes the ISA and creates a processor and creates various flavors of processors/architecture.
Different product lines and families. Different performance, size, cost.
Which means you can buy either a pre made fabbed ARM chip, or buy/license the architecture and use it in your chip.
I just read that ARM also has soft processors IP cores you can instantiate in your FPGA.. very much like
the Microblaze, I dont know the difference at the moment, or which is better and or for what.


Metastability
================================================
I want to introduce this concept/issue early on. It should be fundamental and designers should be aware of it.
It's not even an advance concept.. but from many of my reading.. it is glossed over, or very little attention
is given to it. I guess.. for the most part or for small designs.. you can get by without knowing or dealing with.
Likewise with static timing analysis and timing closure.. but they are all essential parts? of FPGA development.
And are fundamental to it.
We may decompose the advance chapter and introduce it early on?




