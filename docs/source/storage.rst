Data Storage Elements
************************


Latches
======================

SR Latch
-----------

D Latch
-----------


Flip Flops (FF)
======================


D Flip Flops (DFF)
-----------------

JK Flip Flops
-----------------

T Flip Flops
-----------------



Register
================================

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


Memory
================================

Read-Only Memory (ROM)
================================

Random Access Memory (RAM)
================================