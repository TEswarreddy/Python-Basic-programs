# Enter your code here
n=int(input())
list1=[]
count=0
for x in range(n+1):
    count=0
    while(x>0):
        if(x&1==1):
            count+=1
        x=x>>1
    list1.append(count)
    
print(list1)