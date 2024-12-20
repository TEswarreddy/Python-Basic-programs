# Enter your code here
#n=int(input())
n=153
original =n
result=0
while(n>0):
    digit = n%10
    result +=digit **3
    n //=10
if(original == result):
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")