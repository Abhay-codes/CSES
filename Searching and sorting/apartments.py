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
    n,m,k =map(int,input().split())
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
    l2.sort()
    i=0 
    j=0
    ans =0
    while(i<n and j<m):
        val1=l[i]
        val2=l2[j]
        if val1-k<=val2<=val1+k:
            ans+=1 
            i+=1 
            j+=1 
        elif val2<val1-k:
            j+=1 
        elif val2>val1+k:
            i+=1 
    print(ans)
    
    
    
    


