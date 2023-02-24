from abc import ABC, abstractmethod

class PersonAbstact(ABC):
    name = None
    age = 0
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    @abstractmethod
    def getFull(self):
        pass

class Person(PersonAbstact):
    name = 'Vu Thanh Tai'
    age = 22
    def getFull(self):
        self.getName()
        self.getAge()

Person().getFull();
