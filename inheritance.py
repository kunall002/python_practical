class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

dog = Dog("kalu", "Golden Retriever")
print(f"{dog.name} is a {dog.breed} and says {dog.speak()}")
