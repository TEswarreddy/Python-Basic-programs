n=145
original =n 
sum=0
 
while n>0:
    fact=1
    digit = n%10
    #print(digit)
    while(digit > 0):
        fact *=digit
        digit -=1 
    #print(fact)
    sum +=fact
    n =n//10
print(sum)
if sum==original:
    print("It is a strong number")
else:
    print("It is not a strong number")