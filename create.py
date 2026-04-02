# Name of the file
filename = "example.txt"

# Open the file in write mode ('w')
with open(filename, 'w') as file:
    file.write("Hello, this is a new file created in Python!\n")
    file.write("You can write multiple lines like this.")

print(f"File '{filename}' created successfully.")