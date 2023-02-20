import heapq 
from collections import defaultdict 
import math 
import collections



mod=10**9+7
alp='#abcdefghijklmnopqrstuvwxyz'
cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit='1234567890'



#math.facorial(n)------>gives the factorial 






for _ in range(1):
    
    n =int(input())
    #n,m =map(int,input().split())
    '''l=[]
    for   i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)'''
    #print(math.gcd(-2,-6))
    #l1=list(map(int,input().split()))
    l1=[]
    l2=[]
    vec=[]
    for i in range(n):
        a, b =map(int,input().split())
       
        l1.append(a)
        l2.append(b)
    
    
    c=0 
    l1.sort()
    l2.sort()
    mx =0
    i =0 
    j =0 
    while(i<n and j<n):
        if l1[i]<l2[j]:
            c+=1 
            i+=1 
        else:
            c-=1 
            j+=1 
        mx=max(c,mx)
    print(mx)
    
    
   
            
    
    
    


