from tkinter import *
from tkinter import messagebox
#import mysql.connector
import numpy as np
import random
#import collections

# Define a dictionary to map each number to a corresponding character, symbol, or special character
encrypt_dict = {-50: '~',-49: '`',-48: '!',-47: '@',-46: '#',-45: '$',-44: '%',-43: '^',-42: '&',-41: '*',-40: '(',
    -39: ')',-38: '-',-37: '_',-36: '+',-35: '=',-34: '{',-33: '}',-32: '[',-31: ']',-30: ':',-29: ';',-28: '"',-27: "'",
    -26: '<',-25: '>',-24: ',',-23: '.',-22: '?',-21: '/',-20: '|',-19: '\\',-18: 'a',-17: 'b',-16: 'c',-15: 'd',
    -14: 'e',-13: 'f',-12: 'g',-11: 'h',-10: 'i',-9: 'j',-8: 'k',-7: 'l',-6: 'm',-5: 'n',-4: 'o',-3: 'p',-2: 'q',
    -1: 'r',0: 's',1: 't',2: 'u',3: 'v',4: 'w',5: 'x',6: 'y',7: 'z',8: 'A',9: 'B',10: 'C',11: 'D',12: 'E',13: 'F',
    14: 'G',15: 'H',16: 'I',17: 'J',18: 'K',19: 'L',20: 'M',21: 'N',22: 'O',23: 'P',24: 'Q',25: 'R',26: 'S',27: 'T',
    28: 'U',29: 'V',30: 'W',31: 'X',32: 'Y',33: 'Z',34: '0',35: '1',36: '2',37: '3',38: '4',39: '5',40: '6',
    41: '7',42: '8',43: '9',44: '_',45: '-',46: '.',47: ',',48: '/',49: '?',50: '|'}

def encrypt_word(word):
    encrypted_string = ''
    for number in word:
        encrypted_string += encrypt_dict[int(number)]
    return encrypted_string


# Define a function to decrypt a string of characters, symbols, and special characters to a word (list of numbers)
def decrypt_string(encrypted_string):
    decrypted_word = []
    for char in encrypted_string:
        for key, value in encrypt_dict.items():
            if char == value:
                decrypted_word.append(str(key))
    return decrypted_word


#AL = Alphabets
AL = {'A':-1,'B':-2,'C':-3,'D':-4,'E':-5,'F':-6,'G':-7,'H':-8,'I':-9,
'J':-10,'K':-11,'L':-12,'M':-13,'N':13,'O':12,'P':11,'Q':10,
'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}

key_list=list(AL.keys())
val_list=list(AL.values())
def circulant(message):
    e=[]

    for i in message:
        n=len(i)   
        arr=[]
        for j in range(n):
            arr.append(AL[i[j]])
        c = []
        for j in range(n):
            row=[]
            for k in range(n):
                row.append(arr[(j+k)%n])
            c.append(row)  
        if(n%2==0):
            L = int((n/2)-1)
        else:
            L = int(((n+1)/2)-1)
    
        A1 = []
        for j in range(n):
            A1.append(c[j][L])
    
        D1 = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            D1[i][i] = A1[i]

        #EN = ENCRYPT
        EN = D1 - n*(np.identity(n,dtype=int))
    
        EN_KEY = []
        for i in range(len(EN)):
            EN_KEY.append(EN[i][i])

        e.append(EN_KEY)

    return e


#creating a database
'''mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Harish1234",
  database="worksheet1"
)

c=mydb.cursor()
c.execute("DROP TABLE encrypt")
c.execute("CREATE TABLE IF NOT EXISTS `encrypt` (sentence varchar(255) , PASSWORD varchar(255));")
c.execute("DESC encrypt")
mydb.close()'''

def decrypt():

    password=code.get()
    message=text1.get(1.0,END)
    temp=message.split()
    #calling the decrypt string function
    dec=[]
    for t in temp:
        decrypted_word = decrypt_string(t)
        dec.append(decrypted_word)
    #print(dec)
    #message=message[:len(message)-1]
    #message=message.split(",")
    #print(message)
    decrypt=[]
    for i in dec:
        temp=i
        # print(temp)
        n=len(temp)
        D1 = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            D1[i][i] = int(temp[i])
        DE = D1 + n*(np.identity(n,dtype=int))
        result=[DE[r][r] for r in range(n)]

        if(n%2==0):
            L = int((n/2))
        else:
            L = int(((n+1)/2))
        res=np.roll(result,L-1)
        fin_res=[]
        for i in range(len(res)):
            pos=val_list.index(res[i])
            fin_res.append(key_list[pos])

        decrypt.append(fin_res)
    
    fin_answer=''
    for i in decrypt:
        for j in i:
            fin_answer+=str(j)
        fin_answer+=' '

    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#808080")

        '''mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harish1234",
            database="worksheet1"
        )

        c=mydb.cursor()
        c.execute("SELECT * FROM encrypt ")
        rows=c.fetchall()
        sent,passw=zip(*rows)
        print(sent,passw)
        mydb.close()'''

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56",justify=CENTER).place(x=10,y=0)
        text2=Text(screen2,font="robote 10",bg="white",relief=SUNKEN,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,fin_answer)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password")


def encrypt():
    password=code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0,END)
        #to remove '\n' from the string
        message=message[:len(message)-1]
        message=message.upper()
        mess=message.split(" ")
        #calling the function
        encrypted=circulant(mess) 

        string=''
        for i in encrypted:
            encrypted_string = encrypt_word(i)
            string+=encrypted_string+' '   

        #print("ecrypted form :",string)
        res =",".join(str(i) for i in encrypted)

        sql="INSERT INTO encrypt VALUES (%s,%s)"
        val=(res,password)

        '''mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harish1234",
            database="worksheet1"
        )
        c=mydb.cursor()
        c.execute(sql,val)
        c.execute("SELECT * FROM encrypt")
        res=c.fetchall()
        print(res)

        mydb.commit()
        mydb.close()'''

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="robote 10",bg="white",relief=SUNKEN,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,string)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password")

#creating the main frame
def main_screen():

    
    global screen,code,text1
    screen=Tk()
    # messagebox.showwarning("Warning","for decryption each letter is separated by space and each word is separated is comma")
    #setting up the screen resolution
    screen.geometry("375x400")
    #setting up the icon for the window
    icon=PhotoImage(file="C:/Users/haris/OneDrive/Desktop/Harish/semester 4/scl project/key.png")
    screen.iconphoto(False,icon)
    screen.title("Encryption_and_Decryption")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    #setting up the text editor with title

    Label(text="Enter the text",fg="black",font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",13)).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="Encrypt",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="Decrypt",height="2",width=23,bg="#edbd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="Reset",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)

    screen.resizable(True,True)
    screen.mainloop()

main_screen()