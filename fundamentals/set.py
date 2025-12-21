set_var = {2,4,6,8,9,2,6,12} #set is a datatype that ensure only unique elements are saved and eliminates duplicates
print(set_var) #the output will be {2,4,6,8,9,12}

#appending to a set
set_var.add(5) #adds 5 to the end of the set

#extracting all elements from a set into a new one (copying)
new_set = set_var.copy()
print(new_set)

#deleting all elements from a set
new_set.clear()

#Set methods
#performing venn diagram operations with sets
set1 = {4,6,3,3,4,5,7,3,1}
set2 = {0,1,3,7,3,5,2}

print(set1.difference(set2)) #returns elements that are in set1 and not in set2
