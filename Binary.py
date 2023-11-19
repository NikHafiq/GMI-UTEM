def generate_binary_combinations():
    possibilities = []
    
    for i in range(128):  # ASCII range for one character (0 to 127)
        for j in range(128):  # ASCII range for the second character (0 to 127)
            # Convert ASCII values to binary and concatenate them
            binary_i = format(i, '08b')
            binary_j = format(j, '08b')
            binary_combination = binary_i + binary_j
            
            # Check if the length is 16
            if len(binary_combination) == 16:
                possibilities.append(binary_combination)
    
    return possibilities

# Get all possibilities
all_possibilities = generate_binary_combinations()

# Print all possibilities without spaces
for possibility in all_possibilities:
    print(possibility)
