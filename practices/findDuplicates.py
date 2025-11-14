ages = ["a", "b", "c", "d","b", "e", "f", "e", "a"]
duplicates = []

#find the duplicate elements
for item in ages:
    #check if the item is a duplicate and it has not already being detected
    if(ages.count(item) > 1) and (item not in duplicates):
        duplicates.append(item)

#show the duplicates
if len(duplicates) > 0:
    print("The duplicate elements are: ", end="")
    for item in duplicates:
        print(item, end=",")
else:
    print("No duplciates found.")