"""theboard = { 'top-L':'', 'top-M':'',  'top-R':'',
             'mid-L':'', 'mid-M':'', 'mid-R' : '',
             'low-L':'', 'low-M':'', 'low-R' :''}



def printboard(board):
    print(board['top-L'] + '  |  ' + board['top-M'] + '  |  ' + board['top-R'] )
    print('- +  - +  -')
    print(board['mid-L'] + '  |  ' + board['mid-M'] + '  |  ' + board['mid-R'] )
    print('- +  - +  -')
    print(board['low-L'] + '  |  ' + board['low-M'] + '  |  ' + board['low-R'] )


turn ='x'
for i in range(9):
    printboard(theboard)
    print('Turn for' + turn +'.move on which place?')
    move = input()
    theboard[move] = turn
    if turn == 'x':
        turn = '0'
    else :
        turn = 'x'

printboard(theboard)"""



"""# family outing

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests,item):
    numbrought =0
    for k,v in guests.items():
        numbrought = numbrought + v.get(item,0)
    return numbrought

print('Number of things being brought')
print(' - Apples' + str(totalBrought(allGuests,'apples')))
print(' - Cups' + str(totalBrought(allGuests,'cups')))
print(' - Cakes' + str(totalBrought(allGuests,'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests,'ham sandwiches')))
print(' - Apple Pies' + str(totalBrought(allGuests,'apple pies'))) """




"""# program to display inventory of a player in a game

stuff = {'rope': 12, 'torch' : 13, 'gold coin': 34 , 'dagger': 1 ,'arrow': 13}   

print('rope =' + str(stuff.get('rope', 0)))

           
def displayinventory(inventory):
    print('Inventory :')
    
    for k,v in inventory.items():
        print('item= ' + k +'value= '+ str(v))
        

displayinventory(stuff)"""


"""# list to dictionary function for fantasy game inventory



def addtoinventory(inventory,addeditems):
    for k,v in inventory.items():
        length = len(addeditems)
        print('length=' + str(length)
        if k in addeditems : 
                 m=m+1
                 print('m=' + str(m))
        v = v+m
        print( k + '=' + str(v))
        
inv = {'gold coin:' : 42 , 'rope:' :1}
dragonloot = ['gold coin' , 'dagger', 'gold coin', 'gold coin' , 'ruby']
addtoinventory(inv,dragonloot)"""







              



      
    


