class Basic_Info:
    def __init__(self):
        self.name = ""
        self.rollno = ""
        self.gender = ""
    
    def getdata(self):
        self.name = input("Enter Name: ")
        self.rollno = input("Enter Roll Number: ")
        self.gender = input("Enter Gender: ")
    
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.rollno)
        print("Gender:", self.gender)

class Physical_Fit(Basic_Info):
    def __init__(self):
        super().__init__()
        self.height = 0.0
        self.weight = 0.0
    
    def getdata(self):
        super().getdata()
        self.height = float(input("Enter Height (in cm): "))
        self.weight = float(input("Enter Weight (in kg): "))
    
    def display(self):
        super().display()
        print("Height:", self.height, "cm")
        print("Weight:", self.weight, "kg")


person = Physical_Fit()
person.getdata()
print("\nDisplaying Information:")
person.display()
