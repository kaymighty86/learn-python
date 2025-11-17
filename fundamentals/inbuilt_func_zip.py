#zip function (this joins the elements of multiple list-type data structures together in pairs of tuples inside a zip object which can be casted into a list/tupple/set)
#helpful when merging features of datasets together

usernames = ["jay23", "kay123", "ps23", "hovER"]
id = (123,45,67,78,9,3) #side note, becuase i used upper case in the naming of the variable, I'm telling other developers that this is a constant
names = ("James", "Kayo", "Plastic Man", "Hanuma")

users = list(zip(usernames, id, names))

print(users) #this will return [(jay23, 123, James), (kay123, 45, Kayo), ...and so on]