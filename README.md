-------------------------------------------------------------------------------------------------
Max Yarmolinsky, max.yarmolinsky@gmail.com
-------------------------------------------------------------------------------------------------

APPROACH

 I store the social network information and purchase histories as well as most other user data in dictionaries.
The social network is constructed by breadth first search with fixed stopping depth D. Purchasing statistics for each users network are calculated for the T latest purchases in a separate module. 
--------------------------------------------------------------------------------------------------------------------

DEPENDENCIES

I use the following common python libraries
1. sys  
 2. json
3. datetime               
4. math
5. queue 
6. OrderedDict  from collections                                                   
                                                    
NOTE that in python 2 the queue module is called Queue so if you are running my code with python 2.x you need to
    change the import statement in the snetworking.py module 
    
     import queue -> import Queue
     
and also change line 12 

     q= queue.Queue() -> q = Queue.Queue()

RUN INSTRUCTIONS

just execute run.sh


-------------------------------------------------------------------------------------------------------------------------------    
If the JSON log_input file is corrupted by invalid json the line will be skipped in my program and there is a printout. Valid json without required fields such as 'event_type' is also skipped with error message printed.
---------------------------------------------------------------------------------------------------------------------
My program updates the social network and the purchase statistics of each social network on each stream event.
I am finding that this causes the program to run a bit slower than desired, either some trade-offs must be made for
example only updating every T steps, or I need to see where my code can be optimized 


Thank you for your time and consideration!!

Max
