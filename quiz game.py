import random

def qiz_1():
    
  print("_-_-_-_-_-_-_- welcome to my quiz game _-_-_-_-_-_-  \n")


user=input("if you want to play please type yes  :")
if user == "yes":

    print("what is the full form  of cpu")
    user_1=input("answer ::  ")
           

if user_1==("central processing unit"):
         print("correct answer ")
else:
       print("wrong answer \n")
 
   
  

    
user_2= (input("if you want to see the next question please type yes :"))

if user_2== "yes":
             
     user_2=input(" what is the full form of RAM :")
     if user_2=="random access memory":
           print("correct answer\n")
            
     else:
           print("wrong answer \n")
      
          
          
     user_3=input("if you want to continue please type yes :\n")

if user_3== "yes":
          user_3=input("what is the full form of ROM  :\n")

else:
         print("thankyou for playing")

if user_3=="read only memory":
           print("correct answer")
           
else:
         print("wrong answer ")
       

print("_-_-_-_-_-_-_- going well letss continue _-_-_-_-_-_-_-\n")

user_4= input(" How is the resolution of the screen shown?[in pixels / in dots]")
if user_4 =="in pixels":
         print("correct answer")
         print("_-_-_-_-_-_-_-_  GAME OVER  _-_-_-_-_-_-_-_")
else:
         print("wrong answer ")

    
         
            

def again():

    
    qiz_again = input('''
if you want to play from starting please type [ y / n ]
''')

     
    if qiz_again == 'y':
        qiz_1()
    elif qiz_again == 'n':
        print('thankyou.')
    else:
        again()

 
qiz_1()

 
again()

