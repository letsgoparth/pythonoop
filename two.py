class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("O don't know what to say")

class cat(pet):
    def speak(self):
        print("meaw")

class dog(pet):
    def speak(self):
        print("woof")
        
p = pet("Tim", 19 )
p.speak()

c = cat("Dug",34)
c.show()