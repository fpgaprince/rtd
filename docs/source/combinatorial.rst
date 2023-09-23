Combinatorial
#################

Basically combinatorial circuits are not clocked and have no memory capability.

Boolean Algebra, Circuit, Truth Table
**********************************************

Logic Gates 
***********************
(AND, OR, NOT, XOR, NAND), logic operator
In FPGA, you are not actually connecting gates, you capture the boolean expression
and store it LUT, which is basically SRAM. The SRAM is configured at bootup.


Multiplexer/Demultiplexer
**********************************************

Encoder
***********************

Decoder
***********************

Adder
***********************

Subtractor
***********************

Comparator
***********************

This is an add operator

.. code-block:: vhdl
  :linenos:    

    signal A, B : std_logic_vector(7 downto 0);
    signal sum : std_logic_vector(8 downto 0);

    process(A,B) begin
        sum <= A + B;
    end process;
