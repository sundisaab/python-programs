import pywhatkit as pwk
 
 
try:
      
     pwk.sendwhatmsg("+91 54***", "hlo", 13,32)
 
     print("Message Sent!")  
 
     
except: 
     print("Error in sending the message")
