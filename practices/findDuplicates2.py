#lets redo this problem using comprehension expression now
numbers = [49,5,23,6,11,13,11,8,2,23]

duplicateNums = list(set(item for item in numbers if numbers.count(item) > 1)) #set helps us get rid of the duplicates

print(duplicateNums)