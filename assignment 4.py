import os
fh=open("sample", "rt")
line1=fh.readline()
line2=fh.readline()
print("The File Content:")
print(f"line 1 :{line1}")
print(f"line 2 :{line2}")
print("")
if os.path.exists("sample"):
    print("The File Exists")
else:
    print("Erorr: The File Does Not Exist")
fh.close()


# Task 2: Write and Append Data to a File

initial_text = input("Enter text to write to the file: ")


with open("output.txt", "w") as file:
    file.write(initial_text + "\n")
print("Data successfully written to output.txt.")


additional_text = input("Enter additional text to append: ")


with open("output.txt", "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.")

print("Final content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)