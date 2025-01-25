class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def study(self):
        print(f"{self.name} is studying {self.major}")

    def __str__(self):
        return f"Student : {self.name}, major : {self.major}"

# Create the Object
student1 = Student("Alice", "Computer Science")
student2 = Student("Bob", "Mathematics")

# Accessing attributes and calling methods
print(student1.name) # Output : "Alice"
student1.study()     # Output : Alice is studying Computer Science
print(student1)      # Output : Student : Alice, major : Computer Science