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


can we use cache ing techniques to store incoming data into BRAM?

    associative mapping

    direct mapped, block address reserved for certain data types

    set associative










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

