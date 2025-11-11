newList = [23,45,8,3,9,3,8]

a,b,*others,z = [23,3,9,3,8] #desturcturing

#GETTING VALUE 
#--> Slicing
print(newList[2]) #returns 8
print(newList[:3]) #returns array [23,45,8] (just like it works with strings)
print(newList[:]) #returns array with the full elements from the newList array (this can be used to copy elements of an array into a new array)
print(newList[::2]) #returns array [23,8,9,8]. Returns in steps of 2
print(newList[::-1]) #returns new array with the elements fetched in steps of 1 but starts counting from back thereby returning a reversed copy of the array
#--> finding index
print(newList.index(45)) #this returns the index of element with value 45 which is 1
print(newList.index(45,1,4)) #the extra 1,4 params are for telling it where to start searching from and where to stop respectively
print(8 in newList) #this is a boolean expression for confirming if a value exists in a list

#ADDING VALUE
newList.append(23) #this adds 23 to the end of the list
newList.insert(3,90) #adds the new element 90 to index 3 and pushes the rest of the element down the list (NB: Anything can be inserted even another array but it won't spread its values instead will be inserted as one whole array inside the cell)
print(newList)
newList.extend([0,6,32,1]) #spreads the values of the provided array param to the end of the list

#REMOVING VALUE
lastEl = newList.pop() #deletes the last element from the list and returns the value
thirdEl = newList.pop(2) #deletes the element with the given index from the list and returns the value
newList.remove(8) #deletes all instances of the elements that has value 8
print(newList)
newList.clear() #clears the whole array

#OTHER LIST METHODS
newList = [23,45,8,3,9,3,8]

secondList = newList.copy() #returns a copy of the list. (same as just writing newList[:])
newList.count(8) #returns 2 i.e. It counts the number of occurences of the given value 8
newList.sort() #sorts the list in ascending order (the function can be configured to sort in descending order **hover on the function to see details**)
newList.reverse() #reverses the order of the elements of the list i.e. first element becomes last and vice-versa (NB: It doesn't sort) (this is same as writing newList[::-1])

thirdList = list(range(10)) #this creates a list of integers 0 - 9 from the given range object (don't forget range objects can be created with start,stop,step params)
sorted(newList) #an inbuilt function that returns a sorted copy of the given array without mutating the array
