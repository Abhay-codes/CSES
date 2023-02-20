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
    #n,m =map(int,input().split())
    '''l=[]
    for   i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)'''
    #print(math.gcd(-2,-6))
    #l1=list(map(int,input().split()))
    l=[]
    
    vec=[]
    for i in range(n):
        a, b =map(int,input().split())
       
        l.append([a,b])
       
    
    
    c=1
    l.sort(key=lambda x:x[1])
    #print(l)
    mx =1
    st =l[0][0]
    en =l[0][1]
    for i in range(1,n):
        start=l[i][0]
        end =l[i][1]
        if start>=en:
            c+=1 
            en =end 
            
        
    print(c)
    
    
    
    
    end = time.time()
    #print("time=", end-start)
    
    
   
            
    
    
    


