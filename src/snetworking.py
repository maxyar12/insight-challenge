# July 2, 2017
# Defines two functions: 1) build social networks from batch_log data
#                        2) update existing social networks based on stream events
#
# Uses Breadth first search with fixed stopping depth D (to layer D in the BFS)
# to create social network of degree D

import queue

def buildSN(adj_list,max_depth):
     SNetwork = dict([(key,[]) for key in adj_list.keys()])         # initialize the Social Network
     for person in adj_list.keys():
         d = dict([(key,False) for key in adj_list.keys()])       # boolean for storing whether node has been explored          
         q = queue.Queue()
         q.put(person)                                            # add source node to queue
         d[person] = True                                        # mark source node as explored
         current_depth =0                                         # these variables are necessary
         Count_to_depth_increase=1                                # to keep track of the depth
         next_Count_to_depth_increase=0                           # ...
         while not q.empty():                       
             v=q.get()                                     
             for link in adj_list[v]:
                 if d[link] == False:
                     d[link] = True
                     q.put(link)
                     SNetwork[person].append(link)
                     next_Count_to_depth_increase += 1
             Count_to_depth_increase -= 1
             if Count_to_depth_increase == 0:
                 current_depth += 1
                 if current_depth > max_depth-1:
                     break
                 Count_to_depth_increase = next_Count_to_depth_increase
                 next_Count_to_depth_increase = 0                                                    
     return SNetwork
     

