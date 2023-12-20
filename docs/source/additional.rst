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


review cache, i think by using the BRAM, we can implement a cache system.. and so all that stuff is going to apply.    

note xilinx uses 18kB and 36kB BRAMs.. and the total will vary with different family and tiers, will higher tier having more naturally..
64,000kB = 64MB.
4K x 9, 2K x 18, or 1K x 36
An 18 Kb block RAM can be configured with independent port widths for each of those ports as 2K x 9 or 1K x 18 (when used as TDP memory).

Terminology..
    simple dual-port (SDP)
    true dual-port (TDP) memory)

BRAM is the memory. FIFO is just a data structure we apply. Data structure is basically rules we set for organizing data for storage and retrieval.



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

