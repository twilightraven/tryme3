def new_line():
    print()
    
def three_lines():
    new_line()
    new_line()
    new_line()

# the function nine_lines uses a function called three_lines to print nine blank lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# print placeholder below to print out 9 lines
print ("now printing 9 lines")
three_lines()
three_lines()
three_lines()

# print placeholder below to print out 25 lines
print ("now printing 25 lines")
# the function clear_screen prints out 25 blank lines
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

# last line of the program to call the function to clear_screen
clear_screen()
