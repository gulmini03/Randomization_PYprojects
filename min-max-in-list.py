list = []
Number = int(input("number of elements: "))
for i in range(1, Number + 1):
    value = int(input("enter the value of element %d: " %i))
    list.append(value)
 
smallest = largest = list[0]
 
for j in range(1, Number):
    if(smallest > list[j]):
        smallest = list[j]
        
    if(largest < list[j]):
        largest = list[j]
        
 
print("Smallest: ", smallest)
 
print("Largest: ", largest)

print(min(list))