s="madam"
t="madat"
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
        
for j in t:
    if j in freq:
        freq[j]-=1
    else:
        print("not an anar")
c=0
for x in freq.values():
    if x==0:
        c+=1
if  c==len(freq):
    print("Anagram")