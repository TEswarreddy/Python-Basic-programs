n=int(input())
m=int(input())
i=2
lcm=1
while(n>1 or m>1):
    if(n%i==0 and m%i==0):
        
        m //=i
        n //=i
        #print(f"{m}{n}{i}")
        print(i)
        
    elif((n%i==0 and m%i!=0) or(n%i!=0 and m%i ==0) ):
        if(n%i==0):
            n //=i
            #print(n)
            print(i)
           
        if(m%i==0):
            m //=i
            #print(m)
            print(i)
            
    elif((m%i!=0 and n%i!=0) or n!=1 or m!=1):
        i+=1
        
    
        
