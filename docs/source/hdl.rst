########################
HDL
########################
Primary approach to digital logic design in FPGAs and ASICs.
We use it to describe functionality and/or behavior of digital circuits.
It is how abstract, design and develop at a higher level.

The most popular are VHDL, Verilog and SystemVerilog.
VHDL seems to be the preferred language in Defense industry.
Verilog for tech/chip/commerical.. the rest of the world.
SystemVerilog also in tech/commercial, and primarily/intially used for verification. 

    VHDL enforces stricter rules and is typed centric? verbose. wordy, lengthy, less permissive. Strict.
    libraries..

    Verilog is more C like, compact. loosely typed.. Don't have to do component instantiation.

    SystemVerilog, even more compact code. More object oriented like? higher level of abstraction. Helps with verification environment and approaches.

I'm not going to list all the differences under the sun..




I feel like.. HDL should just be purely HDL like basic syntaxs and templates... with out application.
then as we talk about the different logic operation or circuits...
we'll provide snippets of the HDL code which will synthesize into these circuits.
HDL sprinked across the sections......

The HDL language is expansive? but for FPGA synthesis, you can only use a subset of the language.
The language can be used for both development and verification. 
Alot of the verification syntax/HDL is not synthesizable.
We will first focus on synthesizable and return for test bench, validation, verification.

******************************
VHDL
******************************

just some of the basic stuff... examples and templates.

libraries and use
#########################

.. code-block:: vhdl
  :linenos:    

    LIBRARY IEEE;
    USE IEEE.std_logic_1164.ALL;
    USE IEEE.numeric_std.ALL;

.. warning::

    DO USE     
        IEEE.numeric_std.ALL;

    DO NOT USE  
        IEEE.std_logic_arith


entity
#########################
this is how we abstract digital components and modules.
this is how you encapsulate functionality, or create black box.

.. code-block:: vhdl
  :linenos:   

    LIBRARY IEEE;
    USE IEEE.std_logic_1164.ALL;
    USE IEEE.numeric_std.ALL;
    
    entity fpga_top is port (
            clk : in std_logic;
            rst : in std_logic;
            somein : in std_logic;
            anotherin : in std_logic_vector(7 downto 0);
            someout : out std_logic;
            anotherout : out std_logic_vector(15 downto 0)      -- notice no ';'
    );                                                          -- notice ';'
    end fpga_top;                                                         
    
    architecture rtl of fpga_top is

        --signal declarations
        --component declarations

    begin

        -- RTL body.

    end rtl;

in the following, which can be in some other file, we create more entities.
i usually keep one entity per file for organization, but here i am just listing two

.. code-block:: vhdl
  :linenos:   

    LIBRARY IEEE;
    USE IEEE.std_logic_1164.ALL;
    USE IEEE.numeric_std.ALL;
    
    entity some_component is port (
            clk : in std_logic;
            rst : in std_logic;
            someout : out std_logic  
    );
    end some_component;

    architecture rtl of some_component is

        --signal declarations
        --component declarations

    begin

        -- RTL body.

    end rtl;

    -- just for example...
    entity another_comp is port (
            clk : in std_logic;
            rst : in std_logic;
            someout : out std_logic  
    );
    end another_comp;

    architecture rtl of another_comp is

        --signal declarations
        --component declarations

    begin

        -- RTL body.

    end rtl;    

architecture vs structure vs behavior
*********************************************



component
#########################

1.  you create your component with entity directive? (see entity section)
2.  then you declare its usage, in another entity or testbench. 
3.  then you instantiate the component where it is used and label it.
4.  map port signals

re-using the fpga_top entity we created earlier.. 

.. code-block:: vhdl
  :linenos:   
    
    LIBRARY IEEE;
    USE IEEE.std_logic_1164.ALL;
    USE IEEE.numeric_std.ALL;
    
    entity fpga_top is port (
            clk100 : in std_logic;
            clk150 : in std_logic;
            rst : in std_logic;
            dout1 : out std_logic;
            dout2 : out std_logic  
    );
    end fpga_top;
    
    architecture rtl of fpga_top is
        --signal declarations

        -- 2. component declarations        -- for code readability, can create a separate component.vhd file and declare them all there.
                                            -- actually, i'd recommend doing so, it prevents this section from becoming unnecessarily long
        component some_component is port (
            clk : in std_logic;
            rst : in std_logic;
            someout : out std_logic  
        );
        end component some_component;

        component another_comp is port (
            clk : in std_logic;
            rst : in std_logic;
            someout : out std_logic  
        );
        end component another_comp;

    begin
        --  3. component instantiation
        DUT1_label : some_component port map (
            clk => clk100,
            rst => rst,
            someout => dout1
        );

        DUT2_label : another_comp port map (
            clk => clk150,
            rst => rst,
            someout => dout2
        );        
    end rtl;


By instantiating components within other entities, you create a hierarchy and organization for your design.

.. note::

    Notice => used to assign signals to ports. verus <= to assign values or signals to signals!


Object Types
#########################
    
    signals
    
    variable
    
    constants

Signals
*********************************************
These are the common ones I've used.

    std_logic
    
    std_logic_vector
    
    unsigned
    
    signed
    
    integer
        range
        natural 0 to 
    
    natural
    
    arrays

    custom

Assignment/Assigning
*********************************************
    
    <= signal assignment
    
    := variable assignment, signal initialization.


Conversions and Cast/Casting
*********************************************

    first, make sure you are using IEEE.numeric_std.ALL

    second, the ones to take notice of are the integer related ones.
    because the integer uses the system bit rep, most likely 32bits.
    we'll need to specify how many bits/registers we want to use 
    to represent a numeric value when entering the circuit/hw/bit level.


TO UNSIGNED
=====================================


integer to unsigned
------------------------------------

.. code-block:: vhdl
  :linenos:   

    unsigned_signal <= to_unsigned(integer_signal, desired_unsign_length);

signed to unsigned
------------------------------------

.. code-block:: vhdl
  :linenos:   
    unsigned_signal <= unsigned(signed_signal);

std_logic_vector to unsigned
------------------------------------

.. code-block:: vhdl
  :linenos:   

    unsigned_signal <= unsigned(std_logic_vector_signal);




TO SIGNED
=====================================


integer to signed
------------------------------------

.. code-block:: vhdl
  :linenos:   

    signed_signal <= to_signed(integer_signal, desired_sign_length);


unsigned to signed
------------------------------------
keep in mind the needed extra bit for the sign!

.. code-block:: vhdl
  :linenos:   

    signed_signal <= signed(signed_signal);


std_logic_vector to signed
------------------------------------

.. code-block:: vhdl
  :linenos:   

    signed_signal <= signed(std_logic_vector_signal);




TO STD_LOGIC_VECTOR
=====================================

integer to std_logic_vector
------------------------------------

.. code-block:: vhdl
  :linenos:   

    -- only positive integers
    SLV_signal <= std_logic_vector(to_unsigned(integer_signal, unsigned_length));
    
    -- positive and negative integers
    SLV_signal <= std_logic_vector(to_signed(integer_signal, signed_length));


unsigned to std_logic_vector
------------------------------------

.. code-block:: vhdl
  :linenos:   

    SLV_signal <= std_logic_vector(unsigned_signal);

signed to std_logic_vector
------------------------------------

.. code-block:: vhdl
  :linenos:   
    
    SLV_signal <= std_logic_vector(signed_signal);




TO INTEGER
=====================================
i dont think i ever really use this.. maybe in verification?


std_logic_vector to integer
------------------------------------
but remember whether signed or unsigned, it is just a set of registers,
a vector.. signed/unsigned is just how we interpret the vector.
we need to tell the system how to interpret our SLV.

.. code-block:: vhdl
  :linenos:   

    int_signal <= integer(unsigned(std_logic_vector_signal));

    int_signal <= integer(signed(std_logic_vector_signal));

unsigned to integer
------------------------------------

.. code-block:: vhdl
  :linenos:   

    int_signal <= integer(unsigned_signal);


signed to integer
------------------------------------

.. code-block:: vhdl
  :linenos:   

    int_signal <= integer(signed_signal);




resize
*********************************************
Again, make sure you're using IEEE.numeric_std.ALL
Use this to resize "sign extend" your vector/register that holds your signed/unsigned value.
Use before doing arithmetic.

.. code-block:: vhdl
  :linenos:   

    resize (signed; size);
    
    resize (unsigned; size);


process
#########################
You'll be writing/using this, alot.

.. code-block:: vhdl
  :linenos:   

    process (sensitivity list) begin

        -- RTL code

    end process;


The sensitivity list is a list of signals, that we tell the process to monitor
and to act upon/ do something when said signals change. basically, execute the process
when change in sensitivity signals detected.

a process can be combinational or sequential.

combinational vs sequential
---------------------------------------
when writing combinational process, you must list all the input signals to logic function.
leaving or forgetting signals, results in inferred latches and combinational loops.
in generally, neither are desired.

.. code-block:: vhdl
  :linenos:   
    
    LIBRARY IEEE;
    USE IEEE.std_logic_1164.ALL;
    USE IEEE.numeric_std.ALL;

    entity another_component is port (
        clk : in std_logic;
        rst : in std_logic;
        someout : out std_logic  
    );
    end another_component;
    
    architecture rtl of fpga_top is
        --signal declarations
        --component declarations
    begin
        --combinational, you must list all the input signals
        process (sensitivity signals) begin
            if () then
            else
            end if;
        end process;

        --combinational
        process (all) begin     --VHDL2008, to use all
            if () then
            else
            end if;
        end process;

        --sequential, sync reset
        process (clk) begin
            if () then
            else
            end if;
        end process;

        --sequential - w async reset
        process (clk, rst) begin
            if () then
            else
            end if;
        end process;

    end rtl;    



if else
#########################
very similar to what many see in 'software' programming.
syntactically similar, but different end result.
this is probably redundant, but in programming, code is executed sequentially by the processor.
in FPGAs, they result result in encoders and muxes, LUTs. they represent a logic function.  

.. code-block:: vhdl
  :linenos:   

    -- this is in a process block, with all signals listed or all in VHDL2008
    -- sequential version
    process (din1, din2, sel) begin
        if (sel = '1') then
            dout <= din1;
        else    
            dout <= din2;
        end if;
    end process;

    -- will result in priority encoding
    process (all) begin                 --VHDL2008
        if (wen) then
            --some assignment
        elsif (ren) then
            --some assignment
        else
            --some assignment
        end if;    
    end process;



.. warning::

    There is no ternary if-else shorthand, seen in C and verilog
        dout <= sel ? din1 : din2;


when else
#########################
i've never really used this, but have started to see it more often 

.. code-block:: vhdl
  :linenos:   
  
    -- concurrent version.
    -- this doesn't have to be in a process block.
    dout <= din1 when sel else din2;

    b <= "1000" when a = "00" else 
	 "0100" when a = "01" else 
	 "0010" when a = "10" else 
	 "0001" when a = "11";


with select
#########################
i've never really used this..

.. code-block:: vhdl
  :linenos:   

    with a select b <=
        "1000" when "00",
        "0100" when "01",
        "0010" when "10",
        "0001" when "11";

case
#########################
another similar to software programming, but again end result not the same.

Generally cases is used for and/or will become..
MUX vs. FSM 

i dont think you can synth a priority encoder with the VHDL case statement,
per the requirement of the syntax. The case 'sel' variable/signal and when 
condition width have to match for comparison.

.. code-block:: vhdl
  :linenos:   

    --case used for MUX
    process (all) begin     --VHDL2008
        case sel is
            when "00" =>
                dataout <= datain1;
            when "01" =>
                dataout <= datain1;
            when "10" =>
                dataout <= datain1;
            when "11" =>
                dataout <= datain1;                
            when others =>
                dataout <= 0;
        end case;
    end process;  

    -- case used in FSM
    type state_type is (IDLE, WRITE, WR_WAIT, READ);       -- one hot 4 states = 4bits.
    signal state : state_type;

    process (clk) begin
        if (rising_edge(clk)) then
            if (rst) then               -- sync reset
                state <= IDLE;>
            else
                case state is
                    when IDLE =>

                        -- some output
                        busy <= '0';>

                        --next state condition
                        if (some input condition) then        -- next state depends on current state and some input condition, maybe write enable.
                            state <= WRITE;
                        end if;
                        
                    when WRITE =>

                        -- some output
                        data_reg <= data_reg[14 downto 1] & datain;
                        busy <= '1';

                        --next state condition
                        if (some input condition) then     -- maybe counter value, bits written 
                            state <= WR_WAIT;
                        end if;

                    when PARITY =>
                        -- some output                    
                        parity_reg <= datain xor something;

                        --next state condition
                        if (some input condition) then      -- maybe read en.
                            state <= READ;
                        end if;

                    when READ =>

                        dataout <= mem[i];      -- depends on current state
                        
                        --next state condition
                        if (some condition) then        -- maybe counter, bits read.
                            state <= IDLE;
                        end if;           

                    when others =>
                        state <= IDLE;>

                end case;
            end if;
        end if;
    end process;  



generics
#########################
Is used to parametrize design. Enable re-use/customization.
Often seen for bit width, among other block settings.

.. code-block:: vhdl
  :linenos:   

	component some_component is
		generic (N : integer := 6);
	port (
			clk	: in std_logic;
			en : in std_logic;
			rst	: in std_logic;
			datain : in std_logic_vector(13 downto 0);
	);
	end component some_component;

generate
#########################
Use/Synthesize block of code if condition is true

.. code-block:: vhdl
  :linenos:   

    if (some condition is true) generate
        --constants
    begin
        --some code, processes etc.
    end generate;

    if (some condition is true) generate
        --constants
    begin
        --some code, processes etc.
    end generate;

package
#########################
for organizing and centralizing re-use constants, records, functions

.. code-block:: vhdl
  :linenos:   
  
    package some_package is
        --records
        --constants
        --function declarations
    end some_package;

    package body some_package IS
        -- body 
        --function definition
    end some_package;

record
#########################
Define/create them in the packages. Can be used as a type of signal that is a collection of signals.

.. code-block:: vhdl
  :linenos:   
    
    type eth_packet is 
    record
        datain : std_logic_vector(127 downto 0);
        keep : std_logic_vector(15 downto 0);
        end : std_logic;
        start : std_logic;
        valid : std_logic;
    end record;

for loop
#########################
They are not sequentially executed as in software programming.
they are used to reduce, simplify your code.
you have to think about it from a hardware perspective.
the for loop is rolling up? the code,
but when synthesized, it is 'unrolled'/ flattened

.. code-block:: vhdl
  :linenos:   
    
    -- for instance, this is saying we have 8 data_ff
    -- our datain is also 8 bits wide, 
    -- we want to connect one input bit/signal to the data_ff
    -- so instead of writing this 8 times,
    -- we write it once.

    for i in 0 to 7 loop
        data_ff[i] <= datain[i];
    end loop;

    for i in 0 to 7 loop
        DUT[i] <= datain[i];
    end loop;

arrays
#########################
used to store data, can become RAM.

.. code-block:: vhdl
  :linenos:   

    --1D array is your std_logic_vector

    --2D array (N depth, by 16 SL) or 1D of 16bit SLVs
    type mem is array (0 to N) of std_logic_vector(15 downto 0);

    --2D array of SLVs. N width/column, M depth/height/row
    --3D array because each indice is not a bit, but a vector, 
    type mem is array (0 to N, 0 to M) of std_logic_vector(15 downto 0);    

    --for instance in video/imaging
    --1920x1080 = (height x width) or (row x column) "array or matrix", but each index holds a pixel.
    --if it is an RGB pixel, then it is 8bit x 8bit x 8bit = 24bit per pixel = std_logic_vector(23 downto 0)
    -- 8x8x8 = 512 color levels.



operators
#########################

.. code-block:: vhdl
  :linenos:   
  
functions
#########################
They are combinational! I never really see this in designs, more in verification/validation.

.. code-block:: vhdl
  :linenos:   
  
    function <function_name> (
            input parameters : type
            input parameters : type
    ) return <return_type> is
        --constant_or_variable_declaration
    begin
        --HDL code here

        return <value>
    end function;


Template
#########################
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









***********************************
Verilog
***********************************
Later..

***********************************
SystemVerilog
***********************************
Later.. as I dont use enough.



***********************************
HDL PT. 2 
***********************************

This section is to emphasize HDL on FPGAs or vendor specific (primarily Xilinx bc that is what I use at the moment).
It should be revisited after reading about combinatorial and sequential circuits.
I will probably discuss some of it there too, so there will be some redundancy in information depending where your entry is.

Or continue if you're already familiar.



Register/FlipFlops (FF)
##################################################
There is only D FF in an FPGA.. other styles FF you learn in digital logic class do not exist.
If you try implementing other flavors (SR, JK, T), you'll just use the available DFF and surrounding LUTs to realize their functionality.

Reset
#########################
Asynchronously setting or resetting registers are synthesized into preset or clear registers.

Sequential functionality in device resources, such as block RAM components and DSP blocks, can be set or reset synchronously only.


Do not describe flip-flops with both a set and a reset.
No flip-flop primitives feature both a set and a reset, whether synchronous or asynchronous.
Flip-flop primitives featuring both a set and a reset can adversely affect area and performance.

Avoid operational set/reset logic whenever possible. 
There can be other, less expensive, ways to achieve the desired effect, 
such as taking advantage of the circuit global reset by defining an initial content.
Always describe the clock enable, set, and reset control inputs of flip-flop primitives as active-High. 
If they are described as active-Low, the resulting inverter logic penalizes circuit performance.

.. code-block:: vhdl
  :linenos:   
    
    -- sometimes i write like this
    process(clk)
        if(rst) then

    ...

    -- sometimes i write like this
    process(clk)
        if(rst = '1') then

    ...





Inferring and Inference
##################################################

Synthesis/Implementation
##################################################
I want to focus on HDL, RTL and implementation results.
Think hardware.

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

Using Dedicated Hardware
##################################################
Like what it means to use dedicated hardware, inference(ing) vs. LUT.

You'll want to write code such that it will utilize dedicated hardware when you can
such as....
    RAM: BRAM vs distributed memory.. , 
    DSP, for adding/subtracting larger vectors, multiplying large vectors, FIR filters
    SRL, shift registers


Data is written synchronously into the RAM for both types. 
The primary difference between distributed RAM (made from LUT/FF = LUTRAM) and dedicated block RAM lies in the way
data is read from the RAM. See the following table.

::

    Action  Distributed RAM     Dedicated Block RAM
    Write   Synchronous         Synchronous
    Read    Asynchronous        Synchronous


Generally you will always want to take advantage of RAM, DSP, SRL, MUX? over their LUT equivalents.. better performance.
they are tightly stiched already.. "dedicated hardware/circuits" their area or real estate is already in place. 
if you dont use it you lose it. its already there for you.









Finate State Machine
#########################
Vivado synthesis supports specification of Finite State Machine (FSM) in both Moore and Mealy form. An FSM consists of the following:

A state register
A next state function
An outputs function

Mealy depends on current state and input.
Moore depends only on current state. "More is less."

One hot encoding - use this in most case, tool with recognize.

Gray state encoding - use this when passing value such as pointer counter across clock domains.
