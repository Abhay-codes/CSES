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
    l.sort()
    st =min(l)
    en =max(l)
    mn =10**18
    while(st<=en):
        mid=(st+en)//2 
        sm1=sm2=0 
        for i in range(n):
            if l[i]<mid:
                sm1+=abs(l[i]-mid)
            else:
                sm2+=abs(l[i]-mid)
        sm =sm1+sm2 
            
        mn =min(sm,mn)
        if sm1<sm2:
            st=mid+1 
        elif sm1==sm2:
            break
        else:
            en=mid-1
    print(mn)
    
    
    
    
    end = time.time()
    #print("time=", end-start)
    
    
   
            
    
    
    


