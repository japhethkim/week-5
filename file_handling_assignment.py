# Define the filename
filename = "my_file.txt"

# File Creation
try:
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write three lines of text to the file
        file.write("This is the first line.\n")
        file.write("Here is the second line with a number: 123.\n")
        file.write("And this is the third line.\n")
    print("File created and initial content written successfully.")
except (PermissionError, IOError) as e:
    print(f"Error creating or writing to the file: {e}")

# File Reading and Display
try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read and print the content of the file
        content = file.read()
        print("\nContent of the file after initial write:")
        print(content)
except (FileNotFoundError, IOError) as e:
    print(f"Error reading the file: {e}")

# File Appending
try:
    # Open the file in append mode
    with open(filename, 'a') as file:
        # Append three additional lines of text
        file.write("Appending the fourth line.\n")
        file.write("Adding the fifth line with more text.\n")
        file.write("Finally, this is the sixth line.\n")
    print("Additional content appended successfully.")
except (PermissionError, IOError) as e:
    print(f"Error appending to the file: {e}")

# File Reading and Display (again to show appended content)
try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read and print the content of the file
        content = file.read()
        print("\nContent of the file after appending:")
        print(content)
except (FileNotFoundError, IOError) as e:
    print(f"Error reading the file: {e}") 