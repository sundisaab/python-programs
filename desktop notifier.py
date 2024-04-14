from plyer import notification

import time


if __name__ == '__main__':
       while True: # using loop for infinite time 
         notification.notify(
            title="***take rest***",
             message="you have working for 2 hours take a small break otherwise you will get sick",
             timeout=4) #only 4 seconds display the notification
         time.sleep(6) #set time according to you get notifiy 

