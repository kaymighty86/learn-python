rg = range(10) #returns a range object that produces a sequence of integers from 0 - 9
rg = range(1,10) #you can specify the start number. So will produce range object of 1 - 9
rg = range(1,10,2) #you can specify the steps. So will produce range object of 1 - 9 in steps of 2 i.e. 1,3,5,7,9


print(rg) #this will just return the object structure not the values as a range object just provides an iterable object 
#though you can get the values through a for loop 
#or using it to create a list like below
newList = list(rg) #this creates list with the range values of the range object