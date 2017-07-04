# handle purchases of a user based on date and parameter T
# the idea is to only keep track of the T lastest purchases made by a user
# later these purchases will form the purchases of other users social network

import datetime

def handlepurchase(id,amount,time,purchases,T):
    if len(purchases[id]) < T:                  # only need 50 purchases
        purchases[id].append([amount,time])
    else:
        purchases[id].sort(key=lambda x: datetime.datetime.strptime(x[1],'%Y-%m-%d %H:%M:%S'))           # sort by date
        if datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S') > datetime.datetime.strptime(purchases[id][0][1],'%Y-%m-%d %H:%M:%S'):
            del purchases[id][0]
            purchases[id].append([amount,time])