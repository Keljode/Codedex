#print('Hello')
import random

print('==================================')
print(' Rock Paper Scissors Lizard  Spock')
print('==================================')

print('1) ✊ ')
print('2) ✋ ')
print('3) ✌️')
print('4) 🦎 ')
print('5) 🖖 ')
player = int(input('Select a number between 1-5 '))
    
computer = random.randint(1, 5)
if player >=1 and player <=5:
    if player ==1 and computer ==2:
        print('You chose: ✊')
        print('CPU chose: ✋')
        print('The player loses')
    elif player ==2 and computer ==1:
        print('You chose: ✋')
        print('CPU chose: ✊')
        print('The payer won')
    elif player ==1 and computer==3:
        print('You chose: ✊')
        print('CPU chose: ✌️')
        print('The player won')
    elif player==3 and computer==1:
        print('You chose: ✌️')
        print('CPU chose: ✊')
        print('The player lose')
    elif player==2 and computer ==3:
        print('You chose: ✋')
        print('CPU chose: ✌️')
        print('The player lose')
    elif player ==3 and computer==2:
        print('You chose: ✌️')
        print('CPU chose: ✋')
        print('The player won')
    elif(player==1 and computer==4):
        print('You chose: ✊')
        print('CPU chose: 🦎')
        print('The player won')
    elif(player==1 and computer==5):
        print('You chose: ✊')
        print('CPU chose: 🖖')
        print('The player lose')
    elif(player==2 and computer==4):
        print('You chose: ✋')
        print('CPU chose: 🦎')
        print('The player lose')
    elif(player==2 and computer==5):
        print('You chose: ✋')
        print('CPU chose: 🖖')
        print('The player won')
    elif(player==3 and computer==4):
        print('You chose: ✌️')
        print('CPU chose: 🦎')
        print('The player won')
    elif(player==3 and computer==5):
        print('You chose: ✌️')
        print('CPU chose: 🖖')
        print('The player lose')
    elif(player==4 and computer ==5):
        print('You chose: 🦎')
        print('CPU chose: 🖖')
        print('The player won')
        
        
    elif(player==4 and computer==1):
        print('You chose: 🦎')
        print('CPU chose: ✊')
        print('The player lose')
    elif(player==5 and computer==1):
        print('You chose: 🖖')
        print('CPU chose: ✊')
        print('The player win')
    elif(player==4 and computer==2):
        print('You chose: 🦎')
        print('CPU chose: ✋')
        print('The player win')
    elif(player==5 and computer==2):
        print('You chose: 🖖')
        print('CPU chose: ✋')
        print('The player lose')
    elif(player==4 and computer==3):
        print('You chose: 🦎')
        print('CPU chose: ✌️')
        print('The player lose')
    elif(player==5 and computer==3):
        print('You chose: 🖖')
        print('CPU chose: ✌️')
        print('The player win')
    elif(player==5 and computer ==4):
        print('You chose: 🖖')
        print('CPU chose: 🦎')
        print('The player lose')
        
        
        
        
        
        
        
        
    elif player == computer:
        print('It\'s a tie!')
else:
    print('Select a number between 1-5, and retry!')    
    
    
    

