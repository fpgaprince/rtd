Combinatorial Circuits
************************************************

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


Combinatorial Analysis and IMP
=======================================

Boolean Algebra
---------------------

Gate-level Minimization
---------------------








Combinatorial Functions?
************************************************

Multiplexer
=======================================

Demultiplexer
=======================================

Encoder
=======================================

Decoder
=======================================

Adder
=======================================
This is an add operator

.. code-block:: vhdl
  :linenos:    

    signal A, B : std_logic_vector(N downto 0);
    signal sum : std_logic_vector(N+1 downto 0);

    process(A,B) begin
        sum <= A + B;
    end process;


Subtractor
=======================================
This is a subtraction operator

.. code-block:: vhdl
  :linenos:    

    signal A, B : std_logic_vector(N downto 0);
    signal diff : std_logic_vector(N+1 downto 0);

    process(A,B) begin
        diff <= A - B;
    end process;


Comparator
=======================================

Parity Gen and Check
=======================================

