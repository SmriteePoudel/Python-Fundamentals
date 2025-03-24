# Define a custom exception class
class Negative(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

# Function to check for negative numbers
def check_positive_number():
    try:
        num = int(input("Enter a number: "))  
        if num < 0:
            raise Negative  
        print(f"Valid input: {num}")
    except Negative as e:
        print(f"Exception: {e}")


check_positive_number()
