
# sample program :1

"""print( ''' sample program 1: Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item.function should be able to work with any list value passed to it.''')

spam = []
print( ' enter the list')

while True:
    name = input()
    if name == '':
        break
    else :
        spam = spam + [name]        
print(spam)

length = len(spam)
print('Length of spam = ', length)
for i in range(length):
    if(i != length-1):
       print(spam[i],end = ' ,') 
    else :
        print('and' ,spam[i])"""


# list read and print sample program

"""catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
            ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name) """


#sample program 2 :Picture grid

print('read and print characters from a character picture grid')
print("enter no.of elements in a list : ")
raw = input()
n=int(raw)
print("Enter total number of list :")
column = input()
m = int(column)
spam = []
spam1=[]
for i in range(m):
    print(str(i) + 'th list:')
    for j in range(n):
       name = input()
       spam = spam +[name]
n=int(raw)
m = int(column)
print(spam)

# read all the sublist as a common list. now I have to slice it according
#  no.of elements in a list. but got stuck there. tried to call elements from spam
#  as raw length and stored in another list spam1, but nothing worked
length = len(spam)
if i in range(length):
    for j in range(n):
       for k in range(n):
           spam1[k] = spam[j]
    print(str(i)+'th list :', spam1)
              






