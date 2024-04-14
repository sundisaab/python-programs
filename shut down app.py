from tkinter import*
import os



def restart():#restart the system
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")


def logout():
    os.system("shutdown -1")


def shutdown():
    os.system("shutdown /s /t 1")
   
st=Tk()
st.title("shut down app")
st.geometry("1000x980")
st.config(bg="black")

r_button=Button(st,text="restart",font=("times new roman",28,'bold')
                ,relief=RAISED,cursor="plus",command=restart)
r_button.place(x=385,y=80,height='70',width='200')



r_button=Button(st,text="restart time",font=("times new roman",25,'bold')
                ,relief=RAISED,cursor="plus",command=restart_time)
r_button.place(x=360,y=200,height='70',width='250')


r_button=Button(st,text="log out",font=("times new roman",25,'bold')
                ,relief=RAISED,cursor="plus",command=logout)
r_button.place(x=360,y=330,height='70',width='250')


r_button=Button(st,text="shut down",font=("times new roman",25,'bold')
                ,relief=RAISED,cursor="plus",command=shutdown)
r_button.place(x=360,y=455,height='70',width='250')



st.mainloop()