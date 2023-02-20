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
        vec.append([a,1])
        vec.append([b,-1])
        l1.append(a)
        l2.append(b)
    
    
    c=0 
    vec.sort()
    mx =0
    for  k in vec:
        c+=k[1]
        mx =max(c, mx)
    print(mx)
    
    
   
            
    
    
    


