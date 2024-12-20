n = int(input())
m=int(input())
lcm=False
res=max(n,m)
print(res)
while(not lcm):
    res+=1
    if(res%n==0 and res%m==0):
        print(res)
        lcm = True
        break
    