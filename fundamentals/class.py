class Person:
    def __init__(self, name, age): #attributes go here and must always start with "self" which points to the class object itself similar to the "this" keyword in other languages
        self.name = name #initialising the attribute within the class
        self.age = age
    
    response = "nice to meet you"

    def call(self):
        print(f"Hi!, my name is {self.name}, {self.age} years old. {self.response}")

#create a person object from the instance of the 'Person' class
first_person = Person("Matthew", 34)
first_person.call()

#values of object's attributes and variables can be changed
first_person.age = 52
first_person.response = "NOT pleased!"
first_person.call()

# an attribute can be deleted entirely from an object (Note: you cannot delete a variable in a class. e.g. the 'response' variable in the class cannot be deleted)
del first_person.name #delete an attribute
# first_person.call() #this will throw an error

#---------------------------------------------------------------
#INHERITANCE
#class can inherit attributes and behaviours from another class
class Lawyer(Person):
    def getQuestion(self):
        print(f"I'm {self.name}. Anything for a lawyer?")

# create instance
prof = Lawyer("Julie", 49) #you are able to set the name and age becasue the class inherits from the person class
prof.call() #the Lawyer calss inherited this function too
prof.getQuestion()

#A child class can have its own __init__() function
class Trader(Person):
    def __init__(self, name, age, trade):
        super().__init__(name, age)
        self.trade = trade
    def getQuestion(self):
        print(f"I'm {self.name}. I trade in {self.trade}")

trader_1 = Trader("Johnny", 61, "Fishery")
trader_1.getQuestion()


#---------------------------------------------------------------
#ENCAPSULATION
#this is a method for restricting access to variables and methods (making them private)
class Car:
    def __init__(self, color, engine):
        self.__color = color #to make a class attribute private add "__" (double underscore) before the name
        self.__engine_type = engine
    
    def set_color(self, color):
        self.__color = color
        print(f"Color has been changed to {self.__color}")

    def __add_up(): #private function created by using the same double underscore before the name
        print("this method cannot be accessed from outside this class")

nissan = Car("Grey", "V4")
nissan.set_color("Blue")


#---------------------------------------------------------------
#ABSTRACTION
#abstract classes are objects created with at least 1 abstract method
#abstract methods are methods created without any funtionality definitions, these functionalities can then be defined by subclasses (they are more or less like blueprints)
from abc import ABC, abstractmethod #import the modules for enabling abstraction (ABC mean Abstract Base Class which serves as the base class for the abstract class)

class Model(ABC): #abstract classes cannot be instantiated so no need for init function
    @abstractmethod
    def set_name(self):
        pass
    @abstractmethod
    def set_type(self):
        pass

class Product(Model): #this class also becomes an abstract subclass hence it cannot just be instantiated without defining the method from the abstract class
    def __init__(self, name, type):
        self.__name = name
        self.__type = type
    
    def set_name(self, new_name):
        self.__name = new_name
        print(f"The name of the bag is now '{self.__name}'")
    
    def set_type(self, new_type):
        self.__type = new_type
        print(f"The type of the bag is now '{self.__type}'")

bag = Product("Eagle Bag", "Backpack")
bag.set_name("Reddd Bag")
bag.set_type("Holdall")