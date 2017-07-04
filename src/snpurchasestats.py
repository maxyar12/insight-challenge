# this calculates mean and standard deviation from the purchase history
#  of the last T transaction from the users D degree social network

import datetime
import math

def buildstats(snetwork,purchases,T):
     meansSDs = {}
     snPurchaseHistory = {}  
     for person in purchases.keys():
         allSNetworkPurchases = []
         for friend in snetwork[person]:
             for purchase in purchases[friend]:
                 allSNetworkPurchases.append(purchase)
         allSNetworkPurchases.sort(key=lambda x: datetime.datetime.strptime(x[1],'%Y-%m-%d %H:%M:%S'))
         snPurchaseHistory[person] = allSNetworkPurchases[-T:]               # collect only T latest purchases in Social network
         mean = 0.0
         sd = 0.0
         for purchase in snPurchaseHistory[person]:
             mean = mean + float(purchase[0])                             # begin calculation of the mean for this person
         try:
             mean = mean/float(len(snPurchaseHistory[person]))
             for purchase in snPurchaseHistory[person]:
                sd = sd + (float(purchase[0])-mean)*(float(purchase[0])-mean)    # calculate sd 
             sd = math.sqrt(sd/float(len(snPurchaseHistory[person])))   
         except ZeroDivisionError:
             pass         
         meansSDs[person] = [mean,sd]
     return meansSDs,snPurchaseHistory
    