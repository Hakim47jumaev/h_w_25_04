list1=input().split()
list2=input().split()
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if list1[i]==list2[j]:
            print(list1[i],end=' ')

 