Applications
************************

Deeper knowledge in these area will aid in understanding applications of FPGAs.
Remember.. FPGAs are just a means to an end.

Because it is versatile, it is also a cross-section of many different engineering subjects/topics.
NOTE ONLY COVER THAT WHICH YOU'VE DONE. 
other areas will be brief.



Digital Systems
=======================
The world is analog. We need a means to go to and fro.

    DAC

    ADC

Computer Architecture
=======================

Signals and System
=======================

    DSP (Digital Signal Processing)

    Image and Video Processing

Wired/Wireless Communication
=======================

    Encoding
    
    Mapping
    
    Filter
    
    Modulation

    Demodulating

    Decoding



Networking    
=======================
    Ethernet
::

    MAC - media access controller. This is the part of the system which converts a packet from the OS into a stream of bytes to be put on the wire (or fibre). Often interfaces to the host processor over something like PCI Express (for example).
    PHY - physical layer - converts a stream of bytes from the MAC into signals on one or more wires or fibres.
    MII - media independent interface. Just a standard set of pins between the MAC and the PHY, so that the MAC doesn't have to know or care what the physical medium is, and the PHY doesn't have to know or care how the host processor interface looks.
    The MII was standardised a long time ago and supports 100Mbit/sec speeds. A version using less pins is also available, RMII ('R' for reduced).

    For gigabit speeds, the GMII ('G' for gigabit) interface is used, with a reduced pincount version called RGMII. A very reduced pincount version called SGMII is also available ('S' for serial) which requires special capabilities on the IO pins of the MAC, whereas the other xMIIs are relatively conventional logic signals.    



    WIFI


Algorithm
=======================
    Data compression, like music/audio and video and image

Information Theory
=======================
|   BCH Encoder
|   LDPC Encoder
|   CRC

Data Structure
=======================


Controls
=======================





Organize...
=======================

|   LFSR
|   Pseudo random binary sequence

