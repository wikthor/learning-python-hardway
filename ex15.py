from sys import argv #This imports argv

script, filename = argv #Lets argv use filename with the program

txt = open(filename) #asks TXT to open the filename set in parameter

print(f"Here's your file {filename}:") #Intro to listing the file, with filename from command line
print(txt.read()) #This lists the whole filename.

print("Type the filename again:") #Prompts user to type the filename again.
file_again = input("> ") #This is where user enters filename again, and python saves it as the variable.

txt_again = open(file_again) #This is second time file opens.

print(txt_again.read()) #This is second time file reads.
