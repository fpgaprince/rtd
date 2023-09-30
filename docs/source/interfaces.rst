************************
Digital Interfaces
************************
It is just a means to transport/transfer data from one place to another.

Depending on your system and application, 
what you are trying to interface to and the performance requirement.
Data rate and distance. 
it will dictact what is adequate/necessary for your design.

will need a means to access/acquire data.
we will manipulate. process it in some way.
we need to either return the data. or act on the data. store the data.


JTAG
##########################


UART
##########################


SPI
##########################

Quad SPI
##########################
::

    QSPI employs a 4-wire configuration, similar to SPI, but utilizes parallel data lines 
    (DQ0-DQ3) to achieve quad data transfer. It supports higher clock frequencies and 
    provides increased data throughput compared to traditional SPI. 
    QSPI uses Double Data Rate (DDR) techniques to further improve performance.

I2C
##########################


VGA
##########################


HDMI
##########################


Display Port
##########################


USB
##########################


PCIe
##########################


Ethernet
##########################
    10/100/1G

    PCS/PMA

    MAC

    10G

    40G/50G

::
        
    MAC - media access controller. This is the part of the system which converts a packet from the OS into a stream of bytes to be put on the wire (or fibre). Often interfaces to the host processor over something like PCI Express (for example).
    PHY - physical layer - converts a stream of bytes from the MAC into signals on one or more wires or fibres.
    MII - media independent interface. Just a standard set of pins between the MAC and the PHY, so that the MAC doesn't have to know or care what the physical medium is, and the PHY doesn't have to know or care how the host processor interface looks.
    The MII was standardised a long time ago and supports 100Mbit/sec speeds. A version using less pins is also available, RMII ('R' for reduced).

    For gigabit speeds, the GMII ('G' for gigabit) interface is used, with a reduced pincount version called RGMII. A very reduced pincount version called SGMII is also available ('S' for serial) which requires special capabilities on the IO pins of the MAC, whereas the other xMIIs are relatively conventional logic signals.

    The 100Mbps versions of the MII (15-pin MII and nine-pin Reduced MII [RMII]) are complemented by 1Gbps versions, which include Reduced Gigabit MII (RGMII) and Serial Gigabit MII (SGMII). RGMII is a 12-pin interface, while SGMII can operate as either a four- or six-pin interface.


SERDES
##########################

DDR
##########################

SD
##########################

CAN
##########################

Bluetooth
##########################

WIFI
##########################


Audio
##########################



Sensors?
=======================
    
    Gyro

    Accelerometer

    Inertial

    image/video - camera

    Temp 

    Display


RS232 
=======================
    Single ended
        3 wires (TX, RX, GND)
            susceptible to noise!
    
    Short distance <50ft (15m)
    "PC serial port", commonly found on back of PC. 
    Direct point to point between two devices
    Full duplex.
    
    Often used for UART, debug, testingRS232 to USB, FTDI, UART USB adapters
    RS232 to USB, FTDI, UART USB adapters

    

RS422
=======================
    4 wires per device (Tx_p, Tx_n, Rx_p, Rx_n,) differential
        _p: positive, _n: negative
        host's 4 wires will 'fanout' to all peripheral devices.
    Longer distance - ~500ft to 4k?
    Multi devices ~10?
        Each with unique addressing
        there is one host/master and # peripheral devices
    There needs to be some agreement/understanding between all device on how to share the line.
    Full Duplex, but only one slave talk at a time.

RS485  
=======================
    new, replaced rs422.
    2 wire sytem, differential. (line_p, line_n)
    Multiple devices. ~32
    Master and slave share the two wire lines, therefore only
    one can talk at a time. handshake needs to be set up.
    This is called half duplex.
    500ft to 4k?

Ethernet requires more complex wiring and networking infrastructure compared to RS485 or RS232

.. ::note

    Simplex - tx only.
    Half-duplex - transmit/receive, one at a time.
    Full-dplex - transmit/receive, same time.



|   FMC?
|   HMC?
|   DMA?
|   NAND
|   AXIe
|   PXIe