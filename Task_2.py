


text1= input("Enter text to write to the file : ")
file = "output.txt"

try:
    with open(file,'x') as fh:
        fh.write(text1)

except FileExistsError:
    with open(file,'w') as fh:
        fh.write(text1)
finally:
    print(f"Data successfully written to {fh.name}\n")


text2 = input("Enter additional text to append: ")
with open(file,'a') as fh:
    fh.write("\n"+text2)
    print("Data successfully appended.\n")

with open(file,'r') as fh:
    print(f"The final content of {fh.name}:")
    print(fh.read())


