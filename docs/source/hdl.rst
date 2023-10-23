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




I feel like.. HDL should just be purely HDL like basic syntaxs and templates... with out application.
then as we talk about the different logic operation or circuits...
we'll provide snippets of the HDL code which will synthesize into these circuits.
HDL sprinked across the sections......

The HDL language is expansive? but for FPGA synthesis, you can only use a subset of the language.
The language can be used for both development and verification. 
Alot of the verification syntax/HDL is not synthesizable.
We will first focus on synthesizable and return for test bench, validation, verification.


VHDL
########################################################################################################
just some of the basic stuff... references and templates.

Libraries and use
=============================

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
=============================

how to create your component/module

.. code-block:: vhdl
  :linenos:   

    LIBRARY IEEE;
    USE IEEE.std_logic_1164.ALL;
    USE IEEE.numeric_std.ALL;
    
    entity fpga_top is port (
            clk : in std_logic;
            rst : in std_logic;
            someout : out std_logic  
    );
    end fpga_top;
    
    architecture rtl of fpga_top is
        --signal declarations
        --component declarations
    begin
        -- we'll fill it in later.
    end rtl;

this can be in some other file 

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
    
    architecture rtl of fpga_top is
        --signal declarations
        --component declarations
    begin
        process (sensitivity) begin
            if () then
            else
            end if;
        end process;

    end rtl;

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
        process (clk) begin
            if () then
            else
            end if;
        end process;
    end rtl;    

architecture vs structure vs behavior
------------------------------------------------------------



component
=============================

1.  you create your component with entity directive? (see entity section)
2.  then you declare its usage, in another entity or testbench. 
3.  then you instantiate the component where it is used and label it.
4.  map port signals

.. code-block:: vhdl
  :linenos:   
    
    LIBRARY IEEE;
    USE IEEE.std_logic_1164.ALL;
    USE IEEE.numeric_std.ALL;
    
    entity fpga_top is port (
            clk : in std_logic;
            rst : in std_logic;
            someout : out std_logic  
    );
    end fpga_top;
    
    architecture rtl of fpga_top is
        --signal declarations

        -- 2. component declarations        -- for code readability, can create a separate component.vhd file and declare them all there.
        component some_component is port (
            clk : in std_logic;
            rst : in std_logic;
            someout : out std_logic  
        );
        end component;

        component another_component is port (
            clk : in std_logic;
            rst : in std_logic;
            someout : out std_logic  
        );
        end component;

    begin
        --  3. component instantiation
        DUT1_label : some_component port map (
            clk => clk100,
            rst => rst,
            someout => dout1
        );

        DUT2_label : another_component port map (
            clk => clk150,
            rst => rst,
            someout => dout2
        );        
    end rtl;

.. ::note 

    Notice => used to assign signals to ports. verus <= to assign values or signals to signals!

data types
=============================
    signals, variable, constants

signals
----------------------------
These are the common ones I've used.

    std_logic
    
    std_logic_vector
    
    unsigned
    
    signed
    
    integer
    
    natural
    
    arrays

assignment
----------------------------
    
    <= signal assignment
    
    := variable assignment, signal initialization.

conversions
----------------------------

process
=============================

.. code-block:: vhdl
  :linenos:   

    process (sensitivity list) begin

        -- RTL code

    end process;

combinational vs sequential
----------------------------
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
        --combinational
        process (sensitivity signals) begin
            if () then
            else
            end if;
        end process;

        process (all) begin     --VHDL2008
            if () then
            else
            end if;
        end process;

        --sequential
        process (clk) begin
            if () then
            else
            end if;
        end process;
    end rtl;    



if else
=============================
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

    -- will result in priority encoded 
    process (all) begin     --VHDL2008
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
=============================
.. code-block:: vhdl
  :linenos:   
  
    -- concurrent version.
    -- this doesn't have to be in a process block.
    dout <= din1 when sel else din2;

with select
=============================
.. code-block:: vhdl
  :linenos:   
  
case
=============================
.. code-block:: vhdl
  :linenos:   

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


generics
=============================
.. code-block:: vhdl
  :linenos:   

	component some_component is
		generic (channel_type : integer := 6);
	port (
			clk							: in std_logic;
			en							: in std_logic;
			rst							: in std_logic;
			datain					: in std_logic_vector(13 downto 0);
	);
	end component some_component;

generate
=============================
.. code-block:: vhdl
  :linenos:   


    if (some condition is true) geenrate
        --constants
    begin
        --some code, processes etc.
    end generate;
  
package
=============================
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
=============================
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
=============================
.. code-block:: vhdl
  :linenos:   
  
    for i in 0 to 7 loop
        data_ff[i] <= datain[i];
    end loop;

arrays
=============================
double check this..

.. code-block:: vhdl
  :linenos:   
    --1D array is your std_logic_vector

    --2D array (N depth, by 16 SL) or 1D of 16bit SLVs
    type mem is array (0 to N) of std_logic_vector(15 downto 0);

    --2D array of SLVs. N width/column, M depth/height/row
    type mem is array (0 to N, 0 to M) of std_logic_vector(15 downto 0);    

    
for instance in video/imaging
1920x1080 = (height x width) or (row x column) "array or matrix", but each index holds a pixel.
if it is an RGB pixel, then it is 8bit x 8bit x 8bit = 24bit pixel res. = std_logic_vector(23 downto 0)



operators
=============================
.. code-block:: vhdl
  :linenos:   
  
functions
=============================
They are combinational!

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


template
=============================
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










Verilog
##############################################################################
Later..

SystemVerilog
##############################################################################
Later.. as I dont use enough.




HDL2 
##############################################################################
This section is to emphasize HDL on FPGAs or vendor specific (primarily Xilinx bc that is what I use at the moment).
It should be revisited after reading about combinatorial and sequential circuits.
I will probably discuss some of it there too, so there will be some redundancy in information depending where your entry is.

Or continue if you're already familiar.



Register/FlipFlops (FF)
=============================
There is only D FF in an FPGA.. other styles FF you learn in digital logic class do not exist.
If you try implementing other flavors (SR, JK, T), you'll just use the available DFF and surrounding LUTs to realize their functionality.

Reset
=============================
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

Inferring and Inference
=============================

Synthesis/Implementation
------------------------------
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
------------------------------
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

    Action  Distributed RAM	    Dedicated Block RAM
    Write	Synchronous	        Synchronous
    Read	Asynchronous	    Synchronous


Generally you will always want to take advantage of RAM, DSP, SRL, MUX? over their LUT equivalents.. better performance.
they are tightly stiched already.. "dedicated hardware/circuits" their area or real estate is already in place. 
if you dont use it you lose it. its already there for you.









Finate State Machine
=============================
Vivado synthesis supports specification of Finite State Machine (FSM) in both Moore and Mealy form. An FSM consists of the following:

A state register
A next state function
An outputs function

Mealy depends on current state and input.
Moore depends only on current state. "More is less."

One hot encoding - use this in most case, tool with recognize.

Gray state encoding - use this when passing value such as pointer counter across clock domains.
