
import time
#from tkinter import Button --use later 
from pywebio.input import input#,NUMBER   --later
from pywebio.output import put_text
from pywebio.exceptions import SessionClosedException
def t():
    time.sleep(5)

def gl():
    L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
    I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    #num1=dict(zip("1234567890",range(10)))
    #num2=dict(zip(range(10),"1234567890"))
    key=input("Enter your key value",type="number")
    inp=input("enter encipher or decipher",type="text")
    if inp=="encipher":
        plaintext = input("Enter your input here:",type="text") 
        ciphertext = ""
        for c in plaintext.upper():
            if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
            else: ciphertext += c
        put_text("your encipher value is:{}".format(ciphertext))
        put_text("wait for some time it will come after 5 seconds")
        t()
        
    elif inp=="decipher":
        encoded_text=input("Enter your input here:",type="text")
        plaintext2 = ""
        for c in encoded_text.upper():
            if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
            else: plaintext2 += c
        put_text("your decoded value:{}".format(plaintext2))
        put_text("wait for some time it will come after 5 seconds")  
        t()  
    elif inp=="":
        put_text("enter input please")

if __name__=="__main__":
    try:
        while True:
            gl()
    except SessionClosedException:
        print("You closed the session")
