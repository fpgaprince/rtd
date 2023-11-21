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
            src="https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgbA7CAMB00IQFgJxvRzYQGZYFY0ccBGADjJ3zACZKVt9oR8Xn8BTAWhJIChyrKjXBIQSHCLBj8JGsxwD8rFEjFIEIEtBrrN7AdK0opY3cyPz8InCxh2AZgEMANgGcOMPgHcQPbHJkIAxadF5uuCK8IiHR9iQgAC4ATgCuHErMsfJaaqHMCSIGvv6hQaUkYMzQfACSfpUg8swVVfZwrPg+DdjNPU1GNQAykVpyfkhBcQUgzu6erMPGpmMr1bOuHnY1vtpmYiR5ul4j0goi1OfxG-Pb3XRTYcJlXr4PorjWHztNFMHYzxCP1U6kkwTyqGwP0OBy+YJIXx+8LhNjIYiWKBwAKxwRxNCBWhuW0WhiycLAQRQcJxzBy2kQDIQ3RB4k0LJwEChzLyHOwVJsFNeWmgGlZBRFChp3T2kr5guIXN8KHGgJVOWBKq+mIBiO6EB5X05QWeP31YmeZsi1W6ZAgNhxZE0CqFtpEGmYrtwUt8EE5uD9EDRuEFpr97pAvoBfpqlWYgfNgvjXqhTXFjIZfBGRuTEcF+JTCTmxKFkfEYNLkK8CNYFc0ZGoYvsXV8+D9zyqCl1LbbX1bAPVepFObAYOdpqH4YgQ7H3Sqxr9YEaWKCPznjbXvKrbUXAMFO5ztLT6aZpydOI7TQJzCLCyFa4kUmgQUrMeU4Cf67+4etvg0xq+D6fEU3R-kBrJBPIK7dPgOLOkgRgzi2OLhjB2KKuIoqbmoxohiBorhmoCjRqSGE4c+kwHqmwrHieZb2tggH5tcN53L++FgoR4hAkorCcShOTfiw9yYV8NAIV2TQiSI5ipj+wbGniISIfJjbLge9x2v6vSOipPw0Jp4b6TYxGxr8Ch5jpY5UfSNGZgM5p4pYV5EreekGWCRlcVy1ZNAZToAfoJY2FqOrAT6wUiJpJAmEKfTOoE6lvJohlnuhexaasunShOmjpZuMZtHEalFTS1k0bRSk4iETHrCxJK7BO8ITtxPnpeG5B6Os0LQJpzzaEpEnaL1XxDTYA67HFOLRApaV9O1k1pXlfq8CquG7G1uVLd5hVFYKK30fYdLlUs-VocK1XOXVQq8I1URtS1b43Z1YxBoJ0I0KOI00A2JrSh9EWhKO41aFisplDN12g42JBQ8pcgIctnlqe9RjzQj20FEje1I6VR3lXZcg-VN329AShabK5f2o-CYnqA9rDw89MMQoFzYRlEMVII00VhaRyx830PzYbJkmHnJkwFJzOmQUKEups+H4yz8sgcxcapySrVosG2wP3iEfHcWxzCVp5L4aW6sTNWlVsfGbvh69gFaGxGYYhCydvgnTAT3YtNuM15Qr4HkPMsEcxzK2HYiWjQ4d6pHEY8sDypjVk4w0I0yvLTFfZNBns4fiHa5K7OoqF6Kgsl2LgPSfo0F+unfJp3n9uKwXPU11BDWaTLo1a+9QOYx5tcAB4NDgUcoCAZAiNP4iSSAHAALapC4TiJBwAA6bgAMYuAA9tvADWW9uAAlgA5gAdq4mTBF89YBIgU8NoUTbMvfFH8hGMU-FwSlBqOIMSJUTmgtuhDiIRUbcRGF-MgRhk5T0GISK6NRR7KknigHQwR9TBGgLxeeAB1AAogAOQEAAnEU4xBrioSwOQCg+Cjx4DDRBj9bBwMnvsBey9V7ry3rvA+x83BnyvjfN4mlszOmzG5GeqUp613EZFWClCpQjBIAGKqjtSrXgpncNRjsgxcCMEmGYKDujMNkS0JADZHTWgiI0JMOkTGEhSOkcxRhbHyPkdaSoBwNG9GOBAPEeCbDbEcLovSToYp9GULzGJAV2ASRQgk8AmkhZgmsM+MEkBeZqUyXRFgYQkSCnDHkopIEjD5PgtQtJ0EcRVMqeUpCDFNCoUKZ3AOsSA45NliELptCunjmegMiSnpwyehzsrMIOcJnEQavhXKEp3wa23Is0UF53rJVyn0Wg6JoIxV2fkCwsddhQ3alDaQHTDmXJBtuCiq5jg9Oufc-ZUhNKECkCclg253mrI1mEHp+TJmMPEOUBE0lvoNFQHPY4p8HBb28MkLeG8AAOW8SDIoAI5b2SAAEwADRbwcCvFwILDhYKMVMJAvo-BgHwccAAEliolJK+AAFlblgqHOSrl6ImgEGlDgIcPAppCrEBYoUCCRUBDFWPNKsqeDcugGCRVez1o4i4FFBVtTTnCq1cKh6BQFXpRhoKVVhJbDFG8bSsQniZLdVFEY21mgnUlkMW7DVzsky6CCEmP+3kg7CkdVFJ85QopNDsF0eo2g-iaruhqtJMACBCQRGIbUDQhwoEMSaiNnQ6jBGzUqlV6VqjJrZtmHgYQyCNErR07MJNcxgqaXzLgOkZR+B0kLCiEr00Sq7WCvI1bsA8DyDUeocDxWmuCOMaV7Qy1KFtTWqdE65WEiKEJEYzwR2gIHXy8mtwSSbq+DwHWYLoz2DMUekQXAZaSHKErC9uj6pgS4BRd4gxuhbuln8Z2W64jvASjGAa16ZbVL8DLGwIKY4JGsMc9gH0YViG8BwAA5MkTeO8XBCPPmvU+l9z5bwAEbby3pfPeW8ODX0Iy4DDe9L5Ev3iitwfAuaTx9SwABOR8BBggJUY05sIx4h0hSOSnlJHjBE7FTSnjx7UM7Sx6KWg2gSv+g0cY2hjiKDeLGiiW6XnafKJZY98mDNqYBn28x1jeiaVfTY2u9QuCytINe50zm515oc0xTyjm8SJo6EJTz1UVXOlU6WvNqbwM-RnU59TEaDARZvQ2bzXnw3rq6Alhtqmb1BaiHFoSHLbPWevUwMwiaaACpKDgIMWWQtgl-lVswRhHPVbq5ZxotM-ANfskKZrpWXO+d5q+9rNmuueXqwA6LsFxi-y5tpFoo2TMNBipIFoDaVs9cyzpG97XFuJYCZO6JXyb3l0dZl0Uv9TIKrW0OX+mWmvqN6B+hEVjhvXqs75XLtg81MLULYCAmJwNBO-gxeecKcW4uZW4RFhKPCLxRYkAAnuYrrbnetmR6yHGOB23sdJ4DFV9EEdMdPeK22ksaP2mddSe4dFOGj13u36V1elY1xH8C0aY5jTISrZ7gG79xhNbZkpJ276zBcnbkm5yTMsbmRKCDc7b2AZfmIbqIe9O25J45Tktz5artfgGOB1fXuvDeHNk+AeTDm4ieNdZ4sLQlfB2sdele1yvxcZv2HJb13a-jsd-j773hONcq7oC0H3u2Q7rdJ33cxlkchR4bX72kDZ60NmhGpc1pqIK09KB1zP3XUHyKCEGGNReoBcLxfwrDW9cV70Xk4PDW8UVOGERwCHbg94ADcODJBBVwWQUB1EgeIFoCA9KkNIsw0ImvdeG9uCby3tvnfu8gurQURoDA7qcPnokcjO9XAkbcA4OFe8AD6xKXCkqYUwDmw7SABDQIhpIu-t776Jcfk-S94dI4AEp+H-pOnkYvXNTQcrVgUA9zW+GEF4EOBKV+K1KA8FXIA4b0F4LpBKR0KCZ7F4TxB7a1OAlNJgLxf7KIMIYgtdN+CaIILpDJXUIAA" 
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
