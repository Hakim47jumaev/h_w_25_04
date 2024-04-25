list=input().split()
k=0
for i in range(1,len(list)+1,2):
    k=list[i]
    list[i]=list[i-1]
    list[i-1]=k
print(' '.join(list))
