#COMPREHENSION: this is a quick method of creating a list-type data structure by copying and transforming elements from an existing list (and even filtering the elements)
#NOTE!!! this can be applied to not ony lists but tuples, dictionaries

numbers = [334,51,5,14,12,55,6,1,20,43,1,8,9,3,59,21,42]
copyNums = [num for num in numbers] #we are basically copying to the new array

NumsPow2 = [num**2 for num in numbers] #we are basically mapping transformed values to the new array

bigNums = [num for num in numbers if num > 20] #condition can be attached to filter out elements we want

print(numbers)
print(f"The copy: {copyNums}")
print(f"To the power of 2: {NumsPow2}")
print(f"Filter numbers bigger than 20: {bigNums}")