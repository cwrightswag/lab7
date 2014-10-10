print "Dis da first part"
eN = []
lN = 1
while(lN <=300):
    if lN % 2 ==1:
        eN.append(lN)
    lN = lN +1
print eN 

print "Dis da second part" 

mylist = ["swag" , "yolo", 1 , 2 ,3 , 4 , 5 , 6,  7 , 8 , 9, "lookin fresh"]
position = 0
kL = True
while(position < len(mylist)):
  print mylist[position]
  position = position + 1

print "Dis da third part"
    
import random
rand = random.randint(0,50)
userInput = -1
print "Guess a number between0 and 50"
while(rand != userInput):  
    userInput = int(raw_input())
    if userInput == rand:
        print "You guessed it you win!"
    if userInput >  rand:
        print "Too high!"
    if userInput < rand:
        print "Too low!"
        
