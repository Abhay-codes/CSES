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
    
    #n =int(input())
    #n,k =map(int,input().split())
    '''l=[]
    for   i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)'''
    #print(math.gcd(-2,-6))
    #l=list(map(int,input().split()))
    
    #l2=list(map(int,input().split()))
    #print(l)
    #print(n)
    mx =0
    s=input()
    d=defaultdict(int)
    se=set()
    n =len(s)
    i=0 
    j =0 
    prev =s[0]
    c=1
    mx=1
    for i in range(1,n):
        if s[i]==prev:
            c+=1
            mx =max(c,mx)
        else:
            prev =s[i]
            mx=max(c,mx)
            c=1 
    print(mx)
        
    
    
    


