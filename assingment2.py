# Take input from the user
number = int(input("Enter an integer: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(number, "is an Even number.")
else:
    print(number, "is an Odd number.")

# Initialize the sum variable
total_sum = 0

# Iterate over numbers from 1 to 50
for number in range(1, 51):
    total_sum += number

# Display the final sum
print("The sum of numbers from 1 to 50 is:", total_sum)
