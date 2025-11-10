num1 = 23
num2 = -19

absoluteNum = abs(num2) #this will return 19 (absolute form of -19)
roundedNum = round(12.345) #returns 12
sqrOfNum = pow(num1,2) #python default power function (even though there is another in the Math module)
binOfNum = bin(5) #returns the binary of the number in a string with 0b preceeding it to let python know that its a binary number. e.g. this function should return 0b101 (101 being the binary form of 5)

#casting binary to integer
bin2Int = int(binOfNum, 2) #the normal int cast function supports specifying the base of the number to let it know how it will convert it, since the binary number is base 2, we're putting 2 as the base