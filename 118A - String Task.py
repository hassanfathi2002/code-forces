#170367392	Aug/31/2022 11:33UTC+2	hassanfathi2002	118A - String Task	Python 3	Accepted	92 ms	0 KB
s=input().lower()
s_new=''
vowels=list('aouyie')
for letter in s :
    if letter not in vowels :
        s_new+=f'.{letter}'
print(s_new)
