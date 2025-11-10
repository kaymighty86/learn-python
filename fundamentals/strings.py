my_name = "Simeon" #string variable

#multiline string
my_message = '''
    This is
    for
    multiline
    string
'''

#you can use single or double quotes in eachother
print("You are 'beautiful'")
#OR
print('You are "beautiful"')

#using escape character \ to allow special characters when they are absolutly needed
print("Your dog's mother said \"It is a cutie\"")

#CONCATENATION
my_name = "Simeon"
my_number = 86

print("Hi" + my_name + "nice to meet you")

#concatenation using string formating
print(f"Hi {my_name}, your number is {my_number}!")#MUST start with letter f before the string double quotes
#OR (old python2 and before)
print("Hi {}, your number is {}!".format(my_name, my_number))
#OR
print("Hi {0}, your number is {1}!".format(my_name, my_number))