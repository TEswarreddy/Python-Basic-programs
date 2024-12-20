#the second largest number
list1=[9,5,6,45,32,15,67,32,12,1,45,8,89]
max_num=max(list1)
s_max=0
for i in list1:
    if(i>s_max and i!=max_num):
        s_max=i 
print(s_max)