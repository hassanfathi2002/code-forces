#170371012	Aug/31/2022 12:18UTC+2	hassanfathi2002	1722A - Spell Check	Python 3	Accepted	31 ms	0 KB
n=int(input())
s=list('Timur')
s.sort()
for i in range(n):
    l=int(input()) 
    s_new=list(input())
    s_new.sort()    
    if s==s_new :
       print ('yes')
    else :
       print('no')
