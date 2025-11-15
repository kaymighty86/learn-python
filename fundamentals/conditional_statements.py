num1 = 34.98
isActive = True
age = 0 #this is a falsy statemnt
isTall = False #this is a falsy statemnt
listEl = [] #this is a falsy statemnt

#if statement with logical operator
if num1 > 5 and num1 <= 50:
    print("More than 5 and less than 50")
elif num1 > 20 or isTall:
    print("This is how OR logical work")
elif num1 == 20:
    print("This is equal comparison")
else:
    print("Have Maria, the last condition to execute if all others fail")

#--- truthy and falsy
if isActive:
    print("User is active.")

if age:#falsy statement. SO there will no execution
    print("There is age value given")

#--- TERNARY operators
isFat = True if num1 > 20 else False

#--- the "is" logical operator. This is used to compare variables stored in the same location in memory (typically when variables have the same value except lists (and all its types), dicts, functions, classes)
num2 = 5
num3 = 5
print(num2 is num3) #this will return True (although you cannot write this in a logical expression of a conditional statement for some reason. Take note of the example below)
# if 5.0 is 5: #this doesn't work
#      print("We are store in the same location in memory")

