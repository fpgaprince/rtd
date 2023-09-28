Combinatorial Circuits
************************************************
or combinational.

Basically combinatorial circuits are not clocked and have no memory capability.



Basics
=======================================

Binary
---------------------

Logic Functions
---------------------

Truth Table
---------------------

Logic Gates
---------------------

(NOT, AND, OR, XOR), logic operator
In FPGA, you are not actually connecting gates, you capture the boolean expression and store it LUT, which is basically SRAM. The SRAM is configured at bootup.


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




Tristate
-------------------------------
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