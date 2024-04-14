import random
import string 

pass_len=15


charvalue= string.ascii_letters + string.ascii_lowercase + string.digits    
password=''

for i in range (pass_len):
     
     password+= random.choice(charvalue)
     

     print(password)