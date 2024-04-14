import tkinter as tk    #importing tkinter
from PIL import Image, ImageTk   #importing pillow
import random     #importing random


window =tk.Tk()
window.geometry("1000x1000")
window.title("dice roll")



dice =["dice1.jpg","dice2.jpg","dice3.jpg","dice4.jpg","dice5.jpg","dice6.jpg"]#list of dice images

image1= ImageTk.PhotoImage(Image.open(random.choice(dice)))#randomly choose one image from the list of the dice images
image2= ImageTk.PhotoImage(Image.open(random.choice(dice)))
 


label1=tk.Label(window,image=image1)#create a label to display the images
label2=tk.Label(window,image=image2)
 


label1.image =image1#keep a refrence of the image
label2.image =image2
 

label1.place(x=10,y=20) #placing the images on the screen
label2.place(x=700,y=20)
 

#function to roll the dice
def roll_dice():
        image1 =ImageTk.PhotoImage(Image.open(random.choice(dice)))
        label1.configure(image=image1)
        label1.image=image1


        image2 =ImageTk.PhotoImage(Image.open(random.choice(dice)))
        label2.configure(image=image2)
        label2.image=image2

         


button = tk.Button(window,text="Roll",bg="red",foreground="black",font="times 20 bold",command=roll_dice)

button.place(x=550,y=5,height=40,width=200)#placing the button on the scren



window.mainloop()