#just like how javascript has array functions for iteration actions
#python has function that perform similar actions but as inbuilt functions becuase there more many types of data structures in Python so they had to make the functions standalone

#filter function (for filtering some elements out of an array-type object using a function by running a boolean operation on each item and oututs a new map object of elements where the boolean operation yielded to True which can be casted into any new list/tuple/set)
nums = [1,2,3,4,5,6,7,8,9,0]

def evenNums(item):
    return item % 2 == 0

evenNumx2 = list(filter(evenNums,nums))

#OR using anonymous functions to do the same thing makes the code even leaner (since we are never going to use that function again, there is no point defining it) (lamda is used to represent anonymous functions)
evenNumx2_new = list(filter(lambda item: 
                                item % 2 == 0, nums)) #this will return the same value as the expression above

print(nums)
print(f"even nums: {evenNumx2}")
print(f"other method - even nums: {evenNumx2_new}")