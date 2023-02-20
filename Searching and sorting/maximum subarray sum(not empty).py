import heapq 
from collections import defaultdict 
import math 
import collections
import time

mod=10**9+7
alp='#abcdefghijklmnopqrstuvwxyz'
cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit='1234567890'



#math.facorial(n)------>gives the factorial 



start=time.time()


for _ in range(1):
    
    n =int(input())
    #n,x =map(int,input().split())
    '''l=[]
    for   i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)'''
    #print(math.gcd(-2,-6))
    l=list(map(int,input().split()))
    cur =0 
    mx =-1*10**9-20 
    for i in range(n):
        cur+=l[i]
        mx =max(cur,mx)
        if cur<0:
            cur=0 
    print(mx)
    
    
    
    
    end = time.time()
    #print("time=", end-start)
    
    
   
            
    
    
    


