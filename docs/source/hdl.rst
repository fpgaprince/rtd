************************
HDL
************************
Primary approach to digital logic design in FPGAs and ASICs.
We use it to describe functionality of digital circuits.

The most popular are VHDL, Verilog and SystemVerilog.
VHDL seems to be the preferred language in Defense industry.
Verilog for tech/chip/commerical.. the rest of the world.
SystemVerilog also in tech/commercial, and primarily/intially used for verification. 

    VHDL enforces stricter rules and is typed centric? verbose. wordy, lengthy, less permissive. Strict.
    libraries..

    Verilog is more C like, compact. loosely typed.. Don't have to do component instantiation.

    SystemVerilog, even more compact code. More object oriented like? higher level of abstraction. Helps with verification environment and approaches.

I'm not going to list all the differences under the sun..




HDL with emphasis on FPGAs
====================================
Do not asynchronously set or reset registers.
    It becomes preset and clear?

Sequential functionality in device resources, such as block RAM components and DSP blocks, can be set or reset synchronously only.


Do not describe flip-flops with both a set and a reset.
No flip-flop primitives feature both a set and a reset, whether synchronous or asynchronous.
Flip-flop primitives featuring both a set and a reset can adversely affect area and performance.

Avoid operational set/reset logic whenever possible. There can be other, less expensive, ways to achieve the desired effect, such as taking advantage of the circuit global reset by defining an initial content.
Always describe the clock enable, set, and reset control inputs of flip-flop primitives as active-High. If they are described as active-Low, the resulting inverter logic penalizes circuit performance.



:: Flip-Flops and Registers
    
    FDCE
        D flip-flop with Clock Enable and Asynchronous Clear

    FDPE
        D flip-flop with Clock Enable and Asynchronous Preset

    FDSE
        D flip-flop with Clock Enable and Synchronous Set

    FDRE
        D flip-flop with Clock Enable and Synchronous Reset

    The number of Registers inferred during HDL synthesis might not precisely equal the number of Flip-Flop primitives in the Design Summary section.
    The number of Flip-Flop primitives depends on the following processes:
    Absorption of Registers into DSP blocks or block RAM components
    Register duplication
    Removal of constant or equivalent Flip-Flops
    Basically your estimate and final report may not match because the tool will optimize. You can turn this off though.

:: Latches 
    
    Inferred Latches are often the result of HDL coding mistakes, such as incomplete if or case statements.
    Vivado synthesis issues a warning for the instance shown in the following reporting example.

    Inferred Tristate buffers are implemented with different device primitives when driving the following:

:: Tristates

    An external pin of the circuit (OBUFT)
    An Internal bus (BUFT):
    An inferred BUFT is converted automatically to logic realized in LUTs by Vivado synthesis.
    When an internal bus inferring a BUFT is driving an output of the top module, the Vivado synthesis infers an OBUF.

:: Shift Registers
    
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


VHDL
=========
mmm.. do i just put basic shit here.. and then add VHDL examples?

you need libraries.
template!
entity
    input output
signals
data types
component
process
combinational vs sequential
if else
case
generic






Verilog
=========
Later..

SystemVerilog
==================
Later.. as I dont use enough.
