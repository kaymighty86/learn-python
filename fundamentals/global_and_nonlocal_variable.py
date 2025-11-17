#the scope system in python is abbit different from other programming languages because of the fact that we do not explicitly declare new variables using a key word (e.g. var or const) 
#hence variable declared in the most local heirarchy superceeds any copy or version that are outside

#GLOBAL VARIABLE
#variabole that exists in the global scope (i.e not declared in a function's local scope or not in a parent function's scope (for functions that hava another function as parent))
counter = 0

def count():
    global counter #to tell python that this variable is from the global scope so that it doesn't see it as a new variable when we use it. And you must declare it first like this before using the variable in an expression
    counter += 1 #this will return an error if its used just like this without the line above
    return counter

while counter < 3:
    print(count())

#NONLOCAL VARIABLE (from Python3 onwards)
#variabole that exists in a parent function's scope (i.e not declared in a function's LOCAL scope or not in the GLOBAL scope)
num = 4
def return2():
    num = 0
    def secondFunc():
        nonlocal num #to tell python that this variable is from the parent scope so that it doesn't see it as a new variable when we use it. And you must declare it first like this before using the variable in an expression
        num += 2
    
    secondFunc()
    return num

#the expressions below will yield different results because of different scopes (wierddness of python and why its quite different from other prog languages)
print(return2()) #this will return 2 because the "num" variable initialised in the return2() function is different from that one in the global scope
print(num) #this will return 4 because the global variable num remains unchanged