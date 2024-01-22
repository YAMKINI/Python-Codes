"""# Input three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate sum, average, product
sum_numbers = num1 + num2 + num3
average = sum_numbers / 3
product = num1 * num2 * num3

# Find the smallest and largest numbers
smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

# Print the results
print(f"Sum: {sum_numbers}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")"""

#NO 2
"""# Input the radius of the circle
radius = int(input("Enter the radius of the circle: "))

# Constants
pi = 3.14159

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius**2

# Print the results
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference}")
print(f"Area: {area}")"""

#No 3
"""def print_box():
    for i in range(5):
        print('*' * 5)

def print_oval():
    for i in range(5):
        print('  *  ')

def print_arrow():
    for i in range(5):
        spaces = ' ' * i
        stars = '*' * (5 - i)
        print(spaces + stars)

def print_diamond():
    for i in range(1, 6):
        spaces = ' ' * (5 - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

# Displaying shapes
print("Box:")
print_box()

print("\nOval:")
print_oval()

print("\nArrow:")
print_arrow()

print("\nDiamond:")
print_diamond()"""

#No4
"""f=str("  *  " + "     ")
s=str("     " + "  *  ")
n=0
while(n<4) :
  n=n+1
  print(f*8)
  print(s*8)"""
   
 

"""# Input a five-digit integer
num = int(input("Enter a five-digit integer: "))

# Separate the digits using integer division and modulus
digit1 = num // 10000
digit2 = (num % 10000) // 1000
digit3 = (num % 1000) // 100
digit4 = (num % 100) // 10
digit5 = num % 10

# Print the separated digits with three spaces between each
print(f"{digit1}   {digit2}   {digit3}   {digit4}   {digit5}")"""
""" # Print table header
print("Integer\tSquare\tCube")
# Calculate and print squares and cubes for integers 0 to 10
for i in range(11):
    square = i ** 2
    cube = i ** 3
    print(f"{i}\t{squared}\t{cube}")"""
    
    
"""# Input information
total_miles = float(input("Enter total miles driven per day: "))
cost_per_gallon = float(input("Enter cost per gallon of gasoline: "))
parking_fees = float(input("Enter parking fees per day: "))
average_miles_per_gallon = float(input("Enter average miles per gallon: "))
tolls_per_day = float(input("Enter tolls per day: "))

# Calculate cost per day
gallons_used_per_day = total_miles / average_miles_per_gallon
cost_per_day = (gallons_used_per_day * cost_per_gallon) + parking_fees + tolls_per_day

# Display the result
print(f"\nYour cost per day of driving to work is: ${cost_per_day:.2f}")"""

"""def convert_kilometers_to_miles(kilometers):
    miles = kilometers*0.6214
    return miles
# Example usage
kilometers = float(input("Enter distance in kilometers: "))
miles = convert_kilometers_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles:.2f} miles)"""