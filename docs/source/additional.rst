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

what if we read before write.. such that we present the address and well before we put the data in we frame/structure/TAG! it some way..
so that we can decode and know whether we can write to it or not all within or before a period/cycle.

can we jump to an address and then start the search? again.. this requires some addressing system. and then its N iterations as we read.

can we use cache ing techniques to store incoming data into BRAM?

    associative mapping
        store the content and addresses of the memory word. Any block can go into any line of the cache. This means that the word id bits are used to identify which word in the block is needed, but the tag becomes all of the remaining bits.
        ah.. it stores the WORD, not blocks so in direct map.. we store blocks of N words. here we store a single WORD with its address as part of the TAG. and so it is unique. and can be placed anywhere.
        when you search though you compare ALL tags in the cache for a hit/miss.
        this last 2 bit thing regarding which word in the data block.. tells me the block of data comes in with an address. that address is used to create the tag.. so tag is unique.
        when writing from main to cache, it just steps thru or looks for an empty line/unused/unoccupied. adds tag and block.
        when checking. check if empty. if empty. write there. if not increment line until empty.
        when searching cpu will present desired or search tag. check valid first, means somewhere its in there. then ln by ln or check all at once and flag the ln the data is in. and present data.

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

------------------

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

heap 

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

