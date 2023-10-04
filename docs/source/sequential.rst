************************
Sequential Circuits
************************
Consist of storage elements and clocking. Timing.
Allow us to do more complicated? sophisticated circuits.

Time and timing is everything in this world..



Data Storage Elements
##########################
Two basic type, latch and flip flop.
Latch is level sensitive, meaning while it is at some level (say high), it will pass the input. 



Latches
********************
Latches 
:: 
    
    Inferred Latches are often the result of HDL coding mistakes, such as incomplete if or case statements.
    Vivado synthesis issues a warning for the instance shown in the following reporting example.

    Inferred Tristate buffers are implemented with different device primitives when driving the following:


When the level becomes low, it latches the last value and holds it.
    isn't a latch pretty much a negative edge memory device?
    the issue is that it tracks the input while the level is 

The level input can be a clock or some sort of enable/toggle signal. The point is..
The output sees whatever is at the input for one level and holds the last value for the other level.


there are no actual latch circuit in an FPGA. If you do implement a latch, it is through the flip flops and LUTs.
they are unwanted in FPGAs.
I personally have not had to use them. I am well aware this is a common mistake.

The problem is when people learn HDL, specifically the if else statement, case statement and then the clocked/unclocked process.
It must not be clear to them. 

If you are making a combinational circuit with no clock, ALL ELSE STATEMENTS NEED TO BE HANDLED.
If you are making a sequential circuit with a clock, YOU DO NOT NEED TO HANDLE ALL CASES.


SR Latch
================================


D Latch
================================
isn't a latch pretty much a negative edge memory device?
the issue is that it tracks the input while the level is 




Flip Flops (FF)
********************
A flip flop is edge triggered (can be negative or positive). 
The input is sampled/captured on an edge of a clock or signal. Edge meaning the transition of the signal
which is enable/clock.

Nothing is passed to the output during either level, in comparison to the latch.

I will provide circuit level and explanation of how a latch and flip flop works.
Don't gloss over this shit. So many people do or never made the connection between this. 
Undestanding how it works gives you understanding about setup time, hold time, etc and metastability.

Flip Flops can be thought of as the most basic or lowest unit of memory.
It is what implements the bit, also the most basic/lowest data unit.

While all memory devices can be made from FF in the FPGA, there are hard dedicated sequential components.
Because hard means permanent, their circuitry is tightly coupled when the chip/FPGA is made.
They provide better performance and area. They will always be faster than your LUT based equivalent.


D Flip Flops (DFF)
================================
The ONLY type in an FPGA. 



JK Flip Flops
================================
DNE, briefly describe now.. not priorirty.

T Flip Flops
================================
DNE, briefly describe now.. not priorirty.





Flip-Flops and Registers
:: 
    
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







Register
********************

.. code-block:: vhdl
  :linenos:    

    entity registers_1 is    port(  clr, ce, clk : in std_logic;
                                    d_in : in std_logic_vector(7 downto 0);
                                    dout : out std_logic_vector(7 downto 0)
                                    );
    end entity registers_1;

    architecture rtl of registers_1 is
    begin
        process(clk) is begin
            if rising_edge(clk) then
                if clr = '1' then
                    dout <= "00000000";
                elsif ce = '1' then
                    dout <= d_in;
                end if;
            end if;
        end process;
    end architecture rtl;


Memory
********************

Read-Only Memory (ROM)
================================


Random Access Memory (RAM)
================================

BRAM, SRAM, DRAM SDRAM, CRAM











Circuit Analysis
##########################


Timing/Clocking
##########################


Shift Register
##########################

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



Counters
##########################


FSM Finite State Machine
=========================




MAC?
=========================
Multiplay Accumulate
It belongs here because it requires storage, register and registers require clocks.