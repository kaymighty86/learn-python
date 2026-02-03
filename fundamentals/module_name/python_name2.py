#The Python "__name__" built-in variable stores the name of the main module (by default, the value sotred in __name__ for an executed module is __main__)
#If a module is imported by another, the name of the module changes and is no longer "__main__"

import python_name

print("Hello this is Script 2")

if(__name__ == "__main__"):
    print("This is the main module.")
else: 
    print("This module was imported by another.") #the name is not "__main__" so it must have been imported by another module which might be the main module