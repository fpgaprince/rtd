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
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgzCAMB0l3BWEBGMsCcB2ALMhYAmZSADmRIDZkQFIaa6EBTAWmWQChkLsUwKU2XuWFCQvXnSlQQAMwCGAGwDOTKB1zpwBEoIlw9M7BwDuIAoUMEEA5GMinzl5JgEFMBFK-VmLngqTmJLoBug6+lgTYdGCQvFFSjs5iqLb2HAAyfG6BNuaB0goqakgOAB7gCNTsnvie7EjxvADqAEoAOsoACgAqrQD0AMYA9gCuAHYALkwAThwV6FgocSguEMSY4ua8rQAinb0DIxPTcxVsCLws2Jsum9cS2yCKTJOdAHKd7QCOnWAANJ0CAA9MBfX7KEidAC2TGhnUUw0G8kmAEthuN5ssAuAyKtsBAwCRHlEQFDlD9OmUAETEODUrHEAieXDCOzUXCbJogTDgqnUyDsZAM5DoATYYLgFYUAyxeLiRzWNLxPJynzmVUrCW6NXhcweLxuA1gfjq9yeE3iyWWs2S0JBHUUMKObXgJ0Ot3Osyu6IxLUGPVq31SpqJMxqhLaELRM15Oy8Qi6eNmg0uASJw3qjP2nQhAqOLA5XToU32vXoHFpkCFzPllbJmvJ8sIfwxmuR5ueDzFlvbMPV0uBEsCChi9UVuhVicgCg8cf1sToaWWBxZTDE-K6TArMsyIqqeh6p2TsTr0SSDjKGju1Iz5ymycgSYzUZMRzBOiR9C9jvvkifodBy9Ml-0zacqz1D9DCXc91E0atvGTYgJUMOhjG4Xgz0MEhkkeSQZEKJQD0DHRxDnIQ0LnPUKJoUiwG8FtgJo7AxzAXsWIEQMtUsZiVw4ABJcQYwJFlJREgjoCQBABKEyiJDEqioEkmgZOYscfTHKRlOkwSaMY8RJX0rSpMyAzdBsNDchlGRqH3Eos24i1l08EjdGwOcM1nC9w3Y1je1HTikgYujvG7BzeAoSwYLvFyklIrzqxxBLA38sdhxnTSgoEMLvy7UiHHgihVXdML+DCBUzAQDcypnbhPXVKr9DoChSWDPVGvESxIpZPjKo3dyIuEqiuFoGcUJbOhMGQWpKy2RhHB4RhpSG7yxvM6aYpoDaj0sKpPG6zrYrMHhzPi0kjIW86zqa9UqHTd07poB8Frq-AR3G57jpjWhBvMlYjzqmqivu4CWpu4HxADBa8nEg7xKPFaZxh4aKkwE0Z0gJB-10GU3KeAAJPllFkUZFEULE0d4GxNmJKTty2UkMiJ8ZhjeYnSfJgBZHkNomnlez5z9JK4dTJTYCsMbocX-AqkM+zl3qzO0BWjqVz9JX7XMZC1stFQNFgeLFxXzRAA3-FTbw9SVU3yLF4bfDyFg52tptTNdaXId0D3COKQ83bF6a3MCNh8r3Ij7NXJW2Gs6Ive4aQ6Dsv2snd9Tg80lA5HDv28F4XLTemyd4AL2aXJUwS6SlwvlhQkOE+0xwOpDntPGbhqNzNlACDHTv2o7scNlbzK+quOd2G8J3VuihsVjYbaC1nmpq17OfYor6uWEldh3U38qYBM3Pln1reN638wZB0rvSRYOMTZvzilIPy5Vgn2-r7jc-5orsAxBYUlUAln-fC+8VKH2mj3f+P8rj-3PiZMw4FvDTk3v2JBoFB6m1AnqceAhrjFlNLg8c+CULpV1vAn8bYV51Swd3HBdV87R3UHgE8MZd4oB+hgpMc0VJmAAa3f+NEgHqnjFLfhLCDTUP1rfY+-ZprSL0FLTBjhhGmwHtwL2w9Vg71UTvDWSi4hx0rAI6uWCjGGJYchdQ3MmFXC3pcGx5UCDCwqHgIkptezcFQKbFiDNeCEwpBCEmZNTI2CTKaN62QbJZ19qUUyyCInR0nA+TOScYnnFNESRJCYcI+JAKiWQnQZgABMiYmBmICVQ0IAAOkwACejIO63n4NQNg6NuR5M6KUr4lTOjICJkU8pgTyYVFwEgVwEB-yTVnDk4YMxoDQE6O05QpSWBFKJmwImeAvj+P5EKYURNBkjSruKSRxz6hbDgZucQdV7S6kVJqeIgRbk8LEEIEIrUUJW3eW8hMn1zCkhtCbG0VsYw1UjBKTWwk0EvMUc8qmG1rZ7VjAIRF1s2p3PFLKf0-Ygy4UOkIl51zAi4ECrCsiCZSIDSzL5ZU4gNH0WRaRZMF1fDWndJGGqeoGHgpQFaGRvKeVqyUVaLcolgJco1oKswaEJWC0cIwHEBpZVmC5WPcU9sBWUrqtgPIWDxR5ANNqklBc9UP0NeqNCOrxCkj1GhUkBrrUcG5vfcQ+sLE3DLo46SYCXn-y1DAsuXrn7JjNW6j+AaRqwVdG6s+4bvVU0rCsPm1Bw0Vz9ZhFk1rH7lxruIfVLJLUgMvtGkVass1FsTQqma9cTLnDpNeWwFBNg2C0NyPxlIKnVJqeUpm2zlAszZnCTthzNrJmPIYZNF8FrOH8oEPAqtcZsP2rOy2MkF1EBHMuh+haFqBHXRjEI6q11zmdQQdVzr3VuLcGe28e6WkbsSIJO95g6pPogmWxwr7KGmggh+uqc6vGTl7A4JhxrDC4onfNK8cTbwMNvI+Z8r5f3fpXjGf9nLbwykmhtTD6oppLqw1W9QtbIAQCWIhAw3IllE3kMoVQMw2alNRNMLEVUkwkZ5GPSA4onhUd7TRujbMZhMHkIUljko0Zkh-hx6Z4xFA1IKcJ4pyhFnvAAPI9E6IO2pWI2CYxnLYSAWhRwybkx0mYTGmALPycoNTGn2ZBOcYKRolA2EUZIC2p4kwAAWqIKTKb88oGp4xBheZmBiMYyh+jKHkLCTogxESDAANadAAGL8RS6puLYwpizE6JeVYpEdCTlFP4TBmcENviyOwCWRWr7xDK7ZbOMSzBYVqzUEIMKeQblq61mMWDSyodLJ1m9oFWuKKAA" 
            title="Ring Counter" >
        </iframe>
    </div>
        
---------

Build on top of prev, this is a 8bit register. for single bit stream. if you imagine the DFF we're instead
vectors, or words of whatever length say 16bit. then this FIFO is depth is 8 or 16x8. or it has 8 rows.

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=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-o1XEbQRxFCvDjR-V9Ny3gdpvfJrTgqNRlqmBY2xvRNJcEs26rw9QuCKtIGWp0zn52dDqOB6q1mnSeQrR5hzTFB6OdxKCfzabg23p+rOpz4wX4efTeB0m1mguRvOBF6VzbgtBbhFGjz3KbPJbLUwMwyaaAipKDgQMwXfNhYsVVswRhHPVbqyUTmvQmsNfsoKZrpWXO4n1X4drvkXPVcG713AMWYLjB-sNugLQuvzZ68HSQLRm2rZ61lnSt7GhLZ-llo4PAYm-NvWXF1WWRQ-1Miq9bg59ukya+ojrBz4Q2N29Z2znkEi2AMKPGzEgJ62FvdoieDEEVIrcIStlbgUUko8AvdFiQACe9X-4xeq0Zhox3i0xRszco7Za33ab03G795QP0-HJ8W30rqrt10ezTin+m4j+GUzNixpkB2s9wHdu4wntsyUk-tzZAuztyTc5J6W7y7jvnuTt7A0uSj11EA+3bmOCeaw18cq7RyjivW11KQMxzZPgHkw5uIdqvGBQ6EJXw9iZKaqdRYmSDv0pO+9NVyFvx2M-29178C6vldLeMQHuSGuNsGY277s4LQpb1mj00esTb4+istfytSqNlvPZ5eBD1o8HRBEDLGwvUAuFQ8w0Iglu8F5ODw5vdFThhEcAJZvXeAA3DgyRGFcFkFAdRIHiBaAgEysQKL+FYc3lXmvde3AN6by3tw7fO+MLrS9WUCbOFz0SOR7ergSNuAcIi3eAB9MlLgKV-aYOzUdpAAhoEQ2Ibf-C9+kqP8fxeiOUcACU-B-2LdyIvPLR1VNcrBYFNLoV7XIfYMIYOBKF+YoKArQEaIOL0Z4HpBKAvSsJgZ4exJ7OzeAiLd0WMGKBKCAEgqNBAhKHpTJHUH-GgszRgEaKNb6YVVgUA9zbveEWwbjExbgpUB-EAAAZSGAAHkCFN4ABhIYAAaU3gABERDOUABBWoMhP7aKb7MAXoIQDhAQgAMSUMEIABVJCZD5DFCVCyF7YjhKApBfhbCvAgA" 
            title="Ring Counter" >
        </iframe>
    </div>
        
---------

For this 1x8. we are streaming the data. if the src clk is greater than the receive clk, and you constantly stream.
at some point you're going to lose data. the read cant possibly keep up if the writes are constantly happening at a faster rate.
it's just a matter of time before the cup overflows.

it doesn't have to be a serial stream. just in general, if you are constantly writing faster than you are reading.. at some point,
you'll wrap around and catch up.

you can do one of two things, 
    if the FIFO is not using flags (full,/empty) or the writes/reads occur at some known rate and period, 
    the src needs to burst the wr/rd event/data and the FIFO needs to be large enough to accomodate the read/write differences. 

    if you are using flags (full,empty) then they will control your write/read events.



what has to be done here is bursting the read and write. the faster write domain has to accomadate the slower domain.. by bursting
a block of data.. either filling up the FIFO or not. and waiting. the read just reads whenever, as long as it's not empty.

because of this bursting, the incoming data over some time is set. as well as the read.
the FIFO needs to be large enough to hold the write data while it is being read out.

this is called the fifo depth.

i will create several calculators here. or spreadsheet. something interactive.


the second approach is basically a handshaking relationship between the two. where the req/ack is full/empty.
When the fifo is empty, do not read. when the fifo is full do not write. two pointers are created and each
track the write event and read event, respectively. 

The two pointers are shared between the domain.
Both domain needs each other's pointer value, the value must be passed across the domain.
and the domain isn't necessarily the same. 

    If it is, no problem. This is a synchronous FIFO.

    If it isn't, additional steps must be taken to pass the pointer value. This is an asynchronous FIFO.

the respective flags are calculated in their own domain, and are not passed to each other.

the pointer on the other hand often is a BCD counter value.
Passing multi value across domain has risks of skew? not arriving at the same time. 
mis-clocking a pointer value will mess up the flag calculations.

to mitigate this, we convert the BCD counter value to its Gray Code Equivalent.
Gray Code increments / changes one bit at a time.
Therefore while the number is "incrementing" only one bit is changing at a time..
which is like sending a single bit across the domain.

this gray code counter value is now used to determine the FIFO state and whether
we can write/read.






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
Slow to Fast.

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
Fast to slow.

.. raw:: html

    <div style="position: relative; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe 
            width="660" 
            height="400" 
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWEBOaB2AHAZmcjAWBLANgwCYwsQFJrraEBTAWjDACgwEktJ8QyaMiHxwBQqNU7cQxUeOFoSCyZHYAlWZAwgsBamGF7+EYWDFloSS0lowEGkK0O6+TsttcmBr2jYFWqlacGDrMWMIeOmDEAp7mIiAY7ADuTnJe6fxRUKlZcWERBblpvNkSgpESamnMGWWZDTUiMSpyftV5SrGVIGgIVcJqXEgYGb3IxB1DJbLyDe26+s2Lxn0DS-zN-UZuO5uzk9PgcDq9avhkZub8CMjXG3czMHCRgQ5pUzprq8vsAJLgMD6J7gMhFUF2d55MblYSw8BTWYImK0czxJHNNhuMBoWJsZS42JY04qdHRe65EbrQZJfBnapSNIEBnw8adNL7NYItbNHn6HluNQADyc+AgeloEQl2ESZH4AFkAMIABQAOgBnAC2AFcADYAFwAlpqAMYAT1NesYmoADgBDA0AC01ADsAPaagBmjEYABMAEb200Aa3YooiwnwyFoaEgaBEyCo2X4zqNGs16bd7oN3vdACdNRqDfnGPatUbXQBzIuMfNG+16zV+x32gCEHfDugoIhofSwyaIcv4Gqd7v1fuzudH9oAbjaNUHQ5qDZ7F8GQ5qwAByDMaguayC7rvRnTcfgYO7UBAJlMgIMao2mzVkTUAMTfmvHBttOunWeLJ0F2tecmw1DVzVdU0u3MDYyGIfEcB6YhkGHEB7T9P1KxrQCAIA50F39KsFz9RgDUYU1jXdV12ADOkdAwWgpggfA0ATZpRClZROPAfAtjyHiwD4gR5CE-i0nFHoJEkoEhgE1o2EiUSXGGfQxNk8A8Q08x5XAeSpKjCwOU0npRK0nIsWExSUHxFS8kmFRenOPJxjM0y7Hs2zhAc5yuBMUkiSBHEtL8OgHGpQwzzIM5dIGHQGGkfgIWisEovinwkAcQFWFiBAXAhFSoGhbLWgQYSIWEqFMpclMmP4RYVnq+RmHpOYPNqVrFhas9KrybrqGEnKBvEgRYpSho4tmK5bhS6aRAyZo5vwDJ+uWkbVpW1q8rkjqzxcIbttmSLqCRZxhAQTE+usi7aDOzIRScbFZAQxEqAQ1C7w1csFy9HUoKo11NXtPcCM1XVhS7FqkEuHRSBELAWJEkBfz1DUFwgqCrvytw6iSoUuzIBBYZeggkHetCABUAAl-gAZU1FUAFUABlaYAUUzPcvQPDU3wAQVpinNQAEQAeQVPn-gAOU1CnRc1WnmdFgB1EXxclqXIa4Kg2BEfpeLQ1cixLMjTRdfc-xXIC7X1NGwbLV091plV1DZvnhathdTWokt3TAx8q1dRtoGgLWypEHQlAYRHdOBoHNVLDV9QNAAaT2bdRr2jXzU0dSNA1dwzu2NVLLV7UrPdK3jjUqyNedAfAg1HWA6jiMLQCdT3AAiYtSwNM3sK7-SNJk-qONafrkC0sfpCQKfYn68wJDH5F6n0eeDmaDe1g3oaSWX1q2A2GfRWINB+GYNAICnpA6h0O8vWB6cjfAvV3RSBPGFr4s6zTjUPSLJBaC7pdDdkkOKSA50irwEgPPC6hNJBGF0OwEBlwwG0AgVAl48A4HEAQaFNBWAUEoHQS0SBdBsFwFwfgnwqEiEgISEUDBOkKGwBwXieBtgfCMOIWAOhMxMGsJgdQrhZg6G8J4AIlhtg2FUI4Xg0R4AeDEJ7EwshWDZGwPkTQyIEoVGkMETI4R2jFFGGIVfAx0joHsOIJwxBfQ9FAA" 
            title="Ring Counter" >
        </iframe>
    </div>
        
---------


The above method can also be used to send multibit/parallel data.
The data arrives first, then an assert signal, which becomes the pulse. detected as a level.
a pulse is recreated in the slow side and now it can be ready to receive the fast data.
in which the fast data has already been ready/standby this whole time.




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
