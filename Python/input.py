'''
name=input("Please enter your name > ")
print("hello" ,name)

num=int(input("enter a number > ")) # casting to an int first
print(num)
double=num*2
print(double)
'''
#inputs entered are treated as strings
#can put try catch block at beginning to make sure user inputs correctly
'''
try:
    num=int(input("enter a number > ")) # casting to an int first
    print(num)
    double=num*2
    print(double)
except:
    print("you didn't enter a number")
'''
#could also use a while loop with a boolean to continually prompt for input if given incorrect

#read in file
with open("movies.txt") as file: #file in variable the input is stored
    for line in file:
        line=line.strip() #removes new line after each line
        print(line)

with open("heights.txt") as file:
    for line in file:
        info=line.strip().split() # breaks string apart into a list based on whitespace | info=[blah, blah, blah]
        info[2]=int(info[2])
        print(info)