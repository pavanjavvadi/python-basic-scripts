#this program is used to find the selection sort of a list

a =[12,23,43,8,56,67]
length = len(a)
i = 0
while i<length:
    smallest = min(a[i:])
    index_of_smallest = a.index(smallest)
    a[i],a[index_of_smallest]=a[index_of_smallest],a[i]
    i = i + 1
print(a)   