************************************************
Combinatorial Circuits
************************************************
or combinational.

Combinatorial circuits have no memory.
They depend only on the present input.

I am going to talk about the logic from an abstract point of view/high level.
and will return to gate level/CMOS implementation at a later time.
since we are not dealing with it in an FPGA.
These chapters may be broken up at a later time, but for the sake of completion they'll
be as is for now.

Basics
##########################

Binary
====================

Logic Functions
====================

Truth Table
====================
A truth table lists/maps out all the input combinations and their resulting output.
It shows the relationship of the output and input.
The output is a function of the inputs. 
For 2 input, you will have 4 combinations. For, 8. power of 2s.

Logic Gates
====================

(NOT, AND, OR, XOR), logic operator
In FPGA, you are not actually connecting gates, you capture the boolean expression and store it LUT, which is basically SRAM. 
The SRAM is configured at bootup.

NOT Gate
-----------------------
The NOT gate inverts whatever value is at its input.

::
  input output
  0     1
  1     0

Remember, these logic gates are to represent the logical operations/functions in Boolean Algebra.
They are to realize the math, in actual hardware.
The basic boolean functions operate on 2 inputs, X and Y.

AND Gate
-----------------------
The output is true, '1' only when both inputs are true, '1'.

::
  x,y   z
  input output
  0,0    0
  0,1    0
  1,0    0
  1,1    1 



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

