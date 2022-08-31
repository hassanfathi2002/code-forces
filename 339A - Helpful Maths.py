#170367777	Aug/31/2022 11:39UTC+2	hassanfathi2002	339A - Helpful Maths	Python 3	Accepted	92 ms	0 KB
s=input('').split('+')
s.sort()
for i in range(len(s)-1):
    print(s[i]+'+',end='')
print(s[-1])    
