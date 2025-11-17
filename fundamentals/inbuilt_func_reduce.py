from functools import reduce #we have to import this as its not globally available as an inbuilt class like map, zip, filter

#reduce function (this returns the reduced value of all the items in the given array (e.g. adding everything up using the reducer function) starting with an initial value given)

nums = [1,2,3,4,5,6,7,8,9]

def reducer(acc, item):
    return acc + item

sumOfNums = reduce(reducer, nums, 0) #this will return the sum of all the numbers as we have programmed it to

print(sumOfNums)

#OR

#using anonymous reducer function instead of a defined one
sumOfNums_new = reduce(lambda acc, item: 
                            acc + item, nums, 0)

print(f"Other moethod's result: {sumOfNums_new}")