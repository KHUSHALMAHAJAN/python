# Writing to the file
with open('sec.text', 'w') as file:
    file.write("This is the first line in the file sec.\n")
    file.write("This is the second line in the file.\n")

print("File 'sec.text' created successfully.")

# Reading from the file
with open('sec.text', 'r') as file:
    content = file.read()
    print("File content:")
    print(content)
os.remove()
