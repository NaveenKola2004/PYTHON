def sum(l,t):
    for i in range(len(l)):
        for j in range(1,len(l)):
            su=l[i]+l[j]
            com=[i,j]
            if su==t:
                return com
k=int(input())
l=[]
for _ in range(k):
    l.append(int(input()))
t=int(input("Enter the target : "))
print(sum(l,t))