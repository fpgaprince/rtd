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
====================

  (NOT, AND, OR, XOR), logic operator

  In FPGA, you are not actually connecting gates, you capture the boolean expression and store it in a LUT, which is basically SRAM. 

  The SRAM is configured at bootup.

NOT Gate
-----------------------
The NOT gate inverts whatever value is at its input.
"The apostrophe is used to signify negation"
.. math::

  z = x'

::
 
  x     z
  input output
  0     1
  1     0

Remember, these logic gates are to represent the logical operations/functions in Boolean Algebra.
They are to realize the math, in actual hardware.
The basic boolean functions operate on 2 inputs, X and Y.

AND Gate
-----------------------
The output is true, '1' only when all inputs are true, '1'.
 "multiplication implies ANDing"

.. math::

  z &= x \cdot y\\
    &= xy

  Personally, I prefer to write the latter.

:: truth table

  x, y    z
  input   output
  0  0    0
  0  1    0
  1  0    0
  1  1    1 

OR Gate
-----------------------
The output is true, '1' if any of the input is true, '1'.
"addition implies OR"

.. math::

  z = x + y


::

  x, y    z
  input   output
  0  0    0
  0  1    1
  1  0    1
  1  1    1 

XOR Gate
-----------------------
The output is true, '1', if and only if one of the input is true.
The output is false, '0', if all of the inputs are the same.

.. math::

  z = x \oplus y

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
-----------------------
The output is false, '0' if all the inputs are true, '1'.
The output is true, '1' if any of the inputs are false, '0'.

.. math::

  z = (xy)'

::

  x, y    z         z'
  input   output    output
  0  0    0         1
  0  1    0         1
  1  0    0         1
  1  1    1         0

NOR Gate
-----------------------
The output is false, '0' if any of the inputs are true, '1'.
The output is true, '1' if all of the inputs are false, '0'.

.. math::

  z = (x + y)'

::

  x, y    z         z'
  input   output    output
  0  0    0         1
  0  1    1         0
  1  0    1         0
  1  1    1         0


XNOR Gate
-----------------------
The output is true, '1', if only if all inputs are the same.
The output is false, '0', if the inputs are not the same, differ.

.. math::

  z = (x \oplus y)'

::

  x, y    z         z'
  input   output    output
  0  0    0         1
  0  1    1         0
  1  0    1         0
  1  1    0         1


Negative AND Gate
-----------------------
  Negating means to NOT the output/result, which is not the same as NOT'ing the input.
  Negating the input of an AND gate does not produce the same result as negating the output/result of an AND gate.

  Negating the input of an AND gate is called a 'Negative AND' gate.
  Negative AND is not the same as NAND.
  Negative AND is equivalent to NOR


::

  x, y    x', y'    z=X'Y'
  input             output
  0  0    1  1      1           you're inputs are 0, 0 but you negate both to become 1, 1 for the AND gate, which results in a 1. 
  0  1    1  0      0
  1  0    0  1      0
  1  1    0  0      0


Negative OR Gate
-----------------------
  Negative OR is not the same as NOR
  Negative OR is equivalent to NAND

::

  x, y    x',y'    z=A'+ B'
  input            output
  0  0    1  1     1
  0  1    1  0     1
  1  0    0  1     1
  1  1    0  0     0



These last two examples (regarding negative inputs) are DeMorgan's Law.

::

  X'Y' = (X+Y)'
  and
  X'+ Y' = (XY)'





Circuit Analysis, Implementation and Design
================================================

Boolean Algebra
-------------------------------

Truth Table
-------------------------------

Gate-level Minimization
-------------------------------








Combinatorial Components
=======================================
Using logic gates, we create more useful functions.
NOTE: that while we talk about gates to create these functions, an FPGA will actually use its CLB (LUTs and MUX) or dedicated hardware (DSP) to realize it.


Multiplexer
-------------------------------



Demultiplexer
-------------------------------

Encoder
-------------------------------

Decoder
-------------------------------

Adder
-------------------------------
This is an add operator

.. code-block:: vhdl
  :linenos:    

    signal A, B : std_logic_vector(N downto 0);
    signal sum : std_logic_vector(N+1 downto 0);

    process(A,B) begin
        sum <= A + B;
    end process;


Subtractor
-------------------------------
This is a subtraction operator

.. code-block:: vhdl
  :linenos:    

    signal A, B : std_logic_vector(N downto 0);
    signal diff : std_logic_vector(N+1 downto 0);

    process(A,B) begin
        diff <= A - B;
    end process;


Comparator
-------------------------------

Parity Gen and Check
-------------------------------

Multiplier
-------------------------------
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



Tristate
-------------------------------


:: Tristates

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




ALU
-------------------------------
Create/ show a simple one. That utilizes enc/dec, add/sub

  .. code-block:: vhdl
  :linenos:    

