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

---------

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


---------

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

  z &= x'\\
    &= \bar{x}

**Truth Table:**
::
 
  x       z
  input   output
  0       1
  1       0

=====  =====
Truth Table
-------------
Inputs Output
------ ------
X      Y
=====  =====
0      1
1      0
=====  =====

Remember, these logic gates are to represent the logical operations/functions in Boolean Algebra.
They are to realize/implement the math, logical operations and functions in actual hardware.

AND Gate
====================
The output is true, '1' only when all inputs are true, '1'.

.. math::

  z &= x \cdot y\\
    &= xy

*Personally, I prefer to write the latter.*


=====  =====  ======
Truth Table
--------------------
Inputs        Output
------------  ------
X      Y      Z
=====  =====  ======
0      0      0
0      1      0
1      0      0
1      1      1
=====  =====  ======


.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="600" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKABkLiURtC8KU-XvypUAZgEMANgGc61SO07cALHAH81oqCEmz5SRQFkQGNDzwrTli1aopoCFmErLbp89hv2dTgPY6hHYgKmCQ2Aqw8GSECIQohiDcVNgsARBBOqHhkfCQMXEJOtwQqQHcmVTZ3IbQEFSsQA" 
            title="AND gate" >
        </iframe>
    </div>

---------

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

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="600" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKDARQuM+zwBYQOQiF4CqnWiwAyXHoTwUUC7PKhqAZgEMANgGc61SNNkg+cRQrNVrILXoNIjAWUEqR-EHnOi1KaAhYAe3AQQjFTMEhsQ1h4MkIEQhRHEE4IbCDU0PC+SOjHWLh4xOTfLIzg6LC1XMhOAogqViA" 
            title="OR gate" >
        </iframe>
    </div>

---------

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

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="600" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKABkLiURtC8KU-XvypUAZgEMANgGc61SO07cALHAH81oqCEmz5SRQFkQGNDzwrTli1aopoCFmARWEXW6fPYb9nU4B7HUI7EBUwSGwFWHgyQgRCFEMQbipsFiCIEJ1wyOj4SDiEpJ1uCHSg7myqXO5DaAgqViA" 
            title="XOR gate" >
        </iframe>
    </div>

---------

NAND Gate
====================

.. warning::
  
  Negating means to NOT the output/result, which is not the same as NOT'ing the input.
  The output is false, '0' if all the inputs are true, '1'.
  The output is true, '1' if any of the inputs are false, '0'.

.. math::

  z &= (xy)'\\
    &= \overline{(xy)}

**Truth Table:**
::

  x, y    z         z'
  input   output    output
  0  0    0         1
  0  1    0         1
  1  0    0         1
  1  1    1         0

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="600" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKABkLiURtC8KU-XvypUAZgEMANgGc61SO07cALHAH81oqCEmz5SRQFkQGNDzwrTli1aopoCFmAQQEXW6fPYb9nU4B7HUI7EBUwSGwFWHgyQgRCFEMQbipsFiCIEJ1wyOj4SDiEpJ1uCHSg7myqXO5DaAgqViA" 
            title="NAND gate" >
        </iframe>
    </div>

---------

NOR Gate
====================
  The output is false, '0' if any of the inputs are true, '1'.
  The output is true, '1' if all of the inputs are false, '0'.

.. math::

  z &= (x + y)'\\
    &= \overline{(x + y)}

**Truth Table:**
::

  x, y    z         z'
  input   output    output
  0  0    0         1
  0  1    1         0
  1  0    1         0
  1  1    1         0

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="600" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKABkLiURtC8KU-XvypUAZgEMANgGc61SO07cALHAH81oqCEmz5SRQFkQGNDzwrTli1aopoCFmATZlt0+ew371JwHsdQjsQFTBIN0NYeDJCBEIUQxBuKmwWQIhgnTCIhWi4WPjEnW4INMDuLKoc7iiIKlYgA" 
            title="NOR gate" >
        </iframe>
    </div>

---------

XNOR Gate
====================
  The output is true, '1', if only if all inputs are the same.
  The output is false, '0', if the inputs are not the same, differ.
  XNOR is an XOR with the output negated.

.. math::

  z &= (x \oplus y)'\\
    &= \overline{(x \oplus y)}

**Truth Table:**
::

  x, y    z         z'
  input   output    output
  0  0    0         1
  0  1    1         0
  1  0    1         0
  1  1    0         1

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="600" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKABkLiURtC8KU-XvypUAZgEMANgGc61SO07cALHAH81oqCEmz5SRQFkQGSCp54LGPpYtUU0BCzAILCLnZCEEhLw51nAElvXy8zC2wrHRgkZwB7HUJ7EBUwSGwoWHgbFGJsYhUEbDAUQ2y4Mh9CMp1uKmwWRIhknTSMrPhIXPzC4tLyrqrfWoCIRsTuVqp27nKIKlYgA" 
            title="XNOR gate" >
        </iframe>
    </div>

---------

Negative AND Gate
====================
  Negating means to NOT the output/result, which is not the same as NOT'ing the input.
  Negating the input of an AND gate does not produce the same result as negating the output/result of an AND gate.

  Negating the input of an AND gate is called a 'Negative AND' gate.
  Negative AND is not the same as NAND.
  Negative AND is equivalent to NOR

.. math::

  z &= x'y'\\
  &= \bar{x}\bar{y}


**Truth Table:**
::

  x, y    x', y'    z
  input             output
  0  0    1  1      1           you're inputs are 0, 0 but you negate both to become 1, 1 for the AND gate, which results in a 1. 
  0  1    1  0      0
  1  0    0  1      0
  1  1    0  0      0

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="600" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKABkLCrsEUQAWYoRA8+VKgDMAhgBsAznWqR2nKvzDDBmjVF3T5ipMoCyIQnjwi8-EBl5WbVFNAQsAkqpH2ul0bphIrh4IXAI6PmHC4i4ULGCUZig22NZmFg66fIEsAO5m+F58EdjmULn5vqWESSKlynkR6sKNcGUNBfyt1Tad4iwA9rqEjmGQ2Eqw8GSEIShGIGIiA+BmI+pjE-CQ07PzfBDYy0VrYJBZUNAQVKxAA" 
            title="Neg-AND gate" >
        </iframe>
    </div>

---------

Negative OR Gate
====================
  Negative OR is not the same as NOR
  Negative OR is equivalent to NAND

.. math::

  z &= x' + y'\\
    &= \bar{x} + \bar{y}

**Truth Table:**
::

  x, y    x', y'    z
  input             output
  0  0    1   1     1
  0  1    1   0     1
  1  0    0   1     1
  1  1    0   0     0

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="600" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgoqoQFMBaMMAKABkLCrsEUQAWYoRA8+VKgDMAhgBsAznWqR2nKvzDDBmjVF3T5ipMoCyIQnjwi8-EBl5WbVFNAQsAkqpH2ul0bphIrh4IXAI6PmHC4i4ULADuZvhefBHY5lDxib7phCg2aZbKCRHqwiVwGcVJ-BW5NjXiLGDeeQ5mFm1O1K4A9rqEjmGQ2FCw8Bi5xNjE-AjYYChGY3BkhCGLumIiLH0QA7rqw6PwkBMoUzNzC0snq+tGIHwQ2DuPZoOHfEsQVKxAA" 
            title="Neg-OR gate" >
        </iframe>
    </div>

---------

DeMorgan's Law
====================
These last two examples (regarding negative inputs) are DeMorgan's Law,
allowing us to go back and forth between product of sums and sum of products.

.. math::
  x'y' &= (x+y)'\\
  x'+ y' &= (xy)'



---------

Circuit Analysis, Implementation and Design
####################################################

Boolean Algebra
========================================
Will explain.

Truth Table
========================================
Will explain.

Gate-level Minimization
========================================
The tool does this for you, optimizes the logic etc.

---------

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


An if-else approach to writing the MUX only produces the same result when the select/control inputs are mutually exclusive, unique.
If it is not, the tool will synthesize a priority encoder. 
It is better/good practice to use case statements when implementing MUX/selections and reserve if-else for encoding with or without
priority. I'll probably repeat this in multiple sections and unify it at a later point..     


.. code-block:: vhdl
  :linenos:    

      A,B   : in  std_logic;
      sel       : in  std_logic;
      mux_out   : out std_logic;

      ...
      
      -- MUX using a case statement
      process(all) is
      begin
    
        case sel is
            when "0" =>
                mux_out <= A;
            when others =>        -- sel = '1'
                mux_out <= B;
        end case;

      end process;

      process(all) is
      begin
    
        if sel = '0' then
          mux_out <= A;
        else
          mux_out <= B;
        end if;

      end process;      




Demultiplexer
====================
The demux is a device that does just the opposite of the mux. you have ONE input this time, and many outputs. 
you still have select/control signals, but they are related to the output.

with the select bits, you are determining where to route/send the input. you are determining which 
output gets the input.


.. code-block:: vhdl
  :linenos:    

      A,B,C,D   : out  std_logic_vector(7 downto 0);
      sel       : in  std_logic_vector(1 downto 0);
      data_in   : in std_logic_vector(7 downto 0);

      ...


    
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
An encoder has 2^N inputs and N outputs. The inputs are numbered 0 to 2^N - 1.
Only one of these inputs is enabled/on or hot at a time, one hot.
You must guarantee one hot for this encoder to work properly.
Based on which input is hot, the encoder encodes the binary representation of the line.
You have to guarantee that only one of the input is ever hot.

::

  For 4 bit input, you get 2 bit output.

    if line 0 is hot, 0000, you're output is "00"
    if line 1 is hot, 0010, you're output is "01"
    if line 2 is hot, 0100, you're output is "10"
    if line 3 is hot, 1000, you're output is "11"

It encodes the hot line to a binary value, hence binary encoder. or 4 to 2 encoder.
In general, 2^n to n encoder.

Another encoder, is the priority encoder. Where you are allowed to have more than 
one hot line. In this implementation, the input lines have weight/or priority/ ranking.
Thus the index/input with high priority will determine the output result.

::

  If 0001 -> 00
  If 001x -> 0010 = 0011 -> 01
  If 01xx -> 0100 = 0101 = 0110 = 0111 -> 10
  if 1xxx -> 1000 = 1001 = 1010 = 1011 = 1100 = 1101 = 1110 = 1111 -> 11

where x is dont care. in this case.. the most significant '1' determines the output.
where index is 3 2 1 0. If you have a 1 in the 1th index 001x, it doesn't 
matter what is in the 0th index. Your output is 01. You ignore all the lower
significant bits and only out

.. code-block:: vhdl
  :linenos:    

  if (in(3) = '1') then   -- if in(3) = '1', we dont care what the rest is, it is higher ranked higher priority.
    p_enc <= "11";
  else if (in(2) = '1') then    -- like wise if in(2) is '1', we dont look at the rest and so on!
    p_enc <= "10";
  else if (in(1) = '1') then
    p_enc <= "01";
  else -- (in(0) = '1')
    p_enc <= "00";
  end if;


Decoder
====================
We will introduce a binary decoder first.
A decoder has N inputs and 2^N outputs. The output are numbered 0 through 2^N - 1.
For instance if N = 2, you get 0 - 3. If N = 3, you get 0 - 7. etc.

It decodes the binary inputs/ value to one of the "decimal" value output. For a given
input, only one of the output will be on/true. or hot.

The 2 input decoder is generally called a 2 to 4 binary decoder.
3 to 8 binary decoder.. so on. 4 to 16.

Decoders can be used/often are used to decode address and enable some read/write line or select/enable some part.

This is very similar to the demux. you have N inputs (decoder), and N select signals (demux). 
You have 2^N outputs (both), and ONLY one can be on/hot at any given time, BASED on either the input (decoder)
or select signals (demux). They are similar in that the demux HAS to decode the select lines, just as a decoder
decodes the input lines.
The difference between the two is the decoder does not have that one input signal
a demux has. Another difference is the decoder outputs are single lines, 
the demux input/output can be vector/array/bus of bits..
the demux is a DATA routing mechanism/concept. And while a demux's output line is "hot" on enabled, the actual
value could be a 1 or 0, depending on what the INPUT is. The decoder on the other hand, is truly hot when selected
by the input.


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
  
  I need to look at what the cross over point is. Also test out different input widths vs LUT.

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
We use comparisons so often, in if-else statements, but do you really know what is going on? at the LUT level?
I dont think I've really read it anywhere. But here we go..
Say we want to compare two bits.. x and y

::

  x y   
  0 0   x = y
  0 1   x < y
  1 0   x > y
  1 1   x = y

above, we are functionally describing the output result, each result will actually require its own column.
which means there are 3 truth tables, but because the inputs are common, 
we are just going to rotate the result and populate in the table.

::

        A       B       C
  x y   x = y   x < y   x > y
  0 0   1       0       0
  0 1   0       1       0
  1 0   0       0       1
  1 1   1       0       0

for x = y, we see that, there are two cases in which the inputs can be equal.. and this resembles the XNOR gate. 

.. math::

    x < y :\\
    A = \overline{x \oplus y}


for x < y, it is only true in the second line, when x is 0 and y is 1. 
I guess i should write the section about writing equations from truth tables...
which is basically writing sum of products or products of sum.
which then brings about the gate minimizations... if necessary.

but x < y, is 

.. math::

    x < y :\\
    B = \bar{x} y = x'y

likewise for x > y, 3rd line.

.. math::

    x > y :\\
    C = x \bar{y} = xy'

Because there are 3 truth tables, this implies the tool is likely to use 3 LUTs , specifically LUT2, to realize 
this comparative function. The LUT tables will be populated with the same values as above!

Again, we aren't going to be using actual XNOR or AND gates to implement this function, we use their truth tables, input/output relationships.

I hope that last few examples clarify or shed light on how combinational logic is actually realized in an FPGA.

Like with everything else, as the input width increases, the tool will pull in more LUTs and either have them tree down/up, cascaded or paralleled.

.. note::
  TO SELF: this would be interesting to see.. at what point the tool chooses one over the other. Maybe it's already there, under how
  optimization works. But might be intellectual prop stuff.



Multiplier
====================
Things are getting more complicated!
Finish the fundamental section about binary multiplication before coding.



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
See Advance Section.

Shifting?
====================
Maybe just have in sequential?

---------

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
    
  where to put these? we talk about it in fundamentals, but we need to talk about it with HDL and FPGAs.
  fundamental ch, no HDL allowed yet. just theory/math(boolean)/idea/concept.
  by this chapter, i've introduced HDL too.
  combinational would normally be from digital logic/circuit perspective..
  and should.. 
  but not everything is applicable. or not in the same way atleast..
  so maybe i can blend/tie things here.


Unsigned vs Signed Binary
---------------------------------------------
Unsigned vs Signed Fixed Point
---------------------------------------------
Floating point
---------------------------------------------
Advance..

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


::

  x1,x2   y1,y2
  00      00
  00      01
  00      10
  01      00
  01      01
  01      10
  01      11
  10      00
  10      01
  10      10
  11      00
  11      01  
  11      10
  11      11