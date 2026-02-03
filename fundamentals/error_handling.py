#exceptions can be handled to give a custom error message instead of crashing the process
while True:
    try:
        num = int(input("Input a number"))
    except: #this catches all errors
        print("Make sure you are entering a whole number")
    else: #this executes if there is no exception
        print("Thank you for entering the number.")
        break
    finally: #this executes after the whole try/except/else statements
        print("Anything")

#specific exception types can be targetted
try:
    print(int(input("Enter a number")))
except ValueError: #this only hadles ValueError exception
    print("Bad entry bro")

#eception messages can be gotten
try:
    print(int(input("Enter a number")))
except ValueError as err: #this only hadles ValueError exception
    print("Bad entry bro:" + err.__str__())