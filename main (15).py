#sum of a number until it comes in single digit
n=9875
result=0
#while(n>0):
#    digit = n%10
#    result +=digit 
 #   n //=10
while(n >9):
    
    result=0
    while(n>0):
        digit = n%10
        result +=digit 
        n //=10
    n=result
print(result)