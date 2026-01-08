# List of numbers
list1 = [9, 6, 3, 25, 21, 8, 23, 1, 17, 14]
list2 = [37,39,41,29,9,25,43,21,3,42]
list3 = [24,8,10,22,45,34,28,39,3,32]
list4 = [15,21,8,32,46,44,37,20,27,22]
list5 = [11,38,4,28,24,41,15,10,45,14]


# for i in range(len(list2)):
#     for i in range(len(list2) - 1):
#         if list2[i] > list2[i + 1]:
#             swap= list2[i + 1]
#             list2[i+1]=list2[i]
#             list2[i]=swap

# print (list2)


n = len(list1)
for i in range(n):
    for j in range(0,n-i-1):
        if list1[j]<list1[j+1]:
            list1[j],list1[j+1]=list1[j+1], list1[j]

print(list1)