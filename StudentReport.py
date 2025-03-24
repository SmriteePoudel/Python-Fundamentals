class REPORT:
    def __init__(self):
        self.__adno = 0  # Private member for admission number
        self.__name = ""  # Private member for name
        self.__marks = [0.0] * 5  # Private member for marks (list of 5 floats)
        self.__average = 0.0  # Private member for average marks
    
    def __GETAVG(self):  # Private function to calculate average marks
        self.__average = sum(self.__marks) / len(self.__marks)
    
    def READINFO(self):  # Public function to input details
        while True:
            try:
                self.__adno = int(input("Enter 4-digit Admission Number: "))
                if 1000 <= self.__adno <= 9999:
                    break
                else:
                    print("Admission number must be a 4-digit number.")
            except ValueError:
                print("Invalid input. Please enter a valid 4-digit number.")
        
        self.__name = input("Enter Name (Max 20 characters): ")[:20]  # Limit to 20 characters
        
        print("Enter marks for 5 subjects:")
        for i in range(5):
            while True:
                try:
                    self.__marks[i] = float(input(f"Subject {i + 1}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid floating point number.")
        
        self.__GETAVG()  # Calculate the average
    
    def DISPLAYINFO(self):  # Public function to display details
        print("\nSTUDENT REPORT")
        print(f"Admission Number: {self.__adno}")
        print(f"Name: {self.__name}")
        print("Marks: ", self.__marks)
        print(f"Average Marks: {self.__average:.2f}")

# Driver Code
def main():
    student = REPORT()
    student.READINFO()
    student.DISPLAYINFO()

if __name__ == "__main__":
    main()
