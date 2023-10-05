************************
Sequential Circuits
************************
Are circuits with memory.
Their output is a function of present and previous input; their is history, memory..
There is feedback.




Data Storage Elements
####################################################

We will introduce storage elements first.
While clock and timing is closely related to sequential circuits,
it is not necessary in order for you to store information/data.

You just need an..
Input, Control and Output.

The storage element can be made from the basic logic gates.

Two basic type, latch and flip flop.


Latches
================================
Keep in mind input and control.

Latch is level sensitive, meaning while the control signal is at some level (say high), it will pass the input value to the output. 
The output tracks the input.
When this level becomes low, the output "latches" the last value seen at the input and holds on to this value, presenting only this value thereafter
while the control remains low.. The input may change at this point, but the output doesn't care.

Conversely, a the latch could have passed the input while the control signal was low, and latch the input value when the control signal went high.
In otherwords, the output tracks the input while the control signal is low.. and latches the last seens input value when the control signals goes high.
While the control signal is high, it doesn't care what is happening at the input.


.. warning::

    there are no actual latch circuit in an FPGA. 
    
If you do implement a latch, it is realized through the flip flops and LUTs; they are generally unwanted in FPGAs.
They probably have their usage, but I have not personally used or even seen them in the complex systems I've worked with thus far. 

.. warning::

    It is a common mistake I've seen in many new grads.
    Inferred Latches are often the result of HDL coding mistakes, from an incomplete if-else statements and/or case statements.
    In either case, not handling all posible outcomes based on the number of inputs.

.. important::
    
    The problem is when people learn HDL, specifically the if else statement, case statement and then the clocked/unclocked process.
    It must not be clear to them. 

    If you are making a combinational circuit with no clock, ALL ELSE STATEMENTS NEED TO BE HANDLED.
    
    If you are making a sequential circuit with a clock, YOU DO NOT NEED TO HANDLE ALL CASES.
    e.g. registers/vectors to hold a value.. or counters.







SR Latch
-------------------------------
DNE, briefly describe now.. not priorirty.


D Latch
-------------------------------
DNE, briefly describe now.. not priorirty.





Flip Flops (FF)
===========================
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
-------------------------------
The ONLY type in an FPGA. 

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




JK Flip Flops
-------------------------------
DNE, briefly describe now.. not priorirty.

T Flip Flops
-------------------------------
DNE, briefly describe now.. not priorirty.




Register
===============================
A collection and ordered set of flip flops.

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


Simple Memory
===============================
A collection and ordered set of registers.


Read-Only Memory (ROM)
================================




Circuit Analysis
##########################


Timing/Clocking
##########################

While all the memory devices above can function/live w/o a clock.
It is when we add timing, things become interesting.

Previously, they just require a "transition." So that does not necessarily 
imply periodic.


Allow us to create more sophisticated circuits, solving more complex problems.

Time and timing is everything in this world..




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


Random Access Memory (RAM)
####################################################

BRAM, 
----------------

SRAM, 
----------------

DRAM 
----------------

SDRAM, 
----------------

CRAM
----------------

FSM Finite State Machine
##########################




MAC?
=========================
Multiplay Accumulate
It belongs here because it requires storage, register and registers require clocks.