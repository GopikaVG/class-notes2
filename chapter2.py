

import random

print('1.Guess a number Game\n')

secretno = random.randint(1,20)
print('''I am thinking of a number. can you guess it?!
      you have 3 chances ''')

for i in range(1,4):
     guess =input()
     if guess == secretno:
        print('you won!!')     
        break
     elif i != 3:
         print('you missed it, Try again')
         continue
     else: 
            print('you lost !! Better luck next time')
print('My secret Number is', str(secretno))       
print('Have a Good day')






        
import sys
    
print('2. The Collatz Sequence')
def collatz(number):
    try:
       print('number=' + number)

       number1= int(number) % 2
       print('number1 :' + str(number1))
       if number1 == 0:
          print('Number is even')
          number2 = int(number) //2 
          print('number2=' + str(number2))
          return number2
          sys.exit()
       elif number1 == 1:
          print('number is odd')
          number2=(int(number)*3)+1
          print('number2=', number2)
          return number2
    except ZeroDivisionError:
       print('not a valid option')            
       
value = '1'   
print('Enter your choice')


while value != '0':
     choice = input()
     choice = str(choice)
     value= collatz(choice)
     if value == 1:
         break
     else:
         continue

print('completed') 



    

