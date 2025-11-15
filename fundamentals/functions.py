def sumNums(a, b):
    return a + b

print(f"The sum of 56 and 23 is {sumNums(56,23)}")

#the arguments can be inputed in any order if you specify the variable name
def difference(a,b):
    return a - b

print(f"The differecne between 56 and 23 is {difference(b = 23, a = 56)}")

#defining default value of function parameter
def saySomething(message = "Nothing"):
    print(f"You said \"{message}\"")

saySomething("I am working on myself")

#You can define the docstring of the function (definition or description given to functions), whih text editors show when you hover the mouse on the function
def expNum(num, pow):
    '''
    Returns the exponent value of the given number raised to the given power
    '''
    return num ** pow

help(expNum) #this help() function helps print the details of a function and its docstring (providing description just like we have given)

#functions with DYNAMIC/UNFIXED PARAMETERS
def sumMore(*args, **kwargs): #args and kwargs can be any name though, the important characters are the asterisks "*" (1 for unfixed args, 2 for key word arguments or arguments that the user will type in the name of the variable)
    '''
    THe order of creating functions with dynamic/unfixed params: funcName(normal param, *args, default param, **keyword args)
    '''
    print(args) #all the passed arguments when this function was called will be collected into a tuple hence this statement will output a tuple carrying the passed values
    print(kwargs) #this will output a dictionary carrying the passed variable name and their value as keys - value pairs
    
    return sum(args)

print(sumMore(4,65,2, name = "jamie", age = 45))