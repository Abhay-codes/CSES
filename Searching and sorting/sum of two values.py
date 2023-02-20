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
    
    #n =int(input())
    n,x =map(int,input().split())
    '''l=[]
    for   i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)'''
    #print(math.gcd(-2,-6))
    l1=list(map(int,input().split()))
    l=[]
    for i in range(n):
        l.append([l1[i],i+1])
    l.sort()
    start =0 
    end =n-1
    ans=[]
    
    while(start<end):
        sm=l[start][0]+l[end][0]
        
        if sm==x:
           
            ans=[l[start][1],l[end][1]]
            break
        elif sm<x:
            start+=1 
        else:
            end-=1 
    if ans==[]:
        print("IMPOSSIBLE")
    else:
        print(ans[0],ans[1])
        
    
    
    
    end = time.time()
    #print("time=", end-start)
    
    
   
            
    
    
    


