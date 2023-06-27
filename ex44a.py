#Implicit Inheritance

class Parent(object):

    def implicit(self):     #Parent class has a function
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()      #calling the function from parent class
son.implicit()      #calling the function from child class, 
                    #although it doesnt exist in child class,
                    #The Child inherits all functions from the parent's class
