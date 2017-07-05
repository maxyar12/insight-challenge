-------------------------------------------------------------------------------------------------
This readme file describes my code that I am submitting to the insight anomoly_detection challenge
 - Max Yarmolinsky, max.yarmolinsky@gmail.com
-------------------------------------------------------------------------------------------------

APPROACH

I code with Python. I store the users in a list. I store the social network information and purchase histories 
as well as most other user data in dictionaries. The friend network is stored as an adjacency list. The social network is 
constructed by breadth first search with fixed stopping depth D. Purchasing 
statistics for each users network are calculated for the T latest purchases in the network in the module snpurchasestats. 
--------------------------------------------------------------------------------------------------------------------

DEPENDENCIES

I use the following common python libraries:
                                                    1. sys  
                                                    2. json
                                                    3. datetime               
                                                    4. math
                                                    5. queue 
                                                    6. OrderedDict  from collections                                                   
                                                    
 # (NOTE that in python 2 the queue module is called Queue so if you are running my code with python 2.x you need to
    change the import statement from import queue -> import Queue)
---------------------------------------------------------------------------------------------------------------------

RUN INSTRUCTIONS

just execute run.sh

I also want to repeat that in python 2 the queue module is called Queue so if you are running my code with python 2 you need to
    change the import statement from import queue -> import Queue
