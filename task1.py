list1=input().split()
n=int(input())
edit_list=[]
for j in range(1,n+1):
    for i in range(0,len(list1)):
        new_list=[list1[i],str(j)]
        res=''.join(new_list)
        edit_list+=[res]
print(edit_list) 


# my_list = input().split()
# n = int(input())
# result=[]
# for i in range(1, n+1):
#     for j in my_list:      
#         result.append(f'{j}{i}')
        
# print((result))