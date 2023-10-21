# Read data from a file
with open('input.txt', 'r') as file:
    data = file.read()

# Modify the data (e.g., convert to uppercase)
data = data.upper()

# Write the modified data to another file
with open('output.txt', 'w') as file:
    file.write(data)
