username = input("Enter your Username:\n")
password = input("Enter your password:\n")

passwordLength = len(password)

print(f"Hi {username}, your password \"{'*' * passwordLength}\" is {passwordLength} characters in length :)")