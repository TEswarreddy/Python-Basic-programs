n=int(input())
i=2
while(i<n):
    j=2
    count =0
    while(j<=i):
        if i%j==0:
            count +=1
            j+=1
        j +=1    
            
    if count <=1:
        print(i,end=" ")
    i+=1