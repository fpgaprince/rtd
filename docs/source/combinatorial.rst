Combinatorial
===============


This is an add operator

.. code-block:: vhdl

    signal A, B : std_logic_vector(7 downto 0);
    signal sum : std_logic_vector(8 downto 0);

    process(A,B) begin
        sum <= A + B;
    end process;
