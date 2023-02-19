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
    n,x =map(int,input().split())
    '''l=[]
    for   i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)'''
    #print(math.gcd(-2,-6))
    l=list(map(int,input().split()))
    
    #l2=list(map(int,input().split()))
    #print(l)
    #print(n)
    l.sort()
    i=0 
    j =n-1
    ans =0
    while(i<=j):
        if i==j:
            ans+=1 
            break 
        sm =l[i]+l[j]
        if sm <=x:
            ans+=1 
            i+=1 
            j-=1 
        else:
            ans+=1 
            j-=1 
    print(ans)