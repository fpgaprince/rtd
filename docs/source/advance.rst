Advance
***********************

In the way you write HDL..

Speed
    Throughput 
        data or bits per cycel.
        sequential vs. pipelined.. shared resources vs. duplicating resources (increases area)

    Latency
        Cycle count.
        Remove pipeline registers reduces latency, because each register in the path introduces an additional cycle.
        Harder to meet timing

    Timing
        Pipeline the design. in otherwords.. Adding register layers.. 
            Pipelining increase fmax. Decrease delay requirements from register to register.
        Parallelize the design. Analyze function/algorithm, break up into smaller chunks/operations that can be done in parallel.
        Reducing logic level/stages.

Area
    not pipelining. sharing logic resources. remove duplicate logic. use/add control logic, state machine to share sources.
    there are different types of resources. there are the actual FF and LUT that are used to implement your combo logic.
    there are LUT made operations (ie. adder, multiplier, shift) that can be shared, 
    some resources can be pull up to a higher level/hierarchy and be shared across modules, from a global perspective. 
    so resource at the 'module' or component level like clocks and timers..
 
    you do not need a reset for every flip flop or sequential element, it depends what you are doing.
        for instance, you dont need to reset a shift register, if you know you're not going to get valid data until a later time.
        and the circuit/or whatever down stream knows this too. the shift will eventually shift out the initial values set by the FPGA.
        or the garbage input until you get valid.
    
    to use dedicated shift registers, you cannot have a reset signal, they dont have a reset signal. if you do, the tool will
    try to (synth/imp -> syn/imp -> symp) LUT+FF based shift registers. which will take up more resources/area than using dedicated hw.
    more area.

    
Power

FIFO
=======================
    This basic sequential circuit/component/module.. is increadibly important in many application. 
    It was probably first introduced in data structure with queue and stack alogorithm/data storage.
    Its write/read functionality are quite straightforward in nature when everything is within the same clock domain,
    But when the write is in one domain and the reads are in another, it complicates things a little, a little in the sense that
    is it a known issue, we are aware of it, and a way to handle it has been developed. The different domains complicate things
    because we need to track the pointer, which means we need to pass the pointer value back and forth when a write or a read 
    occurs.
    We'll keep it brief here and discuss it more in the CDC section.

Below is a quick and dirty simulation of the write and read pointers.

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgzCAMB0l3BWEBGMsCcB2ALMhYAmZSADmRIDZkQFIaa6EBTAWmWQChkLsUwKU2XuWFCQvXnUb0AZgEMANgGcmUDrnTgCJQRLi6o4jgHcQBQgYIIByMZBNmLyTAIKYCKF2tPmPBUmYkOv469j4WBNh0YJC8kVIOTmKoNnYcADJ8rgHWZgFSIPLKqkj2AB7gCNTsHvge7EhxvADqAEoAOkoACgAqrQD0AMYA9gCuAHYALkwAThwV6FgosSjOEMSY4ma8rQAinb0DIxPTcxVsCLws2JvOm9cS2yAKTJOdAHKd7QCOnWAANJ0CAA9MBfX5KEidAC2TGhnQUw0GckmAEthuN5st-OAyKtsBAwCRHpEQFClD9OmUAETEODUrHEAgeXDCWzUXCbJogTDgqnUyDsZAM5DoATYILgFYUfQxOJGHy5WxxXJy7xmVUrCU6NVhMzuTyuA1gfjqtweE3iyWWs2SkKBHUUUIObXgJ0Ot3O0yuqLRLX6PVq31SpoJUxq+JaYJRM1KsSEHTKs0G5wCBOG9Xp+3aYL5BxYbI6dCm+169A41MgAsZssrJPVpNlhB+GPVyNNjzuIvN7ZhqslgLFgQUMXq8t0SvjkAUHhjutidDSiz2TKYYl5HSYFalwxFFT0PVOidiNeiSQcJQ0d0padOU0TkCTGajJgOIJ0SPoHvtt8kD+DgcvTJP8MynSs9XfAxFzPNQNCrLwk2ICUDDobAuFnU8DBIJJHkkA9d0UfdA20cRZyEVDZz1ciaBIsAvGbIDqOwUcwB7ZiBEDLULCY5cOAASXEGMCRZSVhMMGAkAQfjBIoiRRMoqBoEk6SmNHH1RykJSaBUmMGPESU9M05TMldaxUJyGVDGoPcSkzLiLSXDxiJ0bBZ3TGdz3DNiWJ7EcOMSejaK8Ls7N4CgLGg28nMSEiPKrHE4sDXzRyHacNICgQQq-TsSPsOCKFVd0Qv4UIFRodcSunbhPXVBB12DChSWDPU6okCxwpZXjTFa0iwqEyiuFoadkObOhMGQWoKy2ZTTB4RhpX6zzhp0KoPA6mgJvVdbVqi8QuuWmidEa3hDIcY7DunJqAzO6rKqoAR8H82bqseg7XsPXSFpWlZD1u90CrTd1DyuugAfEa7ZtyMT1rEj7ZOnKGBoqTATWnSAkD-I6Am5AAJPklBkUYFAULEUZOihNmJSSty2Ul0nx8ZhjeAmiZJgBZHlNtGnke25j8lK4NTJTYcs0boEW-DKiMYzVfbXQsWXou9SUPxV21SpzDdkw8FhuOF-bzRAXW-BTLw9SsAQWDI4WBsVS3ZwtlCMn0nQJfB13RScgjigPZ3XTYEiog93Lvf3Uo-eF7hzI9yyChs32TOFtSAhYDSUEKQjbPsPBeGyo2JoneB86mr2pIEulxYL5ZkIDgoJO07r1wD7sdYmoCeuNlACFHTuWqb0cNh19LG6uWd2C8K2lsi+sVjYTbayuGoqx7OfovLquWEldh3U30r66knPlgNXfVhxE-qFL6SJtJFglUN2+OMU5TD-Hy275vpUzEMMu+DEFhSVQKLf+eF96DWEN3S2ACwB-wAV-Rg+YKxeCnJvPsyCQKDyNiBPUr8jbIVStcIC+C8GATHN+VsK9qrYIgfnAQec2D+TwMeGM59aBXC3tNBufAgEAOosA9UypxY8OYQaKhx877HywQ4CaEimHi0kaYARRsB7cFdsPVYO9lE7xVlI2IwdZHFz7Io2uuhK4-Q4BzRhbDEyXCsYYAgAsKh4CJEbHs3BUC4M0LjfGhNibO2sImU0r0bwPnjuHTIKCsg0InPedOoS1DnFNESaJvAiQQG5KiGQnQZgABN8bGBmICFQ0IAAOkwACejIm43n4NQNgqN0mZKUPkr4xTOjIHxjkwpPiSYVFwEgFwEA-xjRnLTXgwwZjQGgJ0DJnR8ksByfjNg+M8BfApBCGkQphTeNZoNSu4oxH7PqFseBPhsbVXtLqBwjsIwBEuQosQQhghNWQubZ5TyUn3iuaSG0hsbTmxlu6SMEo+xAvQQ8+RBgdqOx2ubXIUKoYQw1OKWU-o+xBhwntJWBhcCFnEJQqRDy3KB1tpUFkA8HlqLog9EiSZTo+GtICgFQF6H6QnFaQx7KUBWiAtVV0BpXR6hZQKl26pUJqz5g4RgOIDQStMEKse4oSW8oVeIXI2DxS5H5WqhwQq1WqqeoYbAersCkj1KhUk-LTXmJcYc-OWoRFmAFi-B5ACtSwMvs6iQSotSf1qNpT1IqkKBq-s-S4kKKwrG5hfegP8g0mt4JakBWlY0+syiyPVoDy5aklPytWmbq40TGpNOuyasRsH0NYGwFMryeKeHjNZnQ4SlLKYU+mDalCM2Zk28puzdpJiPAYaNJy+2+QCHgLFMprFrTHWbaSk6zDVXneBJ+nD51EGHAEQ2h5N0HP1Fih+4hd1bp1Tedd+dTQygSAJOprhqo3prCuqScqbzjvPTYWdz6bArxjK+7OQ0WVJgxUO7Sl4Ik3gAzE6gT4XwntNK+64E4eyCpvJezm06+zjXQ2hwt8S7UQCWAhfQ3Imn4zkEoFQMxmb5NRNMLEdVEyQAgC4YQkBxRPBI+2sjFHmYzCYHIbJdGc2DOgTyNjpIMQKDKVkvjuSlAzKUO8AA8j0RtJSe3nGIEgEZxBNAjlGSACTUmmkzBo0waZjSlMqZZr4xxgpGiUBQLQMVtbSSTAABaogpHJrzSgynjEGG5mYGIxhKH6EoOQsJOiDERIMAA1p0AAYnxBLimotjCmLMToHAgA" 
            title="Ring Counter" >
        </iframe>
    </div>
        
---------


Pipeline
=======================
*   Pipelining the design, can increase fmax.
*   Help with Timing
*   Increases latency
*   Increases area

Clock Domain Crossing
=======================
    What is a clock domain. A domain is basically what clock all the registers or set of registers/components/modules are clocked with.
    You have clock domain which are multiples/factors of the other. So they are synchronous.
    You have completely different clock domain in which the two are asynchronous, meaning neither have information on the other.
    The information, meaning the phase relationship between the two or more clock domains. 
    Meaning you can have two domains of the same frequency.. but if the phase information/relationship is unknown,
    you cannot guarantee the setup/hold time requirements for either domain clock edges to be met.
    Thus metastability is probable.

    Discuss metastability here again.

    Double Flop. Double Register. Synchronize Flip Flop. All the same, diff names.
    FIFO
    Phase Control, by using the FPGA's PLL/DLL, we can have multiples/factors of an input clock. The FPGA can monitor or determine the skew across the FPGA
    with finer granularity? or control. The jitter will not be an issue? because it is internal and pre-defined in the spec of the PLL/DLL.

    Create CDC blocks/modules to organize all CDC techniques. Have these modules between the two modules clock by different clocks. Partitioning.

Slower to faster
-----------------------

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcBmWBOA7AFjA5AmMSADjGIDYIFIQlraBTAWjDAChcllIsR8N8ILHD4CoUDgiTlhowRmTk54yGwBKIciRDJivBGEG7eEQfhH5oSS0howE68Fl7deWYjp7g+4C1b7+dlYcxB5gGEr4svhRfLJEQuD4bADuTi5eYM5xdqnpOeARBapprsr8ZmIl+WW1XtU4kWIyNBUSaQpN8giVgqqcIBS8bWhayrlpLZ68U8btmrJzGD06evPLRl4bq7zVo61imF0SWDEgnUIeGGvuKrCQZv4Ok9pzs2v99ETa4UqsmUVWuIHABJQZgJS3IaXO50PLQtrQiETQYycBjb5hMbVf4mIqsRSFJR7MbIQmYnSEnFwDxkv408BoPqSJDbRG3NoovQeRFozl5bZzaFzarCtbC+psAAefEgaEKyEGyDxkLiIAAJgwAC4MADGWoAlgA7ADmAB0AM4W40mgA2DEtACMDVrLbqAPZGrUAJ3dtst1pNRoAhraLZaAGa+gC2Adt7pSlq17sjwYtrot6vd0eDxpZfFiNAIdl8hfztxoWV2pd2eWL4iwBBUeRi1arzbSFZATCbKPbUUr2VYzNK5h0RjHw-m9an7anOKHhhqzJlBEEWDQNAwkAwQjQiuGvC1AAsDeHreeje6MxH3d6Az6GMHozaAwxvQbQ5b1cGtcGAISAdK440M4SgKOuG6JLEFrHu6ACutrqpaV4ZsewYAG4OhajrBrqADWSYpjheGERaYAAOTnnelqQFRwEbh4Ui8MQCDylIu6HiAuHWrqlr4JaABigmWghWoAA7wRmZ5Jse2H2lh-pWgAnkaurAcQChJIIhjhEkSBccG6rqq+6anueMlmdhDDqia2Gajq+oGp6bCOqiLGVq2QjbhIbncoMNBaBAWAYLuqhuVgaIQkkyC7ngirhUITYsEuTAhUI6WfJWDKNOARBuNFQI0M8IBHMoZXCCiFUiBSlXzP5dKDLcjYjk1Hgtb42gdTi+VCNFrArLlqgymgawsJWeBKEwnFqjZdnftqerSeeJruu6yEWre95WvGibpsREZphmAAUloAHyWmAVgAPT4FKqbpu+ACUwH5bSYSNu1wVqlmDCXtelopHeZFbQ9GbJnGCayQhJrHnkuVtHV-JpKMOgrPgoRoyufBgIqWj0hgEBaPKXEADIAKIAGrk6TloAMoAJoAHIAMKWsGRobeTAAiADi5OWtz5MACrkyzwv08zbMWgAgmoAsWoJADyaj06TSsAOqWsLStCTLdMSxa3NKwAsjLIJM0BMqEDM2TXB4MgzbELqWpZJ7WWmBrvqJRoMP+Tp8ZtR2AwatpKRaz7ifarsZtGiGGlH2GGtGf1sO6OgLA2RCKrY9xwEcCDkPgtg+IqyBp6VmegdntBQHncoRIXxfiII8rl+nghotXkA53X8AN+QTcl2YOgVwkXd9T3tcwP3BdF8Pvijx3SgTzgU+57Pjfzy3fBKOXQA" 
            title="Ring Counter" >
        </iframe>
    </div>
        
---------


Faster to Slower
-----------------------

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWEBOaB2AHAZmcjAWBLANgwCYwsQFJrraEBTAWjDACgwEktJ8QyaMiHxwBQqFE7cQxUeOFoSCyZHYAlWZAwgsBamGF7+EYWDFloSS0lowEGkK0O6+TsttcmBr2jYFWqlacGDrMWMIeOmDEAp7mIiAY7ADuTnJe6fxRUmnMGTnhkZ5qabzZEoKREqVZmeWZtfgxKnJ+NakgSrFVXQjVwmpcSBgFEsjE7YO5svINbbr6tQvGfUZLnWj9mVvr-LUTU+BwOr1q+GRm5vwIyFfbt9MwcJGBDmmTOqsrGwCS4GB9I9wGQItQ7kEkO8kmNhKMTJMZvDwIjzPFEbU2G4wGhYmxlDjYpiTio0dEIUMZLsVARTjVqJ1aTTYTNqatkatahz9By3GoAB5OZqLWgRCB6KjZfgAWQAwgAFAA6AGcALYAVwANgAXACWKoAxgBPA2axgqgAOAENtQALFUAOwA9iqAGaMRgAEwARlaDQBrdiCiLCfDIWhoSBoETISUCfh23XKlVJx1O7Vup0AJxVyu1WcYVtVuodAHNc4ws7qrZqVZ6bVaAITNoO6CgiGhdLCSoiJMj8ZW2p1az1pjODq0AN3Nyt9AZV2pds79-pVYAA5MnldmVZBN62wzpuPwMLdqAho1KQL7lbqDSqyCqAGJPlXD7UW9Xj1N520zs3TrWyrKkaDoGq25jbGQxB4jgPTEMgfb8FanqeiW5a-j+P52jOXqljOnqMNqjAGnqToOuw3pJPgOgYLQkwQPgaDRk0YjdrEoi0GA+D7J0nHgDx8ZcYJTQtL0zR4i4omSZE8hsIMIQmIJ8ngLiAJmJA-bgHxYkSPxZydISQmqT0JSGcpLgTOpMxWb0dkdB8UpcWp-Z2J0VkqbZHRcCYJJGViJhqX4dAOMMIJHmQpxaf0OhuT5bbUJF4WJbFPgMOw-ysLECAuGCOVPG8GVOC0CCCXlIlQIVjnGRkCzLPwCzMDRsxuXkzWNc1pW8W1R6CVl1AiZ0lw3ElDQxTMw0pQIWn4BktSTbN-BNToi0zMtIgZOt+VrZ1Lj9dtmJJQgiLOMIx2tcVLjnZdRh8q2zj0TBKJUDBiFXsqRYzq66pgWRDoqlaW44SqGr8vdhAiElpAiFgjHxiAn6asqM4gWBnSnZk+T8A0AoCAgOgwbEBBIK9SEgAAKgAEr8ADKKrygAqgAMjTACiKZbq6O7Kk+ACCNPkyqAAiADy0q878AByKrkyLKo00zIsAOrC2LEuS-dXBUGwIhbAJZOLrm+ZEQa9rbl+C5-paWrIyDhYOluNPyuorO80Llszga5H5k6QG3qWDo1tA0Ca6VIg6EoDBw1pgMAyqBbKlq2oADQe9bSOe7qWYGuqurapu6e28qBaqlaJZbiWcfKqWurTv9wHaja-7kfhOa-uqW4AER5gW2qm+hnfsE6ugopIzSaXQzzwMguLHWQtg+FQWBD5Do+0OPZ2VfAkAz8Qc8L6GRgr4hLTr+Ym9T3Au-75IwiIcvw8JKfIjn5PsDT7PxDz7fxy6CvYAnyJC-Ceth35X0-t-YKAC-6PyQM-Deb9t7Xy-gfcAPAV7tnga-UBSCIGoPbA-HwWCQFbw-nvFBP8j5AA" 
            title="Ring Counter" >
        </iframe>
    </div>
        
---------





Reset 
=======================

    Dedicated BRAM and DSP should be synchronously reset because these are dedicated HW in the FPGA. They were 'fabricated' that way, so in order
    to use them correctly.. their resets should be syncrhronous.

    SRL, no reset. Likewise.. frabricated with NO reset pin/input. Therefore if you try to add one, the tool will synthesize extra surrounding logic
    to implement what you, the designer, wants.

    Using set/reset pins can prevent combinatorial logic optimization.

    Asynchronous Reset vs. Synchronous Reset
    Advantage/Disadvantages
    Asynchronous can happen anytime, you dont care about the clock edges. Synchronous is like all the other signals we've dealt with,
    the clock edge we register the reset signal.
    
    The problem with async reset is in releasing the reset signal, starting operation, in relation to the clock. The point is, there is no relation. So when it is released, 
    all the signals in the FPGA start going to work without knowledge of the clock, which creates a recipe for disaster in a synchronous design.
    When we dont have an idea of the clock periods, or edges, we cannot guarantee our setup/hold times, we that is not guaranteed,
    metastability is highly probable.

    The problem with sync reset, is the requirement for a clock. IF for some reason we lose the clock we wont register a reset. Or if logic is spread out through the FPGA
    such that the propagation of the clock is not equal in different areas, we wont reset all at the same time. This will create an uncertainty
    in our reset state/condition.

    So async issue is the end, and sync's issue is the beginning. To combat this, what is called 'async assertion, sync de-assertion' has been developed/created.
    Async assertion takes care of sync's beginning of requiring a clock to reset, and the sync de-assertion handles, the end of the async to ensure everything
    starts in a known state/value/ at the same time.

    Don't mix async and sync resets, because FF and registers are not fabricated in this way, you will create additional surrounding logic to implement such functionality.

    In regards to fully sync reset and asyc+sync, you need to always synchronize the reset signal the whatever clock domain it is being applied to. 



Clocking
=======================

Static Timing Analysis
=======================

Everything online always tells you.. setup time is the time data needs to be steady/stable at the input pin 
of the flip flop before arrival of clock.
And yes that is true, but they never discuss why this is so. 
I want to do it here..
I add the equations later.
In order to understand why, we have to take a step back and do a deeper dive into flip flops..
what is the DFF/register used by the FPGA.

    I think knowing why something is the way it is helps us better understand what or how.

    1. My experience with FPGA registers have all been with DFF.
        question for self.. why D over SR JK T?
    2. DFF in FPGAs are made with CMOS technology, not TTL.
    3. There are numerous ways to implement a DFF. 
        I will be referencing/using the Master-slave latch to speak of the edge triggered D flip flop.
        Which consists of CMOS inverters and transmission gates.

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWEBOWkwHYwGYeIExgAcERGISCkFApgLRhgBQAMuBgGzhj4gcAs3XtQgAzAIYAbAM40KUJgA8KREBkEYkGcoPyCAIk1Eh8RVZi6nzplFzDQkMSPiMmzIfqqu2U5e49gXAHcTBDseEwxeRmEmEPwooUjeZC5IOJBsSEFUzOyk9JCswR5VYoKM8piPMHDY+LCk-D0KovxqXO9c9IBzULtOfvBkYQUAJUz2n2wp2qh5-mpHeZgEDPxG0qGLBXjErYToiMK3ay9Nm3SASXY6kxbq6lWKJhudvWpm3UWVhxeb8ofTIIXhAp5-NZFEEmH7YDheH4nQ4wz4tMGVfJA7zo+LuLHuHYnOEI6jEjyqInw8mnanpZSEJB0XDA3h0GzfEAAYQAsgB5ADKAB1pCxxAAXADGAAt1ol8SSFNyandPCJjiYHEoKNgTGAkMhkLrVBzOSwANKsW4ovjfJ7gEASGRyRxMABOyqS-DmhPA8CYfS9Ay4geGo3SAHt5nNqF7IDqAvBIMhOGENvNRtgmJGEuA0jVnFBoHqOGmYBAREwgA" 
            title="Ring Counter" >
        </iframe>
    </div>
        
---------

    4. The time for the master to latch the data IS the SETUP TIME.
    5. The shutting off of the first latch/TG is the HOLD TIME.
    6. The time for the input to traverse the inverters to the output is the CLOCK TO Q time.

In the diagram below, I have decreased the inverters slew rate (takes longer to change voltage, go from one state to the other), 
which increases the setup time.
which cuts into the total period and decreases and limits the max frequency.

In other words..

    for a given frequency, if i keep decreasing the slew rate, at some point i wont be able to latch data correctly.

In other words..

    for a given slew rate, if i keep increasing the frequency, eventually the period will be too short and i wont change in time or latch the data correctly!

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWEBOWkwHYwGYeIExgAcERGISCkFApgLRhgBQA7iACztHhj4dch87apCYBJChgBsPPlOGyoUNHDDJ1GzVu4JWgotyHV8BkNmwzRAGXDTF8xSJAAzAIYAbAM40KUJgA8Kbgx2EAwkDHJQoRAAET12MBlGPk5uFL9nfXS7E3STFGToJBhIfCYsvI5DU2QZZHIwYuUyvXwEZN5BDD4M0TZ8HsVBvjq-NmxIULHJ0L69WfACxfmJqcVEzr5+wQ7hmNWzfGoxqrHRAHNd5Ny9tW2-ACUjk5lsY-BLJQUSpRhdAZ3ArtG6WNpDXiGCFdHZVSHXJbcUQSTBbQQHGEteBqLS4jQ6cS2N4WdGhcxfUqqPHUgkSRbkswIPgMkQqHHU7QUBZMswkizcFng5kk-AxQVrMki0zisxSAUkpnysFsRUI9inPY7BBdEEUHUKHbqmS6o1mdaiZ4dYwxK2fJzUH5-ZS6K6mxZuj4iPS20WhVW+8YcU4KNKCA3ezhh6gIXLhlWR3UIBNxigJm3Jr0q-XRnUxQ3BnN8IyZCgFVGlwwxBrgZqlcpZVWLf17MZNEqwcoSeTGH6x+0qdAc3EEtibRQxtFa5YK5bmtqmYtwuyw0zl1Xlnb83lvOXVQNbgRVAQ7btRkBSPbFk+XhQXyd6O+KIjvRxMABG4EjDBkGHMZnUfgfiESDfuA2BEMyAE7LwDgZLwrYwnoMHRAoyGvmwvCHqh+AOFeegNDIAhEGMx74XYW4EXuOzEaCPAkhueg0WeTEMRhOA7uk7FmqE0GQHcXSMEQcyISiQiGKhxAof28CDkOmgElkjB8usSnGi2RTtq0ilceWqmkigjS1h2SFgOsxYpD2mayJZ1n6dBYA8gGjCOSmzlFvxLlWW5Z6CVJgaMGZqF8carlJJWwkinmTBXAFZIqaZZKek8PC7k5YV2k6jr9gCPBmfx6yLPZHy6hZZ72SK+XRJqZEcXRtXUa2BRELBBTUUQ1DwgYHWIWwzVzE1sHLkwzzIAUYyjekFIcNGTr-NFIB9USC2waNfz4WNMhMecjGwV0z69D1KACQJZTCds+ECWNx3nWwyBdON12Bl1T7tYUT27Xwz3zFkTFEeN9SGZp9YLa2dgsRtNZA0hp2KKZ-E3SDIXUExMqYZxvQ4WdfgopJsNiY4WJUnJ+JchhwWw+TeEfrwfAMHxYEAewop+IEMEgAwmC2Mg7OMKEKFxAAOp4ABiwsBJ+Mh0Pg3MWNg7M4RwYYgAAwgAsgA8gAykLquuJ4AAuNAAE5C1Yrj6wAxgAFuL4TUFL3DIEm8tIPzata0LmvuK4ABuNCm+b1tCtu3TMrusJDBR5Hh8HDJVDKjYkijJInhJcjwyzn44CgctgOwuBvfzACKhLwWi7HdQ8lJE8TyAjmBUiV5+GLnarzdY3nq6YvgxTiwgcu4BAAG4HzSvK1YADS4tJIRMbnpG7CN4rMTePrACuAAOQs+wAlgA9t7+v7wAdgAXELq9CwAJubrhCzvx8+0L+t70L+BrwANELFvuAA1s-r9PDHEgGvcWEFuDsGdvBOWkCohKytgfK+2996HxPufTwl9PA331nfTwD8n4G0AcAz+38-4AKFggUBrMpBRDuuebO6pR4xGtq4Y+Fx-ZYNvkLI2O8LhW31kLN8NBnB7yNhwnheC2FCxoFfdhQs97OFIb-MBCsuCcUZnQ-mLC2EcOwbg1wzhDYm08BIh+FxpGyI4QopR08HBMnINgX8FBJjL1CM4AAjkLFgeshauCNnvNex8kGeAQEQK2AAvJgNhywMgcCycALgPDeF8KIPeZhPjfFMnLaukBpDS2wMgSBuB2iE0gARDoJTjDpOwEwNJAkviJEgNkgceTkAFKKbwTS8BylSEqYIJYZhangDKRkh0pk+DtggB1JgQA" 
            title="Ring Counter" >
        </iframe>
    </div>

---------

If I decrease the slew rate of the clock buffers, increasing the time for the "input" clock to reach
the TG, it gives more time for D, the input to change. It increases the hold time. Meaning, data 
must remain stable for this hold time requirement or else any change in D will get passed.
It will get passed because although the rising edge has already arrived at the flop, that rising edge
has NOT arrived at the TG to actually shut off the input. Therefore change can still actually happen!

---------
   
Fan out in general. 
    
    This applies to flip flops driving other registers/logic.
    This applies to clock fan out, hence FPGAs implement global clock routing.
    This applies to reset fan out.

In general the more fanout, the more load on the driving circuit. This stresses the driving circuit
in regards to it having to supply more current.

More load means more capacitance on the line. More capacitance means longer charge/discharge time.
Longer charge/discharge means longer time before input hits threshold for output to switch.
As a result this limits switching frequency.
Chain these effects together over several gates and you have longer propagation delay.
Or longer combinational delay. This eats into your frequency and period,
thus capping/limiting your max frequency or even lowering your max frequency.

In general, your vendor tool should be able to detect high fan out and optimize it.
But you should understand why high fanout can be bad and affect timing.

If you duplicate the driving circuit or logic, you can cut the fanout in half or whatever.

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWEDYCYDMqDsrUE4AOLSAgsJANnWWUmQFMBaMMAKADNwsKQC7UALHT7hw0JDEioOXHmG4hBdeT2XioaVgHdFQkHh5LwqAlG27lJi+Ap1I5lb2UKwV+zsevTnhfYAyIBQCNspytlAR7ACGADYAzvQ09gBK1kHWYKoRehIRMAisAOYZeKjWuMF2rABOIEKWpgLpXhFgcKwAxnXNVk3Bjnaw8JB4o2PjE3gg6NBgRAToCIsUqEFzkKpDbMV9st39pXnmRi3YZS32cdMU3r1wxqbKINHx9KxX6DeKgnX3Fa3PWIJIr7RQ4UEmR5mLq7f6w8GDYYjSYo0ZiFbodDkVAIVzYASuLAaOBsWr1b7BWE-ZTtD5fTC-OgMp4vYE7dIiXYGI4w9IM3YiRHDASolGbYYUBBLMBNPgLT7oImSSCkxnTMq7ZngWnXUyYOjk-UA1lvdnBT6NPkESrQ0FGzVfIVwLEIUXjQzQAgUIKQBCoSACLB4FgIJrElU1NX2vn+1rtHQW9VM2NG9xJ9NG-5pzM-RNZ8xGlqJi4F2NFlNlbMV3Xqsw6M4PdMtNg6XYtBDhEutmPIcLM8xU4Id-jUgcxujD9NVkfmstuBxWZsuee1Hq3ddx+xdZuLxeHJ1wEVu911aB4P14X3OlVEcUR4rNw6nEhHVJr1qLxTIAie0yodT-rk+RjsEjDpJOYGVKWdCQTWsH2GS9ywbs8HaluoLIekzBZMq8BHseoybP6HZ+vgkDoBs2B4EqWwgihmSgnYZh0qYyFIekTEmtBtZGvBrAAB4gIw1p1GU-oQAISDBD8HQxAA1gAOnEyQAMJKQALgA9kp1T0AkAC2ABGMT0Dp9CxEpslyQJQkiasci4ooFBTNJwRxFoACW6kdAAFkpHkAHZKfpmm6UpABEhRROpenhTZwnSYQ4BhhREm6CAUUxXEwWaQAJvQJm5UpUTZcpKnxUQ0wdlVRKLC56UhWFcTRAFmkAK7qUpCkAI45U1HRtdUukBZ1cS5dUHkAG6mXEundW1Hm6blFV6gsYJIOgXp1A1oUzS17WjT1SmFLp0X0NUlk+VE1SFDN6kefpbyCcJLltIoBAamA1CuRlp0xRdcS+ddt0aQ9M1HXEMSaVo53BVE-FKew3WsJpgQ2NkbSVkMcDcPg6B4JJWI4hoEDKCj0zeFkeIE6ekxYAQoxSG0d4qq05MMgxBqY0ksxs5t6UAGKk+GeEEWMLPImLUzMCAKlRAADlEHReVEAUdG8-MCGUQvTNt-owRAAtzW19BqwAnqwQA" 
            title="Ring Counter" >
        </iframe>
    </div>

---------

Positive hold time, data cannot change after the clock arrives

Negative Hold Time. data cannot change before the clock arrives
    isn't this like setup time?

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.edn.com/wp-content/uploads/media-1158084-296936-setup-and-hold-fig8.jpg" 
            title="Ring Counter" >
        </iframe>
    </div>

---------



Timing Closure
=======================



Somewhere
=======================
Duplicate logic to reduce fan out (from a register)
    Helps with timing. easier to route, but increases area.

Logic flattening. Understanding the nature of the function/algorithm from a system level.
Knowing the range of input/output? 
Register balancing.

Clock gating
===============
    No clock gating in an FPGA. you just use enables. You enable/disable a flip flop/register.

Division
====================


Floating Point 
====================


IDK
====================
I hadn't really thought about it before but.. because we use LUTs to capture logic functions.
We are no longer using gates. 
We are using SRAM.
Therefore the prop delay is of the SRAM and not the actual function or gate as taught in digital logic courses.
Which also means.. the delay is constant for all function using that LUT.
