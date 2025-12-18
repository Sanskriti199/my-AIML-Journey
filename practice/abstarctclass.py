from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass #represents null value

class Lion(Animal):
    def make_sound(self):
        print("Roar!!")

class Cow(Animal):
    def make_sound(self):
        print("Moooo!!")

lion=Lion()
cow= Cow()
lion.make_sound()
cow.make_sound()