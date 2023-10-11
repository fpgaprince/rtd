************************************************
Combinatorial Circuits
************************************************
Combinatorial circuits have no memory.
They depend only on the present input and in a sense, the input order does not matter.
Sequential in contrast, have memory, therefore the input order, previous input/state matter.

We'll talk about the logic from an abstract point of view/high level,
returning to gate level/CMOS implementation at a later time (or where necessary).

The reason for this is because we aren't dealing with the gate level or its implementation in an FPGA.
I reiterated this many times over, you are not dealing with logic gates in an FPGA. 
Combinatorial logic are realized with LUTs. 

You will have NOT gates sprinkled throughout the chip to help the tool optimize,
but you wont have an actual AND OR gate.


Basics
##########################

Binary
====================

Logic Functions
====================
  From Boolean Algebra.

  Logic functions boil down to this.
  z = F(x,y). 

  The output z, is a function of x and y input.

  It shows the relationship of the output and input.

  The output, as well as the input, can be multi-variable.

Truth Table
====================
  A truth table is a table that lists/maps out all the input combinations for a given number of input and their resulting output.

  For 2 input, you will have 4 combinations, and 4 output results.

  For 3 input, you will have 8 combinations, and 8 output results.
  
  For 4 input, you will have 16 combinations, and 16 output results..
  
  Notice, powers of 2's.


Logic Gates
##########################

  (NOT, AND, OR, XOR), logic operator

  In FPGA, you are not actually connecting gates, you capture the boolean expression and store it in a LUT, which is basically SRAM. 

  The SRAM is configured at bootup.

NOT Gate
====================
The NOT gate inverts whatever value is at its input.
"The apostrophe is used to signify negation"

.. math::

  z = x'

**Truth Table:**
::
 
  x       z
  input   output
  0       1
  1       0

Remember, these logic gates are to represent the logical operations/functions in Boolean Algebra.
They are to realize/implement the math, logical operations and functions in actual hardware.

AND Gate
====================
The output is true, '1' only when all inputs are true, '1'.

.. math::

  z &= x \cdot y\\
    &= xy

*Personally, I prefer to write the latter.*

**Truth Table:**
::

  x, y    z
  input   output
  0  0    0
  0  1    0
  1  0    0
  1  1    1 

OR Gate
====================
The output is true, '1' if any of the input is true, '1'.

.. math::

  z = x + y

**Truth Table:**
:: 

  x, y    z
  input   output
  0  0    0
  0  1    1
  1  0    1
  1  1    1 

XOR Gate
====================
The output is true, '1', if and only if one of the input is true.
The output is false, '0', if all of the inputs are the same.

.. math::

  z = x \oplus y

**Truth Table:**
::

  x, y    z
  input   output
  0  0    0
  0  1    1
  1  0    1
  1  1    0 

.. warning::
  
  Negating means to NOT the output/result, which is not the same as NOT'ing the input.

NAND Gate
====================
The output is false, '0' if all the inputs are true, '1'.
The output is true, '1' if any of the inputs are false, '0'.

.. math::

  z = (xy)'

**Truth Table:**
::

  x, y    z         z'
  input   output    output
  0  0    0         1
  0  1    0         1
  1  0    0         1
  1  1    1         0

NOR Gate
====================
The output is false, '0' if any of the inputs are true, '1'.
The output is true, '1' if all of the inputs are false, '0'.

.. math::

  z = (x + y)'

**Truth Table:**
::

  x, y    z         z'
  input   output    output
  0  0    0         1
  0  1    1         0
  1  0    1         0
  1  1    1         0


XNOR Gate
====================
The output is true, '1', if only if all inputs are the same.
The output is false, '0', if the inputs are not the same, differ.

.. math::

  z = (x \oplus y)'

**Truth Table:**
::

  x, y    z         z'
  input   output    output
  0  0    0         1
  0  1    1         0
  1  0    1         0
  1  1    0         1


Negative AND Gate
====================
  Negating means to NOT the output/result, which is not the same as NOT'ing the input.
  Negating the input of an AND gate does not produce the same result as negating the output/result of an AND gate.

  Negating the input of an AND gate is called a 'Negative AND' gate.
  Negative AND is not the same as NAND.
  Negative AND is equivalent to NOR

.. math::

  z = x'y'

**Truth Table:**
::

  x, y    x', y'    z
  input             output
  0  0    1  1      1           you're inputs are 0, 0 but you negate both to become 1, 1 for the AND gate, which results in a 1. 
  0  1    1  0      0
  1  0    0  1      0
  1  1    0  0      0


Negative OR Gate
====================
  Negative OR is not the same as NOR
  Negative OR is equivalent to NAND

.. math::

  z = x' + y'

**Truth Table:**
::

  x, y    x', y'    z
  input             output
  0  0    1   1     1
  0  1    1   0     1
  1  0    0   1     1
  1  1    0   0     0


DeMorgan's Law
====================
These last two examples (regarding negative inputs) are DeMorgan's Law,
allowing us to go back and forth between product of sums and sum of products.

.. math::
  X'Y' &= (X+Y)'\\
  X'+ Y' &= (XY)'





Circuit Analysis, Implementation and Design
####################################################

Boolean Algebra
========================================

Truth Table
========================================

Gate-level Minimization
========================================








Combinatorial Components
####################################################
Using logic gates, we create more useful functions.
NOTE: that while we talk about gates to create these functions, an FPGA will actually use its CLB (LUTs and MUX) or dedicated hardware (DSP) to realize it.


Multiplexer
====================
A multiplexer is a device with multiple inputs, select/control input signal(s) and ONE output.
The select signal(s), select/determine which input to feed/route to the output.
Either the number of select signals will determine the number of inputs or the number of inputs
will determine the required number of select signals.

The simple case.. you want to select between 4 inputs. You need need 2 select signals/bits.
Another way to look at it or say it is.. I have 2 select signals, how many signals can I control? 4.
For example I have 3 select signals, how many inputs can I control? 8.
See the pattern? Powers of 2's again! 

What if the number isn't a power of 2? You'll need to recall log/ln and base conversions..

  

.. math:: 
    roundup( ln(N) / ln(2)) = \text{ N bits required}\\
    roundup( ln(7) / ln(2)) = roundup(2.80735) = 3 \text{ bits required}\\
    roundup( ln(9) / ln(2)) = roundup(3.16992) = 4 \text{ bits required}\\
    roundup( ln(14) / ln(2)) = roundup(3.80735) = 4 \text{ bits required}\\
    roundup( ln(29) / ln(2)) = roundup(4.85798) = 5 \text{ bits required}\\


Notice, for 29, you are not using up all the possible combination/control a 5 bit control signal can handle.
5 bits can control up to 32 signals. Therefore when you write your HDL, you have to handle what to do
when the control signal is one of the 3 (32-29) remaining cases that aren't applicable..

While the number or mux input is a result of the number of select bits, you are not required to use all of it, but you should always keep in mind what to do with what you dont care about or doesn't matter.

.. warning::
  
  You need to terminate, handle the else and when other clause, this is a combinatorial circuit with no clocks.

.. code-block:: vhdl
  :linenos:    

      A,B,C,D   : in  std_logic_vector(7 downto 0);
      sel       : in  std_logic_vector(1 downto 0);
      mux_out   : out std_logic_vector(7 downto 0);

      ...


      -- MUX using if-else statement
      process(sel, A, B, C, D) is
      begin
    
        if sel = "00" then
            mux_out <= A;
        elsif sel = "01" then
            mux_out <= B;
        elsif sel = "10" then
            mux_out <= C;
        else                --sel = "11"
            mux_out <= D;
        end if;

      end process;

      
      -- MUX using a case statement
      process(sel, A, B, C, D) is
      begin
    
        case sel is
            when "00" =>
                mux_out <= A;
            when "01" =>
                mux_out <= B;
            when "10" =>
                mux_out <= C;
            when others =>        -- sel = '11'
                mux_out <= D;
        end case;

      end process;

In the above example, the input width could have been anything, you could have been selecting bits instead of vectors..
and those vectors could have been ANY size! I just used 8 for simplicity.. it could have been 12, 16, 32, 54, 64, etc.

Note, while these different approach will produce the same simulation result, they are two different flavors of MUX, 
they are synthesized differently in the FPGA.
Write more..

There is another MUX, a one-shot.


.. code-block:: vhdl
  :linenos:    

      A,B,C,D   : in  std_logic_vector(7 downto 0);
      sel       : in  std_logic_vector(3 downto 0);
      mux_out   : out std_logic_vector(7 downto 0);

      ...
    
      -- MUX using a case statement
      process(sel, A, B, C, D) is
      begin
    
        case sel is
            when "0001" =>
                mux_out <= A;
            when "0010" =>
                mux_out <= B;
            when "0100" =>
                mux_out <= C;
            when "1100" =>
                mux_out <= D;                
            when others =>        -- other sel input combinations
                mux_out <= 'X';
        end case;

      end process;

Demultiplexer
====================
The demux is a device that does just the opposite of the mux. you have ONE input this time, and many outputs. 
you still have select/control signals, but they are related to the output.

with the select bits, you are determining where to route/send the input.


.. code-block:: vhdl
  :linenos:    

      A,B,C,D   : out  std_logic_vector(7 downto 0);
      sel       : in  std_logic_vector(1 downto 0);
      data_in   : in std_logic_vector(7 downto 0);

      ...

      -- MUX using if-else statement
      process(sel, data_in) is
      begin
    
        if sel = "00" then
            A <= data_in;
        elsif sel = "01" then
            B <= data_in;
        elsif sel = "10" then
            C <= data_in;
        else                --sel = "11"
            D <= data_in;
        end if;

      end process;
    
      -- DEMUX using a case statement
      process(sel, data_in) is
      begin
    
        case sel is
            when "00" =>
                A <= data_in;
            when "01" =>
                B <= data_in;
            when "10" =>
                C <= data_in;
            when others =>        -- sel = '11'
                D <= data_in;
        end case;

      end process;


The if-else version is not a true mux, the tool interprets that as a priority encoder.

Encoder
====================


.. code-block:: vhdl
  :linenos:    


Decoder
====================


.. code-block:: vhdl
  :linenos:    



Adder
====================
I will not go into the digital logic details right now.

While in digital logic, you are introduced to half adders, full adders, ripple carry and carry lookahead.. 
It does not apply to FPGAs because again, we're not dealing with the gates.
I'll repeat this many times over and throughout your reading. I don't think this is clear to many.


For example, we learn the half adder logic reduces down to these two operations.

.. math::

  sum &= X \oplus Y\\
  carry &= XY


.. code-block:: vhdl
  :linenos:    

    signal X, Y : std_logic;
    
    signal sum : std_logic;
    signal carry : std_logic;
    
    signal sum2 : std_logic_vector(1 downto 0);   --ovf expanded
    
    process(X,Y) begin
        sum <= X xor Y;
        carry <= X and Y;
    end process;    

    
    process(X,Y) begin
        sum2 <= X + Y;
    end process;



You wont synthesize the logic gates that make the half adder or full adder. 
You describe it (like in the second one), and the vendor tool will synthesize it into their FPGA's building block, the LUT.
The LUT's truth table is populated with the input to output relationship. 
This will synthesize int 2 LUT2s, *it wouldn't be LUT4 because you need two outputs in both case*

::

  x, y    sum
  input   output
  0  0    0           
  0  1    1
  1  0    1
  1  1    0         -> only one case which creates a carry.

  x, y    carry
  input   output
  0  0    0           
  0  1    0
  1  0    0
  1  1    1         -> the carry.








For small addition, the tool with synthesize them into LUTs, but as your bit/data width increases,
there is a point in which it will degrade performance, and is better to use the dedicated DSP hardware.
It is a poor choice to use DSP to just do 8bit addition. If you had to do 128bit addition or something, use the DSP.
What is the cross over though?

.. note:: 
  
  I need to look at what the cross over point is.

Subtractor
====================
Subtraction is pretty much the same as above talk.

.. code-block:: vhdl
  :linenos:    

    signal A, B : std_logic_vector(N downto 0);
    signal diff : std_logic_vector(N+1 downto 0);

    process(A,B) begin
        diff <= A - B;
    end process;


Comparator
====================







Multiplier
====================
.. code-block:: vhdl
  :linenos:    

  entity mult_unsigned is
  generic(
  WIDTHA : integer := 16;
  WIDTHB : integer := 16
  );
  port(
  A : in std_logic_vector(WIDTHA - 1 downto 0);
  B : in std_logic_vector(WIDTHB - 1 downto 0);
  RES : out std_logic_vector(WIDTHA + WIDTHB - 1 downto 0)
  );
  end mult_unsigned;

  architecture beh of mult_unsigned is
  begin
  RES <= A * B;
  end beh;


Divide
====================

Shifting?
====================


Bringing it all together
####################################################
Parity Gen and Check
========================================

Simple ALU
====================
Create/ show a simple one. That utilizes enc/dec, add/sub

  .. code-block:: vhdl
  :linenos:    





NOTES
====================


::

    An external pin of the circuit (OBUFT)
    An Internal bus (BUFT):
    An inferred BUFT is converted automatically to logic realized in LUTs by Vivado synthesis.
    When an internal bus inferring a BUFT is driving an output of the top module, the Vivado synthesis infers an OBUF.


.. code-block:: vhdl
  :linenos:    

    entity tristates_1 is
    port(
      T : in std_logic;
      I : in std_logic;
      O : out std_logic
    );
    end tristates_1;
    architecture archi of tristates_1 is
    begin
    process(I, T)
    begin
    if (T = '0') then
    O <= I;
    else
    O <= 'Z';
    end if;
    end process;
    end archi;
