
n=9875
result=9875
#while(n>0):
#    digit = n%10
#    result +=digit 
 #   n //=10
while(result >9):
    n=result
    result=0
    while(n>0):
        digit = n%10
        result +=digit 
        n //=10
print(result)