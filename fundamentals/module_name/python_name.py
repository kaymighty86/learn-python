#The Python "__name__" built-in variable stores the name of the main module (if a module is executed first it becomes the __main__)
#If a module is not executed first but was imported by another, the name of the module changes and is not "__main__"
#if a module is import by another module, the code of the imported module is executed first

print("Hello this is Script 1")

if(__name__ == "__main__"):
    print("This is the main module.")
else: 
    print("This module was imported by another.") #the name is not "__main__" so it must have been imported by another module which might be the main module