"""
1.Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it. Remember to close your file.
"""
FILENAME = "name.txt"
name = input("Enter name: ")
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()
NUMBER_FILE = 'numbers.txt'

"""
2.(In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
"""
FILENAME = "name.txt"
name = input("Enter name: ")
print(name, file=out_file)
out_file.close()

"""
3.Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it: 17 42 400
Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.
"""
total = 0
FILENAME = "numbers.txt"
in_file = open(FILENAME)
for i in range(0, 2):
    number = in_file.readline()
    total = total + int(number)
print(total)
in_file.close()

"""
4.Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.
"""
total = 0
FILENAME = "numbers.txt"
in_file = open(FILENAME)
numbers = in_file.readlines()
for number in numbers:
    total += int(number)
print(total)
in_file.close()