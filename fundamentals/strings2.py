strVariable = "me me me"

#SLICING
print(strVariable[0]) #this will show "m"
print(strVariable[0:5]) #this will show "me me" because we are starting from index 0 and stoping at the 5th character (the 5th character will not be returned becuase we are stoping there)
print(strVariable[1:]) #this will start showing from index 1 and extend till the end of the string
print(strVariable[:7]) # this will start from the very begining of the array and stop at the 7th cell without returning the 7th value
print(strVariable[0:8:2]) #the extra 2 in this signifies the step. It means we want the character returned to be in steps of 2 i.e. it will return "m em"
print(strVariable[-1]) #show character at the first index at the back

#LENGTH
print(len(strVariable)) #print the length of the string

#STRING METHODS(FUNCTIONS)
strVariable.lower() #returns the string in all lower case
strVariable.upper() #returns the string in all upper case
strVariable.capitalize() #returns the string but the first character is upper case
strVariable.find("me") #returns the index of the first instance of a string in the string
strVariable.replace("me","you")#retuns a string where all the instances of the string given is replaced with the other string provided
strVariable.split(" ")#retuns an array of strings of all character between the seperator
" ".join(["I","am","him"]) #returns "I am him" i.e. returns a string that joins elements of the given array together in one string using the initiator string as the seperator (the reverse of split())

trimmed_string = "   hello i want to play   ".strip() #remove leading and traiing whitespace and return the adjusted string (same as the trim() function in other prog languages)