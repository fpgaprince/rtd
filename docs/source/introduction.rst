Introduction
************************

HDL is often taught from an digital design perspective, with the end goal of designing
a chip/ASIC. While the FPGA and ASIC share similar design/development approach..
I don't think there is enough emphasis or focus on the dissimilarity, differentiation..

You could say HDL in ASIC design has more freedom.
The RTL design has more freedom. The implementation has more freedom.
They have this freedom and flexibility for customization
and the become "APPLICATION SPECIFIC"!

FPGAs on the other hand do not. Most of your gate level hardware are already provided.
You are creating some surrounding logic, function, glue logic.. whatever..
but when synthesis comes around and how things are implemented.
You are incredibly limited! in comparison to ASICs.
But this is a pro and con, you dont have to worry about the physical implementation 
as much or to the same degree, you can focus more on the logic design/RTL design..
functionality.. thus the turn around time for a prototype or development is shorter.

While you have freedom in an ASIC design, it is unlikely you will develop
code or hdl from the gate level, unless you're starting from scratch.
In most case, your company, firm or whatever group, will have standard cells or parts
they will want to you to use.

Say you want to use a JK flip flop, the HDL language will allow you to describe it.
ASICs may use it, you may add it, or it may already be available.
When this info is passed to the physical designer, they too will probably already
have the available part to use (since it is so basic). But in the end..
you JKFF will look like the schematic JK FF. It is true.

FPGA's HW architecture dont have JK flip flops. only D flops and LUTs..
So while you code up the JK flip flop, it's actually going to be implemented as D flops with 
whatever surrounding logic to mimic the JK FF. it is not a true JKFF.

There is a difference in digital design and fpga design.
Digital design encompasses the greater whole. FPGA design is a subset.
You will come across many digital design or digital logic concept or whatever..
but only a subset may be applicable.
some times they will talk from a 'historical' perspective, just for completeness or whatever
but not specifically tell you where or if it's even applicable.

Because I have done alot of this on my own, I am aware of it now and as i write 
everything.. I will do my best to provide some historical information for appreciation,
but at the same time clearly state whether it is applicable to FPGAs.
My main focus is FPGA, HDL and their applications.
My purpose is to create a bridge I feel is not there.





something something

.. epigraph::
    
    "Always."
    --nibbles, the half byte prince

.. hightlights::
    
    "it wasn't easy. it never was."
    --nibbles, the half byte prince

.. pull-quote::
    
    "Always."
    --nibbles, the half byte prince

.. tip::

    "You will face many defeats in life, never let yourself be defeated."

.. hint::

    "You will face many defeats in life, never let yourself be defeated."

.. important::

    "Always two there are, no more, no less. A master and an apprentice."




.. caution::

    "Always two there are, no more, no less. A master and an apprentice."

.. warning::

    "Always two there are, no more, no less. A master and an apprentice."

.. attention::

    "Always two there are, no more, no less. A master and an apprentice."        



.. error::

    "The bandpass."

.. danger::

    "The bandpass."





.. note::

    wtf.


.. admonition:: what does this 

    it does this.    



::
    
    read a shit ton of wikis
    read a shit ton of books
    read a shit ton of forums
    read a shit ton of guides
    watch a shit ton of youtube
    watch a shit ton of lectures
    attend a shit ton of seminars
    read a shit ton of tutorials
    read a shit ton of datasheets
    read a shit ton of white papers
    read a shit ton of IEEE journals
    read a shit ton of technical papers
    fail a shit ton of time.
    get laughed at.

    5hr sleeps
    14hr days
    no social life..

    when i finally make it..
    dont tell me i was lucky.
    "it wasn't easy. it never was."


::
        
    ####################################
    Part -- Number Signs above and below
    ####################################

    with overline, for parts

    ************************************
    Chapter -- Asterisks above and below
    ************************************

    with overline, for chapters

    Title -- Number Signs
    #####################

    Suptitle -- Asterisks
    *********************

    Section -- Equal Signs
    ======================

    Subsection -- Hyphens
    ---------------------

    Subsubsection -- Circumflex
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Paragraph -- Double Quotes
    """"""""""""""""""""""""""    