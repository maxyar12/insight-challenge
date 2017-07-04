# This is the main program that detects purchase anomolies
# building/updating the social network is handled in the module snetworking
# Calculations of means and sds of the purchases in the social network are handled in the module snpurchasestats
# keeping track of purchases is handled by the module purchasehandler
# By Max Yarmolinsky -> 646-326-2959, max.yarmolinsky@gmail.com

import sys
import json
import datetime
from collections import OrderedDict
import snetworking
import snpurchasestats
import purchasehandler

users = []                  # a list of the active user ids
friends = {}                # This adjacency list (D=1) stores friend information for each person 
SNetwork = {}               # D degree social network for each user
purchases = {}              # last T purchases made for each user
snPurchaseHistory = {}      # last T purchases gathered from a user's social network (NOT including user's purchases)

def userinit(userid):                  # initialize new users + their properties
    if userid not in users:
        users.append(userid)
        friends[userid] = []
        purchases[userid] = []
        SNetwork[userid] = []
        snPurchaseHistory[userid] = []
            
batch_path = sys.argv[1]
first_line = open(batch_path,'r').readline()      # Read in the input parameters D, and T  
params = json.loads(first_line)                   
D = int(params['D'])
T = int(params['T'])

batch_file = open(batch_path, 'r')               
iterb = iter(batch_file)                         
next(iterb)                                        # skip the first line of batch_file

for line in iterb:
    ev= json.loads(line)                  
    if ev['event_type'] == 'befriend':               
        userinit(ev['id1'])
        userinit(ev['id2'])          
        friends[ev['id1']].append(ev['id2'])         # update adjacency list
        friends[ev['id2']].append(ev['id1'])         
    elif ev['event_type'] == 'unfriend':
        friends[ev['id1']].remove(ev['id2'])         # update adjacency list
        friends[ev['id2']].remove(ev['id1']) 
    elif ev['event_type'] == 'purchase':
        userinit(ev['id'])
        purchasehandler.handlepurchase(ev['id'],ev['amount'],ev['timestamp'],purchases,T)    # handle purchase
                
SNetwork = snetworking.buildSN(friends,D)       # initial social network from batch file
(means_and_sds,snPurchaseHistory) = snpurchasestats.buildstats(SNetwork,purchases,T)         # get means, sds, social network purchase histories

stream_path = sys.argv[2]                            #  start reading from the stream and do anomoly detection
stream_file = open(stream_path, 'r')
out_path = sys.argv[3]
out_file = open(out_path, 'w')
out_file.close()

for line in stream_file:
     ev = json.loads(line,object_pairs_hook=OrderedDict)
     if ev['event_type'] == 'befriend':               
         userinit(ev['id1'])
         userinit(ev['id2'])          
         friends[ev['id1']].append(ev['id2'])         # update adjacency list
         friends[ev['id2']].append(ev['id1'])  
         SNetwork = snetworking.buildSN(friends,D)                                               # update social network
         (means_and_sds,snPurchaseHistory) = snpurchasestats.buildstats(SNetwork,purchases,T)    # rebuild stats/history     
     elif ev['event_type'] == 'unfriend':
         friends[ev['id1']].remove(ev['id2'])         # update adjacency list
         friends[ev['id2']].remove(ev['id1']) 
         SNetwork = snetworking.buildSN(friends,D)
         (means_and_sds,snPurchaseHistory) = snpurchasestats.buildstats(SNetwork,purchases,T)
     elif ev['event_type'] == 'purchase':
         userinit(ev['id'])
         print(ev['id'])
         print(len(snPurchaseHistory[ev['id']]))
         if len(snPurchaseHistory[ev['id']]) >= 2:                                                   # anomoly detection
             if float(ev['amount']) > means_and_sds[ev['id']][0] + 3.0*means_and_sds[ev['id']][1]:   # anomoly detection
                 print('anomoly of ' + ev['amount']+' for user '+ev['id'])                           # flag + write to 
                 flagged_event = json.dumps(ev,separators=(', ',':'))[0:-1] + ', "mean":'+ '"'+"%.2f" % means_and_sds[ev['id']][0]+ '", "sd":' +'"'+"%.2f" % means_and_sds[ev['id']][1] +'"}' 
                 with open(out_path, "a") as myfile:
                     myfile.write(flagged_event + '\n') 
         purchasehandler.handlepurchase(ev['id'],ev['amount'],ev['timestamp'],purchases,T)
         (means_and_sds,snPurchaseHistory) = snpurchasestats.buildstats(SNetwork,purchases,T)
         
print(SNetwork)
print(means_and_sds,snPurchaseHistory)

print(friends)
         




    