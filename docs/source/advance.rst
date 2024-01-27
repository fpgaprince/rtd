***********************
Advance
***********************
Honestly, I think all FPGA Developers should read and refresh every year!
It will either solidify your knowledge, test/question your understanding or teach you something new!



After you do something for awhile.. or in other words, with time and experience, 
things becomes common practice and methodical.
You find the things you found advance weren't really so, but there is only so much one can absorb at a given time.

---------


The Three Pillars
##########################
In the way you write HDL..
You have either control/alogirithm path or data/processing path.
There are three major corners to a design/development. Speed, area and power.

Speed
========================

can mean different things.

**Throughput** is the amount of data passing through or processed per cycle or bits over time, depending what level you are inspecting/analyzing the system.

the usual example for this is the processor's fetch, decode and execute routine.. where initially decode and execute must complete before the next fetch occurs. 
meaning we must wait 3 cycles before fetching the next instruction. if for example* processed 32bits of data, that would be 32bit per 3 clocks.
If we piped the 3 routines such that they're constantly running.. we can processed 32bits per clock. then in the same 3 clock time.. we'd processed 96bits of data.

pipelining is done at a "higher level", it is a system level determination, an architecturural decision.

or similarly, if there was an ALU in the above example, there are 2 clock cycles, fetch and decode where the ALU isn't being used. By pipelining such that
it is always being used, we increase the throughput and efficiency of our design. 

The ALU in the above example is a shared resources. Even though we've piped it to be constantly pumping/processing data.. we can do better.
How? by duplicating resources, drawing on one of the FPGA's strength, parallelism.

       

**Latency** is the elapsed time or delta time for when data arrives until it departs. 
    
    from when it is received until it is returned (transmitted).
    from the time of input to output.
    from when it enters a component or block until it leaves.
    there are different approach for measuring this delta.

If in the previous processor fetch decode and execute routine, each step took 10ns, it would required a total of 30ns. this is considered the latency.
this latency also dictactes your period and clock rate, frequency.

By implementing a pipelined architecture, and not changing the previous period, 30ns. the 3 steps can be broken into 3 cycles.
This increases the total processing time to 90ns (3*30ns). 

this can also be seen from the inital input of the data until we get the first result. the depth of a pipeline will determine the latency.

Any sort of pipelining or registering of input/outputs will introduct additonal cycles, increase cycle count and as a result, latency. 
Therefore in low latency designs/applications, pipelining and registering / excessive registering is undesirable. 

The removal of register often time makes it harder to meet timing requirements, because we now have more logic and logic levels between registers. 



**Timing** is the arrival time of data at the input of a register/flip flop with respect to a clock edge. More commonly known as setup time and or hold time.
These are hardware timing requirements. This basically happens because for whatever reason.. the registers are set too far apart.

Pipeline the design. in otherwords.. Adding register layers.. allows us to separate logic. with less logic between registers, the required clock periods can decrease.
Pipelining increase fmax. Decrease delay requirements from register to register.
    
        Parallelize the design. Analyze function/algorithm, break up into smaller chunks/operations that can be done in parallel.
        Reducing logic level/stages.

Have you started to notice the trade-offs? In the use of pipelining and registering.
And how they're used in different case/application to meet different goals.

Area
========================

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
========================



Pipelining vs. Registering
####################################################
Pipelining and registering are not the same.
It may be confusing because we are adding additional registers to the design.
It is similar because it affects cycle time and latency.
It affects ours period/ frequency. 

I would say.. pipelining is an achitectural system level development whereas 
registering and buffering is circuit/component level, in this case register transfer level (RTL).


Pipeline
========================

**Benefits:**
*   Pipelining the design, can increase fmax.
*   Help with Timing

**Considerations:**
*   Increases latency
*   Increases area

When piping, also remember to pipe the control signals for that logic, for example data valid.
For instance if you have two adders going to a mux. and you pipe the results 
of the two adders. these adders go to a mux.. the select line needs to be 
piped so that the selection and results will appear at the mux at the same time.
as if you never piped it. it needs to look the same to the mux, or hidden from the mux.

furthermore.. there is a period in which the pipe needs to be filled up
before you get sensible / usable data. This is also the latency.


Registering
========================
Registering is buffering. Registering adds additional clock cycles.
Registering is a method of splitting up logic. It eases place and route.
Allowing us to duplicate registers/logic and reduce fan out.

Sometimes there are several logic levels between a source FF and a dest FF.
adding a register between these two FF can split up the logic level between 
the original FF. Say it was 4 logic level between FF1 and FF2.
Adding a pipe register FF3 between 1 and 2, you can split it to 2 logic level.
2 between FF1 and FF3 and 2 between FF3 and FF2. You can further pipe this.

By adding registers or flip flop to break up the combinatorial logic,
we reduce the critical path or data path, such that we can lower the period
between registers, in other words, increase the overall frequency.

Bc we add more registers/FF in the datapath, we add one more clock cycle delay
for each, this increases latency. you have to be aware of the added latency
and how it affects the overall latency. what are the
requirements and limits.



Register Data Paths at Logical Boundaries
Register the outputs of hierarchical boundaries to contain critical paths
within a single module or boundary. Consider registering the inputs also
at the hierarchical boundaries. It is always easier to analyze and repair 
timing paths which lie within a module, rather than a path spanning 
multiple modules. Any paths that are not registered at hierarchy boundaries 
should be synthesized with hierarchy rebuilt or flat to allow cross 
hierarchy optimization. Registering the datapaths at logical boundaries 
helps to retain traceability (for debug) through the design process 
because cross hierarchical optimizations are kept to a minimum and 
logic does not move across modules.


DSP designs generally allow latency to be added to the design. 
This allows registers to be added to them to implement a higher clock frequency 
design. In addition, registers can be used to increase placement flexibility. 
This is important because at high clock frequency, signals cannot traverse the 
die in one clock cycle. Adding registers can allow hard-to-reach areas to be used.



.. comment_out image:: images/add_reg.png
    :width: 660
    :alt: Alternative text
    :align: center


.. comment_out    

FIFO
##########################
First In First Out.

This sequential module is pretty important and used in many application.
It is best to master this quick. Youl will see it everywhere!

First thing first, FIFOs were probably first introduced in data structure along with queue and stack alogorithms for data storage.
FIFO is a structure for how data is stored and retrieved. Our FIFOs are realized with the BRAMs. which means
you need to write/read to them as well as keep track off the addressing/pointer.

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
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgbA7CAMB00IQFgJxvRzYQGZYFY0ccBGADjJ3zACZKVt9oR8Xn8BTAWhJIChyrKjXBIQSHCLBj8JGsxwD8rFEjFIEIEtBrrN7AdK0opY3cyPz8InDBb2AZgEMANgGcOMPgHcQPbHJkIAxadF5uuCK8IiHRdiQgAC4ATgCuHErMsfJaaqHMCSIGvv6hQaUkYMzQfACSfpUg8swVVXZwrPg+DdjNPU1GNQAykVpyIEFxBSDO7p6sw8amY8vVM64e9jW+2mZiJHm6XiPSCiLUZ-Hrc1vddJNhwmVevveiuNbv200UwdhPIW+qnUkmCeVQ2G+B32n1BJE+3zhsJsZDEixQOH+mOC2JogK0102C0MWVhYCCKFh2OYOW0iHpCG6wPEmmZOAgkKZeXZ2EpNnJLy00A0LIKwoU1O6uwlvIFxE5vhQ4wBypyQOVnwx-wR3Qg3M+HKCT2+erET1NkWq3TIEBs2LImnlgptIg0zBduElvggHNwvogqNwApNvrdIB9-19NUqzADZoFcc9kKaYoZ9L4I0NSfDArxyYSsyJgoj4lBJYhXnhrHLmjI1FFdi6vnwvqeVQUOubrc+Lf+at1wuzYFBTpNg7DEEHo+6VSNvrAjUxQW+s4bq55lbaC-+Au32ZpqbTjJOjux7aa+OYhfmgtXEik0CCFejynAj7XvzDVt8GiNn3vHxFN0v6ASyQTyMu3T4NiTpIEY07NtiYbQViCriCKG5qEawbASKYZqAoUYkuh2FPkgRrUimQpHsepZ2tgAF5lc163D+eGggR4iAkorCcchORfiwdwYZ8NDwZ2TQiSI5gpt+QYUb0IQIfJDZLvudy2n6vQOip3w0JpYb6TYRExj8Ci5jpo5UXSNEZgMZq4pYl6EjeekGaCRlcZyVZNAZjr-voxY2Jq2pAd6wUiJpJAmIKfROoE6mvJohmnmhuxaSsulSuOmjpRu0ZtHEalFZRtI0bRSnYiETFrCxxI7OOcLjtxPnpWG5B6GsULQJpTzaEpEnaL1nxDTY-Y7HF2LRApgpyMluWTWleW+rwyo4TsbW5ct3mFUVAqrfRdhleVdn9ahQrVc5dWzW1cJtS1r68DlBQdQ2clyCOI00PWxpSjQn1RP9Y3vZiMplDNUKgw2JBQ8pcjwStnlqVCYmdaECM7QUSP7UjpWHkep3fedcj1jVBLXSjRgAfD6gPawNPQzg4KBU24ZRDFSCNNFYUkUsvN9N8WGyZJB5yeRBQczpEGCuLKZPu+0vfLI7PnKqcnK5aLCtuNb5PiEfHcWxzAVp5z4aa6sTNWlVvvGbvh3iE5aG+GoYhMydtgrTAT3UtNsMx7+B5NzLCHEcSuh2IFo0GHuoR+G3I60qwPBOMNCNErK0xb2TTpzO77B6uisziKBcigLxei6EHn6FBvpp7yqe5-bCv5z10nvt1mnS6NmsoyOtJA8LNQAB4NEz4YoBMIhkK6kkgBwAC2qQuE4iQcAAOm4ADGLgAPZbwA1pvbgAJYAOYAHauJkwSfHWASIBM9aFI2TJ3+Rt+RTF3xcEpgYjoGREKIzQWzQhxEIVNuIjD5BMIwSdYFonJhsVyfBR5KknigHQwQ9TBGgLxOeAB1AAogAOQEP-bEk4xCrioSwOauBUENBhrAh+tgyBgEnnseeS8V5r03jvfeR83Cn0vtfV4mksxOizG5aeqUJg13EZFGClDJQjBIP6Kq2AICUSvMg24aitGBi4EERM0wKbdB4OMB0LQkD1mseELQhixA6VMQSFI6QLFGHsTpexBV9gaN6EcbRvQ8E2C2HYFielHQxT6MoHmsSArsAkshRJ4BNKC1BNYJ8oJIA8zUlkuiLAwiIgFGGfJxTgJGAKXBah6SoLYmqVUipiEGKaBQkUyCP4QhxK8mknmFYem0J6WONGQyJIejDB6bOSswjZymURBqeFcrijfOrLcyyRTnhRvNLGmhaBoigjFfZ+QLAxx2FDdqUNpCdPAEca5WgrkfxXHczSxz7lKyOZpQgUgzksC3F89Z6swi5I6VrTko8P48FEt9BoqBxBzxPg4Te3hkib3XgAB03iQNFABHTeyQAAmAAaTeDhl4uEYQcLBXB9pIB9H4MA+CjgAAlcWkvJXwAAsg8gUPBBxUvKOlGkBApQ4EHDwKaYqxCWJ5vAiVAQpVjzSoqvl+xoCglVTdbEXAooqrqec8VurxUPQKCq9KMNeXmtwPYVm9iaXOM0DJbqIp7XyJaIMXURi3baudomXQJivXeUDkKF1UVHzlCik0V+9RtC-B1VEC1fh0kwAIEJeEYgtQNEHCgIxVqihCXqDm6V5r1UiE1dUVNrMsw8DCGQRoNablZiJjmQVzTebGLFC6nSgtIVxEzTKmWva8h1uwDwPINR6jsOLVVcY8r2iVqUM4+tiap1KoJPmroIwnhjpAYK8dSCbjEi3Z8Hg2tBVRgiXoo9oEuDS0kOURWl7D2Cm3R-N4HrfDbqlr8Z2264hvAStGAaZbpY1L8NLGwjDo4JGsKc9g-14VHG8BwAA5MkDe28XBCLPqvE+F8z6bwAEZb03hfXem8OBX0Iy4DDu8L6kr3uitwfBOaT39Swf+OR8CBggJUI05twy4h0uSOSnlJHjBE7FTS9imbUO7Sx6KjiWj-o1XEbQRxFCvDjR-V9Ny3gdpvfJrTgqNRlqmBY2xvRNJcEs26rw9QuCKtIGWp0zn52dDqOB6q1mnSeQrR5hzTFB6OdxKCfzabg23p+rOpz4wX4efTeB0m1mguRvOBF6VzbgtBbhFGjz3KbPJbLUwMwyaaAipKDgQMwXfNhYsVVswRhHPVbqyUTmvQmsNfsoKZrpWXO4n1X4drvkXPVcG713AMWYLjB-sNugLQuvzZ68HSQLRm2rZ61lnSt7GhLZ-llo4PAYm-NvWXF1WWRQ-1Miq9bg59ukya+ojrBz4Q2N29Z2znkEi2AMKPGzEgJ62FvdoieDEEVIrcIStlbgUUko8AvdFiQACe9X-4xeq0Zhox3i0xRszco7Za33ab03G795QP0-HJ8W30rqrt10ezTin+m4j+GUzNixpkB2s9wHdu4wntsyUk-tzZAuztyTc5J6W7y7jvnuTt7A0uSj11EA+3bmOCeaw18cq7RyjivW11KQMxzZPgHkw5uIdqvGBQ6EJXw9iZKaqdRYmSDv0pO+9NVyFvx2M-29178C6vldLeMQHuSGuNsGY277s4LQpb1mj00esTb4+istfytSqNlvPZ5eBD1o8HRBEDLGwvUAuFQ8w0Iglu8F5ODw5vdFThhEcAJZvXeAA3DgyRGFcFkFAdRIHiBaAgEysQKL+FYc3lXmvde3AN6by3tw7fO+MLrS9WUCbOFz0SOR7ergSNuAcIi3eAB9MlLgKV-aYOzUdpAAhoEQ2Ibf-C9+kqP8fxeiOUcACU-B-2LdyIvPLR1VNcrBYFNLoV7XIfYMIYOBKF+YoKArQEaIOL0Z4HpBKAvSsJgZ4exJ7OzeAiLd0WMGKBKCAEgqNBAhKHpTJHUH-GgszRgEaKNb6YVVgUA9zbveEWwbjExbgpUB-EAAAZSGAAHkCFN4ABhIYAAaU3gABERDOUABBWoMhP7aKb7MAXoIQDhAQgAMSUMEIABVJCZD5DFCVCyF7YjhKApBfhbCvAgA" 
            title="Ring Counter" >
        </iframe>
    </div>
        
---------

For this 1x8. We are streaming the data serially, 1 bit at a time. If the src clk is greater than the receive clk, and you're constantly streaming..
at some point you're going to lose data! The read cant possibly keep up if the writes are constantly happening at a faster rate!
If writing is like filling a cup up with water and reading is like a person drinking it.
If your fill rate is greater than your consumption rate, it's just a matter of time before the cup overflows.

Again, it doesn't have to be a serial stream. You could have a stream of words, words which are 14 bits, 16bit, 32, 64, 128, whatever size!

Just in general, if you are constantly writing faster than you are reading.. at some point,
you'll wrap around and catch up. you don't want that. you'll want to have logic in place to prevent "overrunning".

You can do one of two things,

    if the FIFO is not using flags (full,/empty) or the writes/reads occur at some known rate and period, 
    the src needs to burst the wr/rd event/data and the FIFO needs to be large enough to accomodate the read/write differences. 

    if you are using flags (full,empty) then they will control your write/read events.


What has to be done here is bursting the read and write. the faster write domain has to accomadate the slower domain.. by bursting
a block of data.. either filling up the FIFO or not. and waiting. the read just reads whenever, as long as it's not empty.
because of this bursting, the incoming data over some time is set. as well as the read.
the FIFO needs to be large enough to hold the write data while it is being read out. This is called the fifo depth.

.. note::

    I will create several calculators here. or spreadsheet. something interactive.


The second approach is basically a handshaking relationship between the two. where the req/ack is full/empty.
When the fifo is empty, do not read. when the fifo is full do not write. two pointers are created and each
track the write event and read event, respectively. 

The two pointers are shared between the domain.
Both domain needs each other's pointer value, the value must be passed across the domain.
and the domain isn't necessarily the same. 

    If it is, no problem. This is a synchronous FIFO.

    If it isn't, additional steps must be taken to pass the pointer value. This is an asynchronous FIFO.

The respective flags are calculated in their own domain, and are not passed to each other.

The pointer on the other hand often is a BCD counter value.
Passing multi value across domain has risks of skew? not arriving at the same time. 
mis-clocking a pointer value will mess up the flag calculations.
to mitigate this, we convert the BCD counter value to its Gray Code equivalent
(Gray Code increments / changes one bit at a time).
Therefore while the number is "incrementing" only one bit is changing at a time..
which is like sending a single bit across the domain.

This gray code counter value is now used to determine the FIFO state and whether
we can write/read.


While we explained how the FIFO works, I did not really mention where it's used.
FIFO can be used to buffer ethernet frames. It can also be used to buffer video or image frames.
FIFO are generally used to buffer data and for passing data across different clock domains.
You can think of both as similar to passing data across clock domains too.

Ethernet and video frames may not be operating at the fastest clock rate, but their data width is wide!
Their data is large trun


In all cases, it operates in the same manner.





Clock Domain Crossing
####################################################
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

    Synchronizer circuit
    async FIFO
    Pulse
    Handshake
    Sample and hold

    if two clocks have the same frequency, but come from different sources, they are async. needs to be handled.
    if they're the same frequency but have different phases.. or the phase can not be guaranteed, it is async. handle it.
    
    if a signal comes in the input pin and you have no information whatsoever about it, it is async. sync it.

    
    double check.. if a clock is a derivative or multiple of the source clock from the pll (MMCM), it is sync.
    the generated clocks are synchronous to the source clock.
    ??    if they have different frequency (one faster, one slower), they're def async.
        even if the source is the same.

    MAKE A TABLE!

    logically exclusive clocks - when two clocks are muxed to the same FF set. only one will be active at any given time, never both/together.
    the FF will only see one or the other. never both.

    physically exclusive is similar, but one may be a debug/test clock. the other is the actual clock. so again.. the FF would never see both at the same time
    or together.

    in both case you have would not have one set of FF driven by one clock and another set of FF driven by the others.
    
    they are exclusive, meaning FF only sees one or the other.


Slower to faster
========================
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
========================
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


.. code-block:: vhdl
  :linenos:   

    process (clk, rst) begin      
        if rising_edge(clk) then
            if data_in = '1' then
               q0 <= not q0;
            end if;
        end if;
    end process;
 
    process (clk2, rst2) begin
        if rising_edge(clk2) then
            q1 <= q0;
            q2 <= q1;
            q3 <= q2;
         end if;
    end process;      

    data_out1 <= q3 xor q2;
    
double flop should only be used for slow changing signal, again going from slow domain to a fast domain.
double flop should be placed physical close to each other during imp to increase MTBF. ASYNC_REG

se_clock_groups to specify unrelated clocks, rather than use set false path. you'll have to specify too many this way.
se_clock_groups is more concise, clean. -asynchronous

Reset 
##########################

    Dedicated BRAM and DSP should be synchronously reset because these are dedicated HW in the FPGA. They were 'fabricated' that way, so in order
    to use them correctly.. their resets should be syncrhronous.

    SRL, no reset. Likewise.. frabricated with NO reset pin/input. Therefore if you try to add one, the tool will synthesize extra surrounding logic
    to implement what you, the designer, wants.

    Using set/reset pins can prevent combinatorial logic optimization.

Asynchronous Reset vs. Synchronous Reset
================================================
    
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

Reset bridge, asynchronous reset, synchronous release/ synchronous de-assert deassert
Reset bridge means.. assert asynchronously and deasserted synhcronously. and also to use two flip flops to synchronize to the domain.

    
.. code-block:: vhdl
  :linenos:   

    process (clk, rst) begin      
        if (rst) then
            rst_out <= '1';

        elsif rising_edge(clk) then
            reg <= '0';
            rst_out <= reg;
        end if;
    end process;


Reset distribution network. Is used to synchronize the reset and ease the place and route. It is like piping a signal.
The distribution tree allows for spreading the registers. These reset to various blocks will have several cycle delay,
depending on the piping and where it is tapped.

remember to syncrhonize reset signals to clock domain it is being used! double flopping is sufficient, because it is a slow changing signal.

----------


When writing HDL, don't mix async and sync resets, because FF and registers are not fabricated in this way, 
you will create additional surrounding logic to implement such functionality.

In regards to fully sync reset and asyc+sync, you need to always synchronize the reset signal the whatever clock domain it is being applied to. 
It is just like any other signal!

.. note::

    Not every digital component/module needs to have a reset coded.
    
For instance.. a shift register, or delay or buffer do not need it.
This is because over whatever cycles, it will flush itself out. it will flush the bad/unused values out.
either that or whatever down stream using these buffers/registers will also have data valid signals passed on.
meaning that while there is garbage in and garbage out, the data valid is de-asserted, so the data is not used, trashed.
you dont have to worry about it. In a similar fashion, synchronizers dont need them.


    state machine should have reset state. generally some IDLE or START state.
    counters should have a reset state. usually zero or some other modulo count value.
    control output to other device will want a reset state, if it is used immediately by other devices.
    but if the control signal isn't used immediately, it probably does not need a reset.
    
    not having reset on every register helps with place and route. minimizes congestion.

    note: there are certain xilinx modules that need async reset, just double check documentation.


bus coherency. means bits arrive at the same time. it should just be.. data coherency.. you dont want 1101 to arrive as 1001. 
this is bits of the bus need to arrive together, at the same time. ensuring parallel data arriving in timely manner. could be counter value, system state.. effects
    solution..

    capturing bus when bus is known to be stable.. 
        source is slow.. then data can appear at fast registers, clk'd by faster clk.. but controlled by enable CE.
        CE is a result of leading edge detect of of slow clock SYNCHRONIZED to the new clock domain.
        3 FFs. the last FF is used as a leading edge detect. the leading edge result/pulse is used as CE into fast FF to 
        register slow data.s

        OR ie using valid signals.. handshaking..                
        the datavalid is passed thru sync into the faster domain. the edge detect of valid in new domain enables, CE
        FF register.
        if fast to slow, the valid signal needs to be longer than one slow clock pulse. and cannot occur multiples time to back.
        or else there is no way for the slow domain to capture it.
            rule of thumb is for valid to only occur once every four destination clock.

        going from slow to fast is not as much of a challenge because the fast clock domain will most likely register the value several times!
        usual double flop will work.

    allowing only one bit to change at a time, gray code.. pointers, counters..

    using a clock crossing FIFO, ie. async FIFO. again with handshaking or... not? if data rates are known and depth is good.   
    the trick is the full flag in the write domain and the empty in the read domain.
    in which. the full flag in the write domain needs the updated read pointer.
    vice versa.. the empty flag needs the write pointer from the write domain.
    two synchronizers are needed for passing the individual pointers, to and fro.
    gray code/counter is used for this in which only one bit can change at a time. decreasing probability of incoherent data!

XPM - xilinx parameterized macros for CDC!
    
    single bit 
    pulse
    gray code
    handshake synchronizers

    this is 4 of them.. there are 7 

Below is from Xilinx

::
        
    AMD devices have a dedicated global set/reset signal (GSR). 
    This signal sets the initial value of all sequential cells in hardware at the end of device configuration.

    If an initial state is not specified, sequential primitives are assigned a default value. In most cases, the default value is zero. 
    Exceptions are the FDSE and FDPE primitives that default to a logic one. 
    
    Every register will be at a known state at the end of configuration. 

    Therefore, it is not necessary to code a global reset for the sole purpose of initializing a device on power up.

    AMD highly recommends that you take special care in deciding when the design requires a reset, and when it does not. 
    In many situations, resets might be required on the control path logic for proper operation. 
    However, resets are generally less necessary on the data path logic. Limiting the use of resets:

    Limits the overall fanout of the reset net.
    Reduces the amount of interconnect necessary to route the reset.
    Simplifies the timing of the reset paths.
    Results in many cases in overall improvement in clock frequency, area, and power.

    Evaluate each synchronous block, and attempt to determine whether a reset is required for proper operation. 
    Do not code the reset by default without ascertaining its real need.
    Functional simulation should easily identify whether a reset is needed or not.

    If a reset is needed, AMD recommends using synchronous resets. Synchronous resets have the following advantages over asynchronous resets:

    Synchronous resets can directly map to more resource elements in the device architecture.
    Asynchronous resets impact the maximum clock frequency of the general logic structures. 
    Because all AMD device general-purpose registers can program the set/reset as either asynchronous or synchronous, 
    it might seem like there is no penalty in using asynchronous resets. If a global asynchronous reset is used, 
    it does not increase the control sets. However, the need to route this reset signal to all register elements increases routing complexity.
    Asynchronous resets have a greater probability of corrupting memory contents of block RAMs, LUTRAMs, and SRLs during reset assertion. 
    This is especially true for registers with asynchronous resets that drive the input pins of block RAMs, LUTRAMs, and SRLs.
    Synchronous resets offer more flexibility for control set remapping when higher density or fine tuned placement is needed. 
    A synchronous reset can be remapped to the data path of the register if an incompatible reset is found in the more optimally placed slice. 
    This can reduce routing resource utilization and increase placement density where needed to allow proper fitting and improved achievable clock frequency.
    Some resources such as the DSP48 and block RAM have only synchronous resets for the register elements within the block. 
    When asynchronous resets are used on register elements associated with these elements, 
    those registers may not be inferred directly into those blocks without impacting functionality.

    Following are additional considerations:

    The clock works as a filter for small reset glitches for synchronous resets. 
    However, if these glitches occur near the active clock edge, the flip-flop might become metastable.
    Synchronous resets might need to stretch the pulse width to ensure that the reset signal pulse is wide enough for the reset to be present during an active edge of the clock.
    When using asynchronous resets, remember to synchronize the deassertion of the asynchronous reset. 
    Although the relative timing between clock and reset can be ignored during reset assertion, 
    the reset release must be synchronized to the clock. Avoiding the reset release edge synchronization can lead to metastability. 
    During reset release, setup and hold timing conditions must be satisfied for the reset pin relative to the clock pin of a register. 
    A violation of the setup and hold conditions for asynchronous reset (e.g., reset recovery and removal timing) 
    might cause the flip-flop to become metastable, causing design failure due to switching to an unknown state. 
    Note that this situation is similar to the violation of setup and hold conditions for the flip-flop data pin.

Synchronous Registers
FDSE - Set, for setting '1'
FDRE - Reset, for resetting to '0'

Asynchronous Registers
FDPE - Preset, for preseting to '1'
FDCE - Clear, for clearing to '0'

When no reset is provided..
Vivado synthesis generally defaults to zero with a few exceptions such as one-hot state machine encodings.
AMD highly recommends that you initialize all synchronous elements accordingly. 
Initialization of registers is completely inferable by all major device synthesis tools. 
This lessens the need to add a reset for the sole purpose of initialization, 
and makes the RTL code more closely match the implemented design in functional simulation, 
as all synchronous element start with a known value in the device after configuration.


Clocking
##########################

for me.
https://docs.xilinx.com/r/en-US/ug572-ultrascale-clocking/UltraScale-Architecture-Clocking-Resources-User-Guide


MMCM vs. PLL.
Fvco = Fclkinn x M/D

Fout = Fclkin x (M/(DxO))

VCO = voltage controlled oscillator

A phase-locked loop (PLL) circuit is a feedback system that combines a voltage controlled oscillator (VCO) and a phase detector in such a way that the oscillator signal tracks an applied frequency or phase modulated signal with the correct frequency and phase.




Static Timing Analysis
##########################

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


    setup slack (positive pass, negative fail!) Just remember WNS, worst negative.

    slack = data required time - data arrival time
    
    slack = [capture edge time + destination clock delay - clock uncertainty - setup time] - [launch edge time + (source clock delay + data path delay)].
    
    PERIOD = capture edge time - launch edge time
    
    slack = PERIOD + [destination clock delay - clock uncertainty - setup time] - [source clock delay + data path delay]
            period - setup + [destination clock delay - clock uncertainty] - [source clock delay + data path delay]


positive means data arrives within period and setup with time to spare.
subtract uncertainty to shorten available time for data to arrive, worse case..

hold slack (positive pass, negative fail), just think 

    slack = (source clock delay + data path delay) - (destination clock delay) + clock uncertainty

positive means it takes the data time to get to the destination flop, such that data doesn't change immediately
on a clock edge, old data at FF2 is held for the hold requirement. old data is stable before new data arrives.
it means it took more time for data to arrive than the required time, therefore the subtraction result is positive..

    hold slack = data arrival time - data required time

   = [launch edge time + source clock path delay + datapath delay] - [capture edge time + destination clock path delay + clock uncertainty + hold time]

    launch edge time - capture edge time + hold time

adding clock uncertainty, means we're saying the clock arrival takes longer, giving more time for data to travel. such that data doesn't "get there too soon".

hold violation is when the data changes too quickly upon a clock edge. meaning new data from some flop before arrived too early. and effects the current flop's launching.
which means the data path was short in comparison to the clock delay path to the destination flop.

you have to FF, 1 and 2 
let data from FF1 already be ready at FF2, we're waiting for the arrival of the clock.
the clock arrives at both 1 and 2.
the data at FF2 from FF1 is getting passed/latched right now.
FF1 also pushes out new data, but this travels super fast to FF2 and changes FF2's value before FF2 actually latches the last value.
this 

one more.. 
clk arrives at FF1, FF1 launches 'new' data. same clock edge arrives at FF2, which is supposed to clock FF1 'old data' but because 
new data traveled thru some super short path, it arrives ON THE SAME clock edge within the hold duration of FF2. this causes a hold violation at FF2
in which the new data from FF1 contaminates or corrupts FF2 from latch the 'old data'.
i think this is the best tone..

if launch clk arrives early, it gives even more time for data to get to the capturing flop on the same edge, we dont want that.
if clock arrive at capturing later.. again gives more time for launch data to arrive at capturing on the same edge. bad

notice.. hold is regarding the same clock edge on two flops.
the analysis is done on the launch and capture flop, one the same edge in time.
launch data cannot arrive at capturing flop within the hold window. or data will be corrupted.

setup is launch edge on launching flop, followed by capturing edge on capture flop. 
laucnh data must arrive at capture before next edge.

you must look for the shortest data path and make sure it is not shorter than the hold requirement.

for setup.. you look for the longest data path and make sure it does not exceed the period and setup.


jitter and skew are similar as in the have to do with the clock and its arrival to a register. it can sooner or later.
the difference is in the source of these phenomenon?
jitter is inherent in the clock, whether it is external, from an oscillator/crystal. or even MMCM / PLL.
it is what it is and must be accounted for.

skew is due to routing, the clock path to a various registers spread out across the fpga. as in while the same clock edge or source rises..
it must propagate across the fpga to the intended registers. and if one is further away.. physically, it will physically take longer
for the clock to propagate. 

"time difference between the clock signal arriving at the source and destination flip flops in a given clock path"
"Positive skew : source FF receives clk earlier than the desination"
"Negative skew : source FF receives the clock later than the destination"
the clock is time from a common source or start point. common node.
    this is why there is destination clock path delay and source clock path delay 


two registers that need to be clocked by the same clk.. may actually see the clock arrive at different absolute time.

so you basically have skew.. and then jitter on top of that. jitter happens regardless and again is innate, known, accepted, accounted for. with clock uncertainty!

skew on designs >300MHz can become issue
intra clock 300ps. between balance sync clock 500
when utilization is high, harder for clock. because it has to spread across the fpga
REMEMBER, a CLOCK is also a signal. it too, needs to propagate just like anything else.
and must adhere/obey the same laws!

there are 4 types of timing exceptions:
    Multicycle paths
    false paths
    min and max delays
    clock groups


clock uncertainty.
uncertainty relative to ideal clock. which can be due to 
user specificed external clock information, system jitter. or duty cycle distortion.    
input jitter, discrete jitter, phase error, user added uncertainty.
clock modifying blocks can add jitter and phase error to clock

    use clocking wizard, it provides accurate uncertainty data.

reserve slack margine to represent noise.
NEVER add extra uncertainty to ensure proper hardware functionality. tool is conservative.
can over constrain that path related to a clock or a clock pair.

uncertainty helps model hardware operationg conditions accurately. "run time"


consider using BUFGCE_DIV, it is a divider. instead of using MMCM.


it seems you are more probable to have setup issues with input timing. due to board signal propagation or poor characterization of external devices.
if it were internal.. it is most likely due to place and route and the results of poor placement of resources, components, logic.
which can also be a result of poor coding.

hold violations are usually internal. and most likely due to clock domains and imporoper constraints.

i think* the output timing face similar issues.

these are more complicated constraints because we need external device specs and board/pcb specs as well.
and you wont truly see this/these failures and or violations without having the actual HW.


Slack (setup/recovery) = setup path requirement
- datapath delay (max)

+ clock skew

- clock uncertainty

- setup/recovery time

Slack (hold/removal) = hold path requirement
+ datapath delay (min)

- clock skew

- clock uncertainty

- hold/removal time

For timing analysis, clock skew is always calculated as follows:

Clock Skew = destination clock delay - source clock delay (after the common node if any)


small setup time violation may still work in lab. lower fq initially 
there is more focus by tool to fix hold violations

hold violations are critical, design will most likely not work.
    check multi cycle constraints
    check clock skews
reduce number of control setes




Timing Closure
##########################

    Timing closure and static timing analysis (STA) are one.

    You use STA to close timing.

    To close timing means to address timing violation and failures.

    Timing violation result from failing to meet setup and hold time requirements.

    STA must be performed to determine cause of violation.

    

Causes of Timing Violations
================================================

Logic Delay
-------------------------------------

Logic Delay is made up of cell delays.
Cell delay is time from input to output of LUT or a series of LUTs (logic levels).
It is like the gate delay and propagation delay learned in digital design.
Slower clock allows for more logic level or combinatorial logic in between registers.
Faster clock have more stringent requirement, requiring less logic levels.

For timing to be met, these delays need to meet setup and hold time requirements.

Datapath Delay and Logic Levels
In general, the number of LUTs and other primitives in the path is most important factor in contributing to the delay. 
Because LUT delays are reported differently in different devices, separate cell delay and route delay ranges must be considered.

Net Delay
-------------------------------------
Net Delay is routing delay, the propagation delay from through the routing network from one logic block to another.

Net Delay is something to look at POST ROUTE. you can look at it's estimate after synthesis before routing..
but net delay and congestions is something that kinda happens afte routing.

net delay is wire delay and is the RC models you learn in digital classes
the difference ish with FPGA and ASIC is that the fabric/IC is components are 
already placed. you are merely selecting this component and that component to implement.
and so the route is in a sense predefined, the tool knows what the wire RC is.. or delay is.
from one cell to another. or from one lut to another or from whatever to whatever so on.
reword.


Clock Skew and Uncertainty
-------------------------------------

AMD devices use various types of routing resources to support most common clocking schemes and requirements such as high fanout clocks, 
short propagation delays, and extremely low skew. Clock skew affects any register-to-register path with either a combinational logic or interconnect between them.
Clock skew in high frequency clock domains (+300 MHz) can impact performance. In general, the clock skew should be no more than 500 ps. 
For example, 500 ps represents 15% of a 300 MHz clock period, which is equivalent to the timing budget of 1 or 2 logic levels. 
In cross domain clock paths the skew can be higher, because the clocks use different resources and the common node is located further up the clock trees. 
If the clock uncertainty is over 100 ps, then you must review the clock topology and jitter numbers to understand why the uncertainty is so high.


Analyzing Violations
================================================

**High logic delay percentage (Logic Delay)**
    
*   Are there many levels of logic? (LOGIC_LEVELS)
*   Are there any constraints or attributes that prevent logic optimization? (DONT_TOUCH, MARK_DEBUG)
*   Does the path include a cell with high logic delay such as block RAM or DSP? (Logical Path, Start Point Pin Primitive, End Point Pin Primitive)
*   Is the path requirement too tight for the current path topology? (Requirement)

**High net delay percentage (Net Delay)**

*   Are there any high fanout nets in the path? (High Fanout, Cumulative Fanout)
*   Are the cells assigned to several Pblocks that can be placed far apart? (Pblocks)
*   Are the cells placed far apart? (Bounding Box Size, Clock Region Distance)
*   For SSI technology devices, are there nets crossing SLR boundaries? (SLR Crossings)
*   Are one or several net delay values a lot higher than expected while the placement seems correct? Select the path and visualize its placement and routing in the Device window.
*   Is there a missing pipeline register in a block RAM or DSP cell? (Comb DSP, MREG, PREG, DOA_REG, DOB_REG)

**High skew (<-0.5 ns for setup and >0.5 ns for hold) (Clock Skew)**

*   Is it a clock domain crossing path? (Start Point Clock, End Point Clock)
*   Are the clocks synchronous or asynchronous? (Clock Relationship)
*   Is the path crossing I/O columns? (IO Crossings)


Addressing Violations
================================================


High Cell Delay
-------------------------------------
*   Modify RTL, use parallel or more efficient operator
*   Add pipeline reg, use synth retiming
*   Pipe DSP BRAM and URAM
*   Optimize SRL


opt_design -remap
report_qor_suggestions


Dedicated blocks have more stringent timing requirements than registers, SRL and LUTs
Before piping dedicated blocks (BRAM DSP etc), enable all registers first!


I hadn't really thought about it before but.. because we use LUTs to capture logic functions.
We are no longer using gates. We are actually using SRAM!
Therefore the prop delay is of the SRAM and not the actual function or gate as taught in digital logic courses.
Which also means.. the delay is constant for all function using that LUT/cell.


High Route Delay
-------------------------------------

*   Check PnR constraints, adjust floorplan constraints
*   Check high fanout nets
*   Check congestion level, resolve levels greater than 4


reduce muxf mapping to lower congestion
improve logic levels
reduce control sets
optimize high fanout nets
replicate drivers.. ie register replication.. which is like buffering the data. or buffer amplifier
register replication
prioritize critical logic
fix hold violations prior to routing
addressing congestion
tuning compile flow
floorplanning

addressing congestion

lower utilization
disable LUT combining and MUXF inference
balance SLR (super logic region) utilization for SSI (stack silicon interconnect)
use block level synthesis strat
use alternative pnr directives
limit high fanout nets in congested area
turn off cross-boundary optimization.


unlike ASIC where you have a physical designer responsible for placement and route..
FPGA is all in one with their vendor tool. you generally let the tool 
perform the pnr. and use directives to focus on performance, area, speed, power.
For higher performance development/design you will most likely have to set up placement.



there is delay penalty for data propagating across SLR
pipeline data!


there is post placement optimization (enabled by default) and post route (disabled)..


restructuring/re-wiring LUT, creates new LUT functions so that the critical path or function/logic
is faster

cell replication and register replication serves the purpose of improving timing


registers can be pulled into or out of DSPs. like wise..
registers can be pulled into or out of BRAMs

retiming moves reigsters across combinational logic levels





congestion..
use less than 70-80% utilization in device or SLR

3 types: global, short, long




Control Signals and Control Sets
-------------------------------------------------
A control set is the grouping of control signals (set/reset, clock enable and clock) that drives any given SRL, 
LUTRAM, or register. For any unique combination of control signals, a unique control set is formed. This is important, 
because registers within a 7 series slice all share common control signals, and thus, only registers with a 
common control set can be packed into the same slice. For example, if a register with a given control set has just 
one register as a load, the other seven registers in the slice it occupies will be unusable.

Designs with too many unique control sets might have many wasted resources as well as fewer options for placement, 
resulting in higher power and lower achievable clock frequency. Designs with fewer control sets have more options and 
flexibility in terms of placement, generally resulting in improved results.


avoid mixed-mode control signals for sequential calls.

only use clock enable and set/reset when necessary, usually first and last stage.



Give priority to improving the code instead of modifying the Compiler Settings.
Analyze whether critical paths can be re-coded.
Check if logic can be pushed across register boundaries.
Check if part of the logic can be done in parallel, or in a different data cycle (a cycle before or later).

Excessive levels of combinational logic in your design can increase the delay on a path and cause that path to become critical.
conditional statements are always translated as additional levels of logic. 

Wide distribution of registers is one of the main causes of excess delay on timing paths.

Your design can have synchronous or asynchronous reset signals. 
Typically resets coming into FPGA devices are asynchronous. 
You can convert an external asynchronous reset to a synchronous reset by feeding it through a synchronizer circuit. 
You can then use this signal to reset the rest of the design. 
This clock creates a clean reset signal that is at least one cycle wide, and synchronous to the domain in which it applies.


    which means understand when to use set/reset and when to use the clock enable.






Pushing the Logic from the Control Pin to the Data Pin
During analysis of critical paths, you might find multiple paths ending at control pins. 
You must analyze these paths to determine if there is a way to push the logic into the datapath without incurring penalties, 
such as extra logic levels. 

There is less delay in a path to the D pin than CE/R/S pins given the same levels of logic because there is a direct connection
from the output of the last LUT to the D input of the FF. 
The following coding examples show how to push the logic from the control pin to the data pin of a register.


Tips for Control Signals
Check whether a global reset is really needed.
Avoid asynchronous control signals.
Keep clock, enable, and reset polarities consistent.
Do not code a set and reset into the same register element.
If an asynchronous reset is absolutely needed, remember to synchronize its deassertion.


Duplicate logic to reduce fan out (from a register)
    Helps with timing. easier to route, but increases area.

Logic flattening. Understanding the nature of the function/algorithm from a system level.
Knowing the range of input/output? 
Register balancing.

duplicate register
register replication

Replicate High Fanout Net Drivers
Register replication can increase the speed of critical paths by making copies 
of registers to reduce the fanout of a given signal. 
This gives the implementation tools more flexibility in placing and routing the different 
loads and associated logic. Synthesis tools use this technique extensively.

Most synthesis tools use a fanout threshold limit to automatically determine 
whether to duplicate a register. Lowering this global threshold allows automatic 
duplication of high fanout nets. However, it does not allow control over which 
registers are duplicated or how their loads are grouped. In addition, the global 
replication mechanism does not assess timing slack accurately, 
which can lead to unnecessary replicated cells, logic utilization increase, 
and potentially higher power consumption.

For high frequency designs, a better approach to reducing fanout is to use a balanced tree for the high fanout signals. 
Consider manually replicating registers based on the design hierarchy, 
because the cells included in a hierarchy are often placed together. 
For example, in the balanced reset tree shown in the following figure, 
the high fanout reset FF RST2 is replicated in RTL to balance the fanout across the different modules. 
If required, physical synthesis can perform further replication to improve WNS based on placement information.


Often, a better approach to reducing fanout is to use a balanced tree for the high fanout signals. 
Consider manually replicating registers based on the design hierarchy, because the cells included in a hierarchy are often placed together.

AMD devices contain dedicated SRL16 and SRL32 resources (integrated in LUTs). These allow efficiently implemented shift registers without using flip-flop resources. However, these elements support only LEFT shift operations, and have a limited number of I/O signals:

Clock
Clock Enable
Serial Data In
Serial Data Out


A commonly used pipelining technique is to identify a large combinatorial logic path, break it into smaller paths, and introduce a register stage between these paths, ideally balancing each pipeline stage.


High Clock Skew or Uncertainty
-------------------------------------



*   Reduce skew, use parallel buffers instead of cascaded buffers
*   Use CLOCK_DELAY_GROUP
*   Check asynch clocks, add timing exceptions
*   Reduce uncertainty, check MMCM settings
*   Use BUFGCE_DIV for clock divider or dividing clocks.






revisit baselining for timing and design closure.






Somewhere
##########################

Clock gating
-------------------------------------
    No clock gating in an FPGA. you just use enables. You enable/disable a flip flop/register.
    use clock enable.
    
    Do no use FF output to drive clocks of other FFs.

.. code-block:: vhdl
  :linenos:   

    process (clk, rst) begin      
        if rising_edge(clk) then
            if data_vld = '1' then      -- data_vld is the clock enable
               din <= data_in;
            end if;
        end if;
    end process;
 
Clock enables are created when an incomplete conditional statement is coded into a synchronous block. 
A clock enable is inferred to retain the last value when the prior conditions are not met. 
When this is the desired functionality, it is valid to code in this manner. 


Division
-------------------------------------


Floating Point 
-------------------------------------




Additional Reading
##########################

https://docs.xilinx.com/r/en-US/ug949-vivado-design-methodology/Design-Creation-with-RTL
https://docs.xilinx.com/r/en-US/ug949-vivado-design-methodology/RTL-Coding-Guidelines
https://docs.xilinx.com/r/en-US/ug949-vivado-design-methodology/Design-Closure
https://docs.xilinx.com/r/en-US/ug949-vivado-design-methodology/Timing-Closure
https://docs.xilinx.com/r/en-US/ug949-vivado-design-methodology/UltraScale-Device-Clocking

https://www.intel.com/content/www/us/en/docs/programmable/683082/23-1/recommended-hdl-coding-styles.html

https://docs.xilinx.com/r/en-US/ug906-vivado-design-analysis/Introduction

https://docs.xilinx.com/r/en-US/ug906-vivado-design-analysis/Timing-Analysis

https://docs.xilinx.com/r/en-US/ug1388-acap-system-integration-validation-methodology/Timing-Closure