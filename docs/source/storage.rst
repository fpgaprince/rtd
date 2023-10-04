****************************************
Data Storage Elements
****************************************

We will introduce storage first, because a clock is not necessary
in order for you to store information/data.

Input, Control and Output.

The storage element is made from the basic logic gates.
They DO depend on past values though,
and so can be thought of as sequential.



Two basic type, latch and flip flop.


Latches
##########################
Latch is level sensitive, meaning while it is at some level (say high), it will pass the input to the output. 
When this level becomes low, the output "latches" the last value seen at the input.
This value is seen at the output for as long as the level remains (low in our case).


:: 
    
    Inferred Latches are often the result of HDL coding mistakes, such as incomplete if or case statements.
    Vivado synthesis issues a warning for the instance shown in the following reporting example.

    Inferred Tristate buffers are implemented with different device primitives when driving the following:


When the level becomes low, it latches the last value and holds it.
    isn't a latch pretty much a negative edge memory device?
    the issue is that it tracks the input while the level is high.

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
DNE, briefly describe now.. not priorirty.


D Latch
================================
DNE, briefly describe now.. not priorirty.





Flip Flops (FF)
##########################
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
================================
DNE, briefly describe now.. not priorirty.

T Flip Flops
================================
DNE, briefly describe now.. not priorirty.




Register
##########################
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
##########################
A collection and ordered set of registers.


Read-Only Memory (ROM)
================================

