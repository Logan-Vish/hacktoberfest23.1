# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Handle the case of an empty list to avoid division by zero

    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example list of numbers
number_list = [5, 10, 15, 20, 25]

# Calculate and print the average
average = calculate_average(number_list)
print(f"The average is: {average}")
