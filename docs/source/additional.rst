************************
Additional
************************

Knowledge in these area will aid in understanding applications of FPGAs.
Because it is versatile, it is also a cross-section of many different engineering subjects/topics.
NOTE ONLY COVER THAT WHICH YOU'VE DONE. 
other areas will be brief.

Digital Electronics
##########################

Signal and Systems
##########################

DSP
##########################

VLSI 
##########################

Circuits
##########################

Microelectronics
##########################

Computer Architecture
##########################

Data Structure
##########################
these are just conversations with myself..



try to implement or think about everything with a RAM. what are the challenge, limitations, is it even worth
RAM is address and data. it is basically an array, with the address being the indices!
    if data is added to the RAM, unsorted, it will take o(n) time to search for it.
  
    if you add some function for the address/indice, it is like keying it or hashing it. which will become o(1).

    would you want to sort RAM? does that even make sense? because you would have to perform a bunch of read and writes..
    eating up your cycle counts. this doesn't sound viable you're probably going to be writing to RAM every cycle.
        unless you are not writing every cycle. and it is some form of burst.

    similar to hashing or creating a look up, if you perform additional stats? what do you call it.. 
    what i am trying to say is keep track of for instance min, max values and the current wr address as you input data.
    can have total
    so you'll have some supporting logic/registers for common ____.
    Properties.

    i think if it is a dual port RAM, you can read from both ports.. and cut the search in half.
    but each half is still an o(n) search..

    it seems at this point.. the best thing to do is to have some way of determining where to place the data/what address to use.
    a system for inputing/inserting/adding/ and reading/retrieving data.
    a hash function.. then you can find it precisely without having to search later. 
        this brings up.. what if the data coming in results in the same key.. how do you prevent over writing if data is already there.
        how do you now data is already there or not?

    when data comes in we must parse it. or if data is there and something else needs to look or search for it, it is query/querying the database.

review cache, i think by using the BRAM, we can implement a cache system.. and so all that stuff is going to apply.    

note xilinx uses 18kB and 36kB BRAMs.. and the total will vary with different family and tiers, will higher tier having more naturally..
64,000kB = 64MB.
4K x 9, 2K x 18, or 1K x 36
An 18 Kb block RAM can be configured with independent port widths for each of those ports as 2K x 9 or 1K x 18 (when used as TDP memory).

Terminology..
    simple dual-port (SDP)
    true dual-port (TDP) memory)

BRAM is the memory. FIFO is just a data structure we apply. Data structure is basically rules we set for organizing data for storage, retrieval and/or modification.

can you implement trees like binary tree or other trees using BRAM?



everything has led me to, you want to make a mini database with the RAM. or cache? 
https://www.cise.ufl.edu/~mschneid/Research/papers/HS05BoCh.pdf

some things to maybe explore.. SQL (structured query language).. meh... DBMS (database management system)


i imagine t o speed up algorithms or what not, you want to implement some of the data structure in hardware. that way you can offload or 
do some of the decisions in the FPGA before even passing it on, as in it may not even need to go up to the next level. we can handle it
in the low/hardware level. but to do that we have to imitate/replicate the structure used above.

i imagine at the next layer up.. it is basically a database, that is constantly changing as more info comes in.


reminder o(n) is "linear"... duh.. so sometimes they'll just say linear complexity or the search is linear or the algo is linear. like wise with retrieval.

merge sort divides in half, but each half has to iterate n. half is logn. n times. o(nlogn)




Hash functions calculate the address of the page in which the record is to be stored based on one or more fields in the record
hashing functions chosen to ensure that addresses are spread evenly across the address space
‘occupancy’ is generally 40% to 60% of the total file size
unique address not guaranteed so collision detection and collision resolution mechanisms are required
Open addressing
Chained/unchained overflow

B tree vs B+ tree?

Can we create BRAM binary tree? in which each block is like a node with children. but this would be like creating that mapping externally.. not linked
by the BRAM. so the structure is external searched and then pointed to the RAM.. which is kind of like hashing isn't it?

if you use multiple BRAM, you pay the price of a clock cycle to talk one before the other, if there are multiple level etc.

what if we read before write.. such that we present the address and well before we put the data in we frame/structure/TAG! it some way..
so that we can decode and know whether we can write to it or not all within or before a period/cycle.

can we jump to an address and then start the search? again.. this requires some addressing system. and then its N iterations as we read.

if we create an external tree.. we'd still need some form of memory right? we'd use registers.. and so then every entry into bram would require registers to hold value.
and point to some address location.. well.. won't we start using up the FF resources with this approach? yes..

it seems the best is to have some method/function/hash/encoder/decoder so that we can determine it in one cycle.



If you want to find the position in an unsorted array of n
 integers that stores a particular value, you cannot really do better than simply looking through the array from the beginning and move toward the end until you find what you are looking for. This algorithm is called sequential search. If you do find it, we call this a successful search. If the value is not in the array, eventually you will reach the end.




---------

it seems what i need to look at is cache..

as that is basically data storage and retrieval at the hw level. and is the fastest memory type next to registers.

can we use cache ing techniques to store incoming data into BRAM?

    (fully) associative mapping
        store the content and addresses of the memory word. Any block can go into any line of the cache. This means that the word id bits are used to identify which word in the block is needed, but the tag becomes all of the remaining bits.
        ah.. it stores the WORD, not blocks so in direct map.. we store blocks of N words. here we store a single WORD with its address as part of the TAG. and so it is unique. and can be placed anywhere.
            This indicates that there is no need for a block field. 

        when you search though you compare ALL tags in the cache for a hit/miss.
        this last 2 bit thing regarding which word in the data block.. tells me the block of data comes in with an address. that address is used to create the tag.. so tag is unique.
        when writing from main to cache, it just steps thru or looks for an empty line/unused/unoccupied. adds tag and block.
        when checking. check if empty. if empty. write there. if not increment line until empty.
        when searching cpu will present desired or search tag. check valid first, means somewhere its in there. then ln by ln or check all at once and flag the ln the data is in. and present data.

        when cache full, can use LRU least recent used to determine which to drop/overwrite.

         However, a fully associative cache is expensive to implement.
            — Because there is no index field in the address anymore, the entire
            address must be used as the tag, increasing the total cache size.
            — Data could be anywhere in the cache, so we must check the tag of 
            every cache block. 

    direct mapped, block address reserved for certain data types
        The simplest technique, known as direct mapping, maps each block of main memory into only one possible cache line. 
        or In Direct mapping, assign each memory block to a specific line in the cache. 
        If a line is previously taken up by a memory block when a new block needs to be loaded, the old block is trashed. "overwritten"
        "thrashing", results in high misses.

        so a block contains a x words, say 4 words 32bit each. say main memory has 10blocks.
        cache has 5 lines. blocks 1 ln1, 2 ln2, ...5 ln5, 6 ln1, 7ln2, 10 ln 5.. 
        block# mod 5. so if block 10 comes in, and you already have something at ln 5, it gets over written.. even if the old data belonged to block 5.

    set associative
        Set associative addresses the problem of possible thrashing in the direct mapping method. It does this by saying that instead of having exactly one line that a block can map to in the cache, we will group a few lines together creating a set.

        An intermediate possibility is a set-associative cache.
        — The cache is divided into groups of blocks, called sets.
        — Each memory address maps to exactly one set in the cache, but data 
        may be placed in any block within that set.

        N way associative = N blocks in a set. cache is divdied into sets.



in summary.. direct map uses creates memory blocks, so there is overlap, think of mod function. nothing to handle overlap, just overwrite.. 
associative uses entire addr so each cache line is unique, memory can be written anywhere.
set associative is hybrid of the two. part of the address is used to index into cache set. which is like directmapping. 
once in a set, use associative. ie use the rest of address. so that ln is unique, and you can place anywhere
in both associative method, replacement is done by LRU.


when CPU does find data in cache and operates on it and returns it to cache, this needs to flow back to main memory or whereever.

just for reference, CPUs 
CPU registers, counters, pointers, etc
L1 cache can be 2KB to 64KB (kinda like our BRAMs!!), holds instructions
L2 cache can range from 256KB to 512KB.
L3 cache can be 1MB to 8MB.




Using Dedicated Blocks or Distributed RAMs
RAMs can be implemented in either the dedicated block RAM or within LUTs using distributed RAM. The choice not only impacts resource selection, but can also significantly impact performance and power.

In general, the required depth of the RAM is the first criterion. Memory arrays described up to 64 bits deep are generally implemented in LUTRAMs, where depths of 32 bits and less are mapped 2 bits per LUT and depths up to 64-bits can be mapped one bit per LUT. Deeper RAMs can also be implemented in LUTRAM depending on available resources and synthesis tool assignment.

Memory arrays deeper than 256 bits are generally implemented in block memory. Xilinx devices have the flexibility to map such structures in different width and depth combinations. Familiarize yourself with these configurations to understand the number and structure of block RAMs used for larger memory array declarations in the code.

cache takes blocks of words from main memory. and adds a tag/header. a cache "line" can hold multiple main memory words. a word can be 32bit, 64bit, etc. so you could have N words per tag! N words making up a "block".
in other words..
cache is made up of "lines" 
each line has a tag and block of memory.
each block of memory consists of words.
if for instance a block is defined as 4 words, and a word is 32bits.
then each cache line holds 4*32bits of memory.. 128bits plus the tag.


i think you can implement hashing system on the BRAM. your key can be a time stamp or something in addition to whatever, this way we ensure uniqueness.
at this point i dont even know what the data is 

building an efficient order book, with efficient ways to manage best bid/ask) is important because I care about speed and scalability of processing market data 



---------

SHA - secure hash algorithm

stack - LIFO, last in first out. push pop. max size/ top. stack/frame pointer. check overflow underflow 
which is the same as checking full vs. empty in our fifos.
    back tracking, depth first search.

queue - FIFO, first in first out. first come first serve. enqueue, dequeue
read write counter pointers, empty, full flags 

hash table
From wiki..
In computing, a hash table, also known as a hash map, is a data structure that implements an associative array, also called a dictionary, which is an abstract data type that maps keys to values.[2] A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.
In many situations, hash tables turn out to be on average more efficient than search trees or any other table lookup structure. For this reason, they are widely used in many kinds of computer software, particularly for associative arrays, database indexing, caches, and sets.

associative array.. 2D array. one row key. other row data. key and data correspond to the index.

sparse matrix
binary search tree

the above are definitely things that can be implemented in HDL/hardware.

heap - is dynamic memory

do i reallly need to know lists?
maybe revisit comp arch to see which of the comsci can be applied

Algorithm
##########################
At the heart of everything are algorithms. and state machines.
breadth first serach

O(1) - Excellent/Best, independent..
O(log n) - Good, cut in half
O(n) - Fair, for loops
O(n log n) - Bad, loops of cut in half lol
O(n^2), O(2^n) and O(n!) - Horrible/Worst, nested loops

https://www.bigocheatsheet.com/


parsing data.


Controls
##########################

Networking
##########################
add your diagrams..

OSI layer
TCP/IP
UDP
Ethernet
MAC
PCS/PMA
frames
packets

Operating Systems
##########################

<<<<<<< HEAD
Linear Algebra
##########################
=======


IDK..
##########################
log10(n)/log10(2) --> log2(n)
    10^x = y

ln(n)/ln(2)
    e^x = y

    e = 2.71828 = euler's number
pi = 3.14159
3db point = half power point = 0.70712 = 1/sqrt(2)

POWER is 10log10(x)
AMPLITUDE is 20log10(x), gain vs frequency bode


AMDAHL's LAW!
impact of optimization to overall system.

S(latency) = 1/ [(1-p)=(p/s)]

multiple components
= 1/[p1/s1 + p2/s2 + p3/s3]



IDK..
##########################
Level2 is not free.
low latency ethernet (MAC and PCS/PMA)
    systems are currently 10G
    is traffic continuous?
        most likely not

802.3, which is within 100 ppm of 312.5 MHz for 40G and 390.625 MHz for 50G.

time stamp 1588v2 PTP 1-step and 2-step timestamping
modify TCP/UDP 

data feed handler
    ie decoder, parser
    FIX ITCH OUCH encode decode

packet processor, router/traffic management


update books


cycle counts..
1us = 1000ns
300mhz = 3.33ns

390.625mhz = 2.56ns

312.5 = 3.2ns
156.25mhz = 6.4ns

xaui input 
if 156.25
64bit
64 + (64/8 * 2) = 80
64(10/8) = 80
80*156.25 = 12500 Mbps = 12.5Gbps / 4 = 3.125Gbps per lane --> 12.5G/10G
if we double the fq.. 
80*312.5 = 25000 Mbps = 25Gbps / 4 = 6.250Gbps per lane --> 25G/20G


256(66/64) = 264
264 * 156.25 = 41250 Mbps = 41.250 Gbps / 4 = 10.3125 Gbps per lane --> 40G, this is wrong.

128(66/64) = 192
192 * 156.25 = 30,000 Mbps too low.. this is wrong

thus the 312.5 requirement.. and 390.625
192 * 312.5 = 60,000Mbps = 60Gbps = 60G this is write, can support 40G and 50G
192 * 390.625 = 75000Mbps = 75Gbps (up to)

note available line code types.. 8/10, 64/66, 128/130

one more..
 CAUI-10 (10 lanes x 10.3125G), CAUI-4 (4 lanes x 25.78125G) 


note to self...
RX is 128 bit, but we get 64bit at a time or only 64bit is enabled..
ENA1 for top half. EN0 is bot half.
I think this is straddle.. where we present 128, but only 64 viewed /process

what is axi straddle packet
The AXI4-Stream transmit interface consists of two segments, 
where each is 64-bits (8 bytes) wide. 
128bit = 16 bytes

This segmented approach or straddled AXI4-Stream approach 
as it is referred to allows for greater efficiency 
such that a packet can start and end in any given segment or cycle.

need to send 73bytes? 73/16 = 4.5626 --> need 5 cycles.
need to send 115byte? 115/16 = 7.1875 --> need 8 cycles.
need to send 81bytes? 81/16 = 5.0625 --> need 6 cycles.




IDK too
##########################

end to end application
runtime

valgrind
callgrind
gprof

functions which consume the most execution time
measure runtime gprof.
add timers and performance counter 


throughput, volume data process per run time
usually limited by PCIe

xbultil to test DMA to determine upper bound of throughput/data transfers


look at profiling, in multi threaded app, consider effects of parallelism
identify bottleneck and potential

    computational complexity of the functions.. cubing? dividing? multiplying?
    
    computational intensity of the function.. what does that mean? like how often? or how long it takes?
    
    data access locality, do we have to access global memory. 
    global memory is the "local" DDR. ie memory on the FPGA PCB. in which the PCB is the ALVEO PCB 
        this is similar to GPU in which it has local DDR memory.
            which is differnt to the DDR memory on the motherboard used by the CPU. they call CPU memory host memory.
                host memory is the DDr on the mobo, or server mobo. like at home.
    
    throughput of the function, how much data /run time or per clock cyle.


use multiple kernel instances.

a kernel is the FPGA RTL which accelerates whatever function for the CPU.
inside the kernel is the compute unit

an FPGA can have multiple kernels. for different applications!

reduce CPU idle time, maximize FPGA/ kernel utilization ... ie CPU is sequential. we're taking a piece of that sequence out 
and doing it in the fpga. therefore we need to get the CPU to do something else in the mean time/ until data is ready again.
custom data path

reduce overhead of enqueing kernel with data?
optimizing data movement.. transfers betweeen host, memory and kernel.
scheduling compute units, again to maximize their usage.
    i think i saw somewhere, where it may need to time to ramp up like a fifo.. so there is penalty for something like that.

memory accesses or basically penalties.

for FPGA.
throughput goal, latency, datapath width, number of engines, interface bandwidth


parition code into load, compute, store.
    memory architecture is responsible for moving data in/out of kernel.

ping pong / buffer io?

decompose compute block to identify throughput goals
look for single loop nest
connect compute using dat flow?

loop unrolling
array partitioning

io contentions? memory being accessed multiple times in one loop iteration..

loop carried dependencies.

create internal cache..
reconfiguring io and memories architecture

interface optimization. use burst data transfers. use full axi data width.
    pipeline code for burst transfers

optimizing kernel to kernel communication. stream data between K2K, axi stream
optimze mem architecture, array partition.
optimize computational paralllism.. coding data parallism. task parallelism. dta flow.
        looop parallisim, unrolling loops. pipelining loops.

optimizie compute units device resources.. data width, macro operations. fixed point arithmetic.
                                                        using optimized libraries.

topological optimization. use multiple compute units... using multiple DDR banks.



i think the key to acceleration is determing which functions or algo we want to run on FPGA.
convert these functions to C/C++ kernels. and convert host code to use openCL, which 
talks to PCIe or kernel. so we can call and schedule or use the fpga/kernel, which has the compute.
but we all need to load, compute, store.




reminder.. note
pointer points to a memory location.



command from host thru pcie to fpga can take 30 to 60us! thats signifiicant latency.



optimize data transfer before, data movement. before data computation.

CU = compute unit













>>>>>>> a51d9f50d900c04260d48674647ae55426bda731