-------------------------------------------------------------------------------------------------
This readme file describes my code that I am submitting to the insight anomoly_detection challenge
 - Max Yarmolinsky, max.yarmolinsky@gmail.com
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
If the JSON log_input file is corrupted by invalid json the line will be skipped in my program and there is a printout. Valid json without required fields such as 'event_type' is also skipped with error message printed. My program will break if the json values are incorrect types in the log file. For example, something like "amount":"5g0dk" which cannot be converted to a number will break my program. I chose not to implement exception handling of these values due to time constraints, but I could easily handle this issue if needed. (I noticed that I only checked for missing keys when reading the batch_log and not when reading the stream_log, but at this 
point I don't want to make any further changes because the project is due soon)
---------------------------------------------------------------------------------------------------------------------

Thank you for your time and consideration!!

Max
