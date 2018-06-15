print('''*** 1 .code that prints Hello if 1 is stored in spam , prints Howdy if 2 is \n
stored in spam , and prints Greetings! if anything else is stored in spam. *** \n''')

import sys
print('Enter your choice')
spam=input()
if spam == '1':
       print('Hello')
    
elif spam =='2':
       print('howdy')
            
else :
    print('Greetings') 




 print('''2. program that prints the numbers 1 to 10 using a for loop.
Then write an equivalent program that prints the numbers 1 to 10 using
a while loop.\n''')

print('numbers are ')
for i in range(1,11):
    print(i)

print('\nusing while loop')
i=0
while i< 10:
     i+=1
     print(i)  
     
    
