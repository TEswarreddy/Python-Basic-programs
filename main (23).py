#rotate the array by 1
list1=[1,2,3,4,5,6]
n=len(list1)-1
last=list1[-1]
while(n>=1):
    list1[n]=list1[n-1]
    n-=1
    
list1[0]=last
print(list1)
    