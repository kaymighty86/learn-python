#Modules are python scripts
#Packages are folders containing modules
#you can import all kinds of things from a module e.g functions, variables, classes, etc

#There are different methods of importing

#--------------------------
#Type 1, import the whole package(s) and module as one module (as shown in the example below, its not very good if the module you want to access is far into multiple sub-directories, a solution is to assign custom name to this import (as shown later on, down the line))
import sample_package.utils #"sample_module" is a package and "utils" is a module

maximum = sample_package.utils.max_num(1,2,34,5,23,33)#when calling an object from the module, you have to write the full reference before calling the object
print(maximum)

#OR
#type 2 (preffered), import the module alone, this allows you have access to any object inside the module and you do not have to write the full reference everytime you want to call the module
from sample_package import utils

maximum1 = utils.max_num(1,2,34,5,23,33)
print(maximum1)

#OR
#type 3 import a particular object from a module. However, you cannot have access to anyother object in the module aside from what you imported (this is similar to how javascript's import is)
from sample_package.utils import max_num

maximum2 = max_num(1,2,34,5,23,33)
print(maximum)

#--------------------------
#ASSIGN CUSTOM NAMES
#--------------------------
#you can assign a custom name to anything imported

# Example 1: assign custom name to imported function.
from sample_package.utils import max_num as myMax

maximum3 = myMax(1,2,34,5,23,33)
print(maximum3)

# Example 2: assign custom name to imported module.
import sample_package.utils as myUtils

maximum4 = myUtils.max_num(1,2,34,5,23,33)
print(maximum4)