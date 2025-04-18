########################
Data Storage Elements
########################

* analog equivalent? multivibrator, - bistable.
* digital logic/design
* FPGA version/application.. differences

We will introduce storage elements first.
While clock and timing is closely related to sequential circuits,
it is not necessary in order for you to store information/data.

You just need an..
Input, Control and Output.

The storage element can be made from the basic logic gates.

Two basic type, latch and flip flop.
The smallest memory element, being the flip flop. D FF to be specific.


******************************
Latches
******************************
Keep in mind input and control.

Latches are circuit which are sensitive to the level of the control signal, 
meaning while the control signal is at some level (say high), the circuit will pass the input value to the output. 
In other words, the output tracks the input.
When the control signal becomes low, the output "latches" the input value and stores it.
While the control signal remains low.. the output ignores any changes at the input, presenting only the latched/stored value.

Conversely, a the latch could have passed the input while the control signal was low, and latch the input value when the control signal is high.
In otherwords, the output tracks the input while the control signal is low and ignores it when the control signals is high.

What was just explained here was the D latch.


.. warning::

    there are no actual latch circuit in an FPGA. 
    
If you do try to implement a latch, its functionality is realized through flip flops and LUTs; they are generally unwanted in FPGAs.
They probably have their usage, but I have not personally used or even seen them in the complex systems I've worked with thus far. 
It is a common mistake I've seen with those new to FPGA and HDL.

.. warning::

    Inferred Latches are often the result of HDL coding mistakes, specifically from an incomplete if-else statements or case statements
    in a combinatorial process/always block where the developer did not handle all posible outcomes based on the input.

I think the confusion is knowing when an if-else and case statement needs to be completed in a unclocked/clocked process/always block

.. important::
    
    If you are writing a combinational circuit (unclocked), 
    YOU MUST HAVE THE ELSE OR DEFAULT CLAUSE.
    
For the combinatorial circuit, you do not need to explicitly have an else if statement for every possible outcome, if one else can take care of it.
what i mean is you can lump everything into the else clause if that is your logic.

    For instance, you dont need to explicitly write out every combination..

.. code-block:: vhdl
  :linenos:    

    process(A,B) begin
        if (A = '0' and B = '0') then
            out <= '0';
        elsif (A = '0' and B = '1') then
            out <= '0';
        elsif (A = '1' and B = '0') then
            out <= '0';
        else
            out <= '1';     --implies A = 1 and B = 1
        end if;
    end process;

    When the following is equivalent.

.. code-block:: vhdl
  :linenos:    

    process(A,B) begin
        if (A = '1' and B = '1') then
            out <= '1';
        else
            out <= '0'     --implies the only time output = 1, is if A and B = 1. for all other case, output = 0.
        end if;
    end process;


.. important::

    If you are writing a sequential circuit (clocked), 
    YOU DO NOT NEED THE ELSE OR DEFAULT CLAUSE.

This is because you creating registers/vectors to hold a value.. or counters.. 
in which if the conditions for the value to change are not met. It retains it's value.
This is storage.

.. code-block:: vhdl
  :linenos:    

    process(clk) begin
        if (A = '1' and B = '0') then
            out <= '1';
        elsif (A = '0' and B = '1') then
            out <= '0';            
        end if;
    end process;

Writing this is perfectly fine. It means that output can only change to a '1' when AB = '10'
The output can only be '0' when AB = '01'. For all other case, hold the previous value.
Maybe provide a waveform of various input combinations to show?


This is more for historic purposes/ derivation.

Multivibrators
#########################

SR Latch
#########################
DNE, briefly describe now.. not priorirty.

Gated SR Latch
#########################
DNE, briefly describe now.. not priorirty.

D Latch
#########################
DNE, briefly describe now.. not priorirty.






******************************
Flip Flops (FF)
******************************
Keep in mind, we still have not introduced the clock.
Think of input, control and output.

A flip flop is an edge triggered circuit.
The input is sampled/captured on an edge of the control signal. 
Edge meaning the transition of the control signal. The transition can be from low to high (positive edge)
or high to low (negative edge).


Nothing is passed to the output during either level, in comparison to the latch.



Flip Flops can be thought of as the most basic or lowest unit of memory.
It is how most basic/lowest data unit, the bit, is realized in circuit/hardware..


How do we detect an edge? pulse detector.
by attaching this to SR or D latch, we create the equivalent flip flop version.

Clocking the Control Signal
##################################################
Up to now we've only referred to the control signal/enable signal.
While latches do not require a clock, they do have some sort of enable signal.
This enable signal determines when and when not to store information.

If, we instead, made this signal toggle periodically.. say, with a clock/oscillator.

It is when we add timing, things become interesting.
It allow us to create more sophisticated circuits, solving more complex problems.

Time and timing is everything in this world..
    We can synchornize multiple events.

    We can predetermine when things happen.

    We can expect things to happen at very specific times. We can predict.

    With a clock we establish a sense of time.



D Flip Flops (DFF)
#########################
The ONLY type in an FPGA. 


.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="700" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKDASQTBRG0LxCEALFT4CqkFgFlB+Xv0F4BYqCBTQE02QKHYe-HXtXrNAGQrd5OocoUSQAMwCGAGwDOdapIBKFniKpdfzhwNWQqEzUNVRhNIA" 
            title="WTFFFFF" >
        </iframe>
    </div>

---------


Flip-Flops
:: 
    
    FDCE
        D flip-flop with Clock Enable and Asynchronous Clear (clear = 0)

    FDPE
        D flip-flop with Clock Enable and Asynchronous Preset (preset, any value not 0)

    FDSE
        D flip-flop with Clock Enable and Synchronous Set (set, any value not 0)

    FDRE
        D flip-flop with Clock Enable and Synchronous Reset (reset = 0)

    The number of Registers inferred during HDL synthesis might not precisely equal the number of Flip-Flop primitives in the Design Summary section.
    The number of Flip-Flop primitives depends on the following processes:
    Absorption of Registers into DSP blocks or block RAM components
    Register duplication
    Removal of constant or equivalent Flip-Flops
    Basically your estimate and final report may not match because the tool will optimize. You can turn this off though.



Edge triggered latch?
#########################
by using pulse detector + SR latch, SR FF is created.

SR Flip Flops
#########################
we dont want that invalid state.. thus JK and D.

JK Flip Flops
#########################
DNE, briefly describe now.. not priorirty.

T Flip Flops
#########################
DNE, briefly describe now.. not priorirty.


Most text will start out talking about digital logic and all their components
with regards to TTL logic.
I want to talk about the CMOS equivalent circuits. because internally this is what it is.
at the interface it can be either or and may even be LVDS.

.. important::
    
    Provide CMOS latch and flip flop with transmission gates and inverters.
    Don't gloss over this, I feel like many never learned this.
    Undestanding how it works gives you better/deeper understanding about setup time, hold time, metastability, etc.

    
******************************
Register
******************************
A collection/series/ordered set of flip flops make a register.
Say we have a set of 8 flip flops ordered from 0 to 7.
If we synchornize all of them to the same clock, and a transition (low to high)
occurs, all 8 flip flops will 'latch' whatever is at the input
and store it. This is basically how to store a byte (8 bits of data).
It will hold onto this value until the next rising edge of the clock.

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


Test this out. when you reset a register made of FF. if your reset value is 0011 for instance.
I think it will use 2xFDRE (for the 00 portion) and 2xFDSE for the 11 portion.
FDRE resets the value to 0. FDSE sets the value to 1.

Here our register size is 8bits, a byte. But it can be any size you need for your application.
In processors, you'll typically see 32bit or 64 bit nowadays.. but back then..
they started small and overtime increased..

Again, depending on your application, maybe it will be 10bits 12 or 14.. maybe 24. It depends
on whatever you need it to hold.

******************************
Memory
******************************


.. image:: images/network-Page-13.drawio.png
    :width: 400
    :align: center


Now that we have introduced the clock. We can introduce more refined/cultivated/developed/ memory types?

A collection and ordered set of registers.
Now say if we had 8 of these 8bit registers.. we can create a larger memory module/component.
how would we locate or assign to each of these registers?
how do we retrieve the stored information?
we can create/use an addressing system.
which is basically using a decoder.



Read-Only Memory (ROM)
#########################
for whatever size, is written to at startup. or programmed.
and cannot be done again.
during run time, you can only 'read' from it.
you read from it by supplying an address.
the address is decoded and the ROM outputs whatever is at that address location.





Random Access Memory (RAM)
################################

SRAM
*********************************************
Static random-access memory (static RAM or SRAM) is a type of random-access memory (RAM) 
that uses latching circuitry (flip-flop) to store each bit. SRAM is volatile memory; 
data is lost when power is removed. The term static differentiates SRAM from DRAM (dynamic random-access memory) 
which must be periodically refreshed. SRAM is faster and more expensive than DRAM; 
it is typically used for the CACHE and internal registers of a CPU while DRAM is used for a computer's main memory.

You'll see L1 L2 whatever CACHE memory, usually in the megabytes for CPU.

BRAM
======================
While all memory devices can be made from FF in the FPGA, there are hard dedicated memory components.
Meaning, their circuitry is part chip/FPGA is fabric, their circuitry is tightly coupled to provide better performance (speed/timing) and minimal area. 
They will always perform better than your LUT based equivalent.

BRAM is static RAM. 
This is the main type of RAM you will see/come across read about in relation to FPGAs.

CRAM
======================
Configuration RAM, which is basically SRAM that hold the FPGA configuration information.

DRAM 
*********************************************
Is dynamic random -access memory. They have to be refreshed periodically. These are the ones you buy for your PC.
They are external to the processor. They are external to the FPGA. They can be on a memory PCB, 'memory stick' 
or be packaged in an IC and placed directly on your PCB, like any other component. They are main memory.
Because they are external to the CPU/FPGA.. whatever, there is a propagation penalty! They are therefore slower! always.
Their advantage is cheapness. You can make larger memory capacity, gigabytes! vs. SRAM. 
SRAM being internal.. you only get kilobyte size memory. But they are way faster, as they're built in to your CPU
or FPGA.

SDRAM 
======================
is DRAM, but synchronized to a clock. Pretty much everything these days. 
DDR, DDR2, DDR3, DDR4, DDR5 (i think this is where we're at at the time of this writing).

DDR memory will be mentioned alot as well, now that we have SoC's where we CPU/FPGA on the same fabric.
I guess previously you could instantiate soft processors as well.

FLASH
################################
I am only mentioning it here because in Intel's MAX10, an FPGA/CPLD i worked on had it as "dedicated hardware"
internal to the FPGA. But more info about flash should be in the memory interface chapter/section.

Flash memory is an electronic non-volatile computer memory storage medium that can be electrically erased and reprogrammed. 
The two main types of flash memory, NOR flash and NAND flash.



CFM = Configuration Flash Memory. UFM = User Flash Memory. When i worked with max10
user flash memory (UFM) block that stores non-volatile information.
CFM is used to store configuration images 

