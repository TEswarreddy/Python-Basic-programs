n = int(input())
m=int(input())
res =min(n,m)
print(res)
while True:
    res -=1
    print(res)
    if(n%res==0 and m%res==0):
        print(res)
        break
        
    