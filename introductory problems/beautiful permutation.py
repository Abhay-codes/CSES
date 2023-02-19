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
    if n==1:
        print(1)
    elif n<4:
        print("NO SOLUTION")
    else:
        for i in range(2,n+1,2):
            print(i,end=" ")
        for i in range(1,n+1,2):
            print(i,end=" ")
        
        
    
    
    


