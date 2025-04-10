'''
#Loops
#ex 1
for i in range(1,21):
    if i%3==0:
        print(i, end=" ")
print()

#ex 2
count = 1
sum=0
while count <=50:
    if count %2==0:
        sum+=count
    count+=1
print(sum)

#ex 3
numbers=[5,8,2,15,10,3,7]
for num in numbers:
    if num>5:
        print(num,end=" ")
print()

#Challenge
lst=[1,2,3,4,5]
lst2=[]
lst2.append(lst[0])
#for i in range(1, len(lst))
    #lst2.append(lst2[1-1])
#^^^ran out of time

#FUNCTIONS
#ex1
lst=[0,3,8,4,5]
def swap(list):
    x = list[0]
    list[0]=list[len(list)-1]
    list[len(list)-1]=x

swap(lst)

print(lst)
'''

#input
#prompt for a file name and print each line of that file with the line number
name=input("Please enter a file > ")
with open(name) as file:
    count=1
    for line in file:
        print(str(count) + '. ' +line.strip())
        count+=1
