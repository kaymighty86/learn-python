#the scope system in python is abbit different from other programming languages because of the fact that we do not explicitly declare new variables using a key word (e.g. var or const) 
#hence variable declared in the most local heirarchy superceeds any copy or version that are outside
counter = 0

def count():
    global counter
    counter += 1#this will return an error just like this
    return counter

print(count())