#Lists
cart=["apples","bananas","cherries"]
print(cart)

#add items to list
cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

#remove items from list
#removes only one iteration of the item from the list
cart.remove("cherries")
print(cart)

#remove item not in list -> errors out
'''cart.remove("pineapple")'''
#add qualifier if not sure in list
if "pineapple" in cart:
    cart.remove("pineapple")

#remove items at index place
cart.pop(3)
print(cart)

#list functions as a list and a stack
cart.pop()
print(cart)

#organize list
cart.reverse()
print(cart)
cart.sort() #natural sorting order ie, alphabetic etc
print(cart)

#adding more items
cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

#slicing a list
#cart[start.index:end.index]
fruit_basket=cart[3:] #does not remove from cart, just copies to new list
print(cart)
print(fruit_basket)

#declare a list
squares=[]
#list 1-10, square numbers, add to squares list
for i in range(1,10):
    squares.append(i*i)
print(squares)

#list comprehensions
#simpler way to do above
squared = [x*x for x in range(1,10)]
print(squared)

values=[34,27,95,18,36,21,64,50,77]
even_values = [x for x in values if x%2 ==0] # only adds even numbers
print(even_values)

# iterates through cart and checks if item starts with b and adds to list if it does
b_items=[item for item in cart if item.startswith("b")] 
print(b_items)

#create list with default value and multiply to get length you want
inventory=[0]*len(cart)
print(inventory)
inventory[0]=100

#sets
number_set=set() #creates empty set
number_set={1,1,2,3,4,0,10,5} #literal notation | cant have duplicates, auto orders when printed
print(number_set)
number_set.add(-10)
print(number_set)

num_lst=[1,1,4,5,5,6,6]
no_dups = set(num_lst) # convert list to set to remove dupes
print(no_dups)
no_dups=list(no_dups) #convert set back to list
print(no_dups)

ns=sorted(number_set) #resorts list after adding items
print(ns)

#dictionaries
#look up values, count occurences, store records 
fav_snacks={}
fav_snacks={
    "kathleen":"tortilla chips",
    "maggie":"pretzels",
    "emily":"buffalo chicken dip",
    "ava":"chocolate"
}
print(fav_snacks)
fav_snacks["wade"]="popcorn"
print(fav_snacks)

print("kathleen's favorite snack is "+fav_snacks["kathleen"])
'''print("kathleen's favorite snack is "+fav_snacks["bob"])''' # errors out because no bob in dictionary
if "bob" in fav_snacks:
    print("kathleen's favorite snack is "+fav_snacks["bob"])

#iterate through dictionary printing out each one
for key in fav_snacks: 
    print(key+"'s favorite food is " +fav_snacks[key])
    print(f"{key}'s favorite food is {fav_snacks[key]}") # same as above but without using '+' and to allow variables in print

for key,value in fav_snacks.items(): # other way to print out key/value
    print(key,value)

keys=fav_snacks.keys()
values=fav_snacks.values()

fav_snacks["alice"]=["chips","nuts"] 
print(fav_snacks)
# key cannot be a list but value can be almost everything
#key cannot be duplicate but value can