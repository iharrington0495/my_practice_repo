print ("Hello World")
# comments
''' 3 apostrophes
big comment
python version of /*
'''
# highlight code and press ctrl + / and it will autocomment

#variables
x=100
x="hello"
x=[1,2,3]
print(x)
# ^^ will print last assigned variable

#math stuff
x=100
y=10
result = x//y #floor division. chops off decimal
print(result)
print(x/y)
print(int(x/y)) #mod to print as int

min_value = min(1,2,3) #find min
print(min_value) #python naming convention. Use underscore
raised = pow(2,3) # raising to the power of
print(raised)
raised = 2**3 # other way to raise to power of
print(raised)

#If Statements
x = -1
y=0
if x< 0:    #use :
    print("x is negative")
    y+=1        #no ++ operator
elif x>0: #else if
    print("x is positive")
else:
    print("x is zero")

start = 10
end = 100

if x>start and x<end:  # and instead of && or instead of ||
    print("x is within range")

if x<start or x>end:
    print("x is not in range")


#LOOPS
#While Loop
count=0
while count <5:
    print(count)
    count+=1

#For Loop
for i in range(5):
    print(i) # prints vertically

for i in range(5):
    print(i, end=" ") # prints horizontally
print() # needed to move to next line

for i in range(5, 15):
    print(i, end=" ") # start and end range
print()

for i in range(1, 15, 2): # range 1-15 incrementing by 2
    print(i, end=" ") 
print()

lst=[2,4,6,8]
for i in range(len(lst)):
    print(i,lst[1])

for val in lst:
    print(val, end=" ")
print()

for i,val in enumerate(lst): #technically does same thing as line 76/77
    print(i, val)

#default or defining functions
def hello_world():
    print("Hello World!")
hello_world()

def hello(name):
    print("Hello " +name)
hello("Bob")

def hello2(name="Bob"):
    print("Hello " +name)
hello2()
hello2("Jane")

#Strings
hello="hello"
for c in hello:
    print(c)

#negative indexes -> count from right
title = 'python'

#repetition operator -> *

#comparing strings '==' works instead of .equals

#membership operators
#in and not in operators used to check if a substring is in a baseball

#String slicing
course="platform computing"
plat=course[0:8] # can do [:8] to do from 0
print(plat)
comp=course[9:18] #can do [9:] to do from 9 to the end
print(comp)
