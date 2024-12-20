list1=[8,5,9,3,6]
target=11
dicti={}
for i in range(len(list1)):
    x=target-list1[i]
    #print(x)
    if (x in dicti):
        print(f"{i}, {dicti[x]}")
    dicti[list1[i]]=i
    #print(dicti)
    
