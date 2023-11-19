import base64

# Read content from the file
file_path = 'answer.txt'

try:
    with open(file_path, 'r') as file:
        for line in file:
            # Add padding to make the length a multiple of 4
            line = line.strip() + '=' * (4 - len(line.strip()) % 4)
            
            # Decode each line individually
            decoded_line = base64.b64decode(line)
            
            # Print or use the decoded content as needed
            print(decoded_line.decode('utf-8', errors='replace'))
except FileNotFoundError:
S    print(f"File '{file_path}' not found.")
    exit()
