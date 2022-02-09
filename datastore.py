#from main import *
from collections import Counter
'''
This is to collect the rolls to then derive data from the information.
'''



def collect(roll):
    print("From datastore.collect() " + str(roll))



#Initialize list
alist = []
count = 0

def counter(roll):
    global count
    #Read up on namespaces inside of Python
    alist.append(roll)
    c = Counter(alist) #sort by most common occurances
    count += 1
    #Why can this function see this variable but couldn't see count without global?
    print(str(c) + " datastore.counter()")
    print("Count: " + str(count) + '\n')
    return c #<collections.Counter()>



'''Testing'''
#counter(0)
#counter(11)
#counter(1)
#counter(11)
#counter(11)
#counter(2)
#counter(3)