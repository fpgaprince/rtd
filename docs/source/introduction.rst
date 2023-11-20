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


There is also a intersection between microcontrollers and FPGA.
In fact, an FPGA can do whatever a uC can do, functionally, but most likely 
requiring more power. 

With uC, you can just pick up C and kind of be on your way..
With FPGAs, I dont think you can just pick up HDL and be on your way..
I have learned both and uC, C was much easier to pick up and create something.
FPGA has grown in popularity/usage and vendors have created easier methods/entry point.
but in general, learning both from the ground up C was easier, and what i learned early on.
FPGA/ASIC/RTL all that came at much later time, many undergraduate courses later.

I am not saying one is harder or easier, uC controller development, embedded software and embedded systems
are no trivial task. Like wise using an ARM processor is no trivial task. Each 
have their design/development challenges. Each are professions of their own.

While I would love to understand everything and all of it, it really boils down to
how much time you have and how much time you want to invest into it.

Im sure your journey will introduce you to all of it, but to be an expert in even one is very demanding.

Anyways.. enough about that.. we'll jump into the fundamentals. 

something something?

Actually, a good way i think i learned how to use microcontrollers was through programming and interfacing
them with sensors, start simple and gradually more complex/complicated one. 
I think by doing the same with an FPGA, it will give you an understanding and better feel for it.
You'll learn about the sensor, interfacing and protocol. 
You'll send/request data. process data. and do something useful.

this is the essence of all circuits, whether analog or digital.

we're trying to do something with the data/information. something useful... or just fun.

in recent years the SoC has advance very quickly and the intersection between microprocessors and FPGAs
are greater than ever. What once was just a processors in the embedded system now is a FPGA SOC with a 
processors in the same fabric. It's pretty amazing. Alot of what the processors and microcontroller 
did before, with electromechanical control or reading? sensors are now part of using the FPGA.

So the FPGA engineer now needs to expand his knowledge into the embedded systems domain.
and Embedded engineers are also crossing over into the FPGA realm.


ok done.

not..

at the end of the day.. i view myself as a hardware designer.
i constantly am thinking about the hardware, architecture, signals,
controls, datapath, timing, electrical requirements and limitations.
speed, area, power..
i am aware of the resistance, inductance, capacitance 
frequency impedance components placement routing..

it just happens that i discribe circuit (digital) functionality
thru a language instead of capturing it in a schematic.

i am in the in between, the crossroads.
i am neither this nor that.