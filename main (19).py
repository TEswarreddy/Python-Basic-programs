#check if a number is square of 2
#n=16
# count=0
# while(n>0):
#     if(n&1 == 1):
#         count +=1
#     n =n>>1 
# if count ==1:
#     print("It is a square of 2")
# else:
#     print("It is not")
n=15
if( n &(n-1)==0):
    print("It is a square of 2")
else:
    print("It is not a square of 2")