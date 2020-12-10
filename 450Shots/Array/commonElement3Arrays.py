__author__ = "ResearchInMotion"

t=int(input())
for i in range(t):
    n1,n2,n3=map(int,input().split())
    a=set(list(map(int,input().split())))
    b=set(list(map(int,input().split())))
    c=set(list(map(int,input().split())))
    g=a.intersection(b).intersection(c)
    g=list(g)
    g.sort()
    if len(g)==0:
        print(-1)
    else:
        print(*g)
