from itertools import combinations
strin,num=map(int,input().split())
n=len(str(strin))
g=list(combinations(str(strin),n-num))
g=(sorted(g))
t="".join(g[0])
print(t)
