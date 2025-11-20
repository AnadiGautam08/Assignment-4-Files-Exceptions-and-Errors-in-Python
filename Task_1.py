"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist
"""


try:
    with open('sample.txt', 'r') as fh:
        i=1
        for line in fh:
            print(f"Line {i}: {line.rstrip()}")
            i+=1

except FileNotFoundError:
    print("File not found")




