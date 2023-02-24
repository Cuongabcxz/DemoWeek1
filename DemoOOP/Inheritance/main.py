class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def info(self):
    print(self.name + ",", self.age, "years old.")

# Student inherits from Person
# without add any other properties or methods
class Student(Person):
  pass

# create an object of Student class
kane = Student("Kane", 29)
kane.info ()
