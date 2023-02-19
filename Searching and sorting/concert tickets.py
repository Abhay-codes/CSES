import heapq 
from collections import defaultdict 
import math 
import collections
import bisect



mod=10**9+7
alp='#abcdefghijklmnopqrstuvwxyz'
cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit='1234567890'



#math.facorial(n)------>gives the factorial 






for _ in range(1):
    
    #n =int(input())
    n,x =map(int,input().split())
    '''l=[]
    for   i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)'''
    #print(math.gcd(-2,-6))
    l=list(map(int,input().split()))
    
    l2=list(map(int,input().split()))
    #print(l)
    #print(n)
    l.sort()
    for i in l2:
        k =bisect.bisect_right(l,i)-1 
        #print(k,"k")
        #print(k)
        if k==-1:
            print(-1)
        else:
            print(l[k])
            l.pop(k)
        
        