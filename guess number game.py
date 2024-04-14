import random
 
 
target = random.randint(1,100)

while True :
      user_choice= int(input ("guess a number :"))
    

      if(user_choice==target):
             print("______wow you won_______ ")
             break
      
      elif(user_choice < target):
              print("you enter a small number please guess bigger")

      else:
             print("you enter a big number please guess smaller ")

 
