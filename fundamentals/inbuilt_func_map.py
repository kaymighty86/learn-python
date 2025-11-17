#just like how javascript has array functions for iteration actions
#python has function that perform similar actions but as inbuilt functions becuase there more many types of data structures in Python so they had to make the functions standalone

#map function (for transforming an array-type object by mutating its values into another state using a function and oututs a new map object with the newly mutated elements which can be casted into any new list/tuple/set)
evenNums = [2,4,6,8,10,12]

def multiplyX2(item):
    return item * 2

evenNumx2 = list(map(multiplyX2,evenNums))

#OR using anonymous functions to do the same thing makes the code even leaner (since we are never going to use that function again, there is no point defining it) (lamda is used to represent anonymous functions)
evenNumx2_new = list(map(lambda item: item * 2, evenNums)) #this will return the same value as the expression above

print(evenNums)
print(f"x2: {evenNumx2}")
print(f"other method x2: {evenNumx2_new}")