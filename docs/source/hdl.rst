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





VHDL
########################################################################################################
mmm.. do i just put basic shit here.. and then add VHDL examples?

you need libraries.
    LIBRARY IEEE;
    USE IEEE.std_logic_1164.ALL;
    USE IEEE.numeric_std.ALL;

    use     USE IEEE.numeric_std.ALL;
    DO NOT USE  std_logic_arith


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


Putting it all together, template!

.. code-block:: vhdl
  :linenos:   
    LIBRARY IEEE;
    USE IEEE.std_logic_1164.ALL;
    USE IEEE.numeric_std.ALL;
    
    entity is port (
            clk : in std_logic;
            rst : in std_logic;
            someout : out std_logic  
    );
    end fpga_top;

    architecture rtl of fpga_top is
        --signal declarations
        --component declarations
    begin
        process (sensitivity) begin
            if () then
            else
            end if;
        end process;

        process (clk) begin
            if () then
            else
            end if;
        end process;
    end rtl;









HDL with emphasis on FPGAs/vendor
##############################################################################
Specific to Xilinx at the moment......
I feel like.. HDL should just be purely HDL like basic syntaxs and templates... with out application.
then as we talk about the different logic operation or circuits...
we'll provide snippets of the HDL code which will synthesize into these circuits.
HDL sprinked across the sections......



I kinda want a deeper dive with the results of the implementation too..
like what it means to use dedicated hardware vs. LUT 

or like the fact that there is only D FF in an FPGA.. other styles FF is just going to be an implementation..
which uses the DFF such that the functionality will be equivalent to another #FF.


Do not asynchronously set or reset registers.
    It becomes preset and clear?

Sequential functionality in device resources, such as block RAM components and DSP blocks, can be set or reset synchronously only.


Do not describe flip-flops with both a set and a reset.
No flip-flop primitives feature both a set and a reset, whether synchronous or asynchronous.
Flip-flop primitives featuring both a set and a reset can adversely affect area and performance.

Avoid operational set/reset logic whenever possible. There can be other, less expensive, ways to achieve the desired effect, such as taking advantage of the circuit global reset by defining an initial content.
Always describe the clock enable, set, and reset control inputs of flip-flop primitives as active-High. If they are described as active-Low, the resulting inverter logic penalizes circuit performance.


You'll want to write code such that it will utilize dedicated hardware when you can
such as....
    RAM: BRAM vs distributed memory.. , 
    DSP, for adding/subtracting larger vectors, multiplying large vectors, FIR filters
    SRL, shift registers


Data is written synchronously into the RAM for both types. 
The primary difference between distributed RAM (made from LUT/FF = LUTRAM) and dedicated block RAM lies in the way
data is read from the RAM. See the following table.

::

    Action  Distributed RAM	    Dedicated Block RAM
    Write	Synchronous	        Synchronous
    Read	Asynchronous	    Synchronous


Generally you will always want to take advantage of RAM, DSP, SRL, MUX? over their LUT equivalents.. better performance.
they are tightly stiched already.. "dedicated hardware/circuits" their area or real estate is already in place. 
if you dont use it you lose it. its already there for you.


Vivado synthesis supports specification of Finite State Machine (FSM) in both Moore and Mealy form. An FSM consists of the following:

A state register
A next state function
An outputs function

Mealy depends on current state and input.
Moore depends only on current state. "More is less."

One hot encoding

Gray state encoding.


know the difference between if-else vs. case statement with regards to implementation.
if-else becomes priority encoder. whatever is at the top of the if else becomes whatever
is closest to the output. or into the register. if the first else case statement is true
it is executed and the others dont matter.

if your control register is for instance 4 bits wide. and you only use one of each bit as the control signal.
that means they are not mutually exclusive.

mutually exclusive means unique. each if-else or case statement is unique. so it doesn't matter if you use 
if-else or case.. because you can create priority or parallel with either one.
it depends how the statements are...
but for good pratice.. if-else is usually used for priority encoding.
case for parallel mux, where decision is mutually exclusive.
mutually exclusive means only one decision or branch can be true at any given time.
show example of code of everything you're saying here. explicitly!!

while case statement is generally used for muxes, improper use can create a priority mux.
if the conditions of an if-else are mutually exclusive, it will create a true mux.
if it is not, it will most likely synthesize a priority encoder.
basically in both case it depends how you write the conditions.



Verilog
##############################################################################
Later..

SystemVerilog
##############################################################################
Later.. as I dont use enough.
