from tkinter import *
import os

def register_user():
  
  user_info=username.get()
  pass_info=password.get()
  fobj=open(user_info, "w")
  fobj.write(user_info+"\n")
  fobj.write(pass_info+"\n")
  fobj.close()

  username_entry.delete(0,END)
  password_entry.delete(0,END)
  Label(screen1,text="Registration Successful",bg="SlateGray1",fg="red").pack()
  
def register():
  global screen1
  screen1=Toplevel(screen)
  screen1.title(" REGISTER ")  
  screen1.geometry("400x300") 
  screen1.configure(bg="SlateGray1")

  global username
  global password
  global username_entry
  global password_entry
  username=StringVar()
  password=StringVar()

  Label(screen1,text="Please Enter Your Details",bg="SlateGray3").pack()
  Label(screen1,text="").pack()
  Label(screen1,text="Username",bg="SlateGray3").pack()
  username_entry=Entry(screen1, textvariable=username)
  username_entry.pack()
  Label(screen1,text="Password",bg="SlateGray3").pack()
  password_entry= Entry(screen1,textvariable=password)
  password_entry.pack()
 
  Label(screen1,text="").pack()
  Button(screen1,text="Register", height="2", width="30", bg="DarkSlateGray3", command=register_user).pack()

def delete_screen3():
    screen3.destroy()

def login_success():
  global screen3
  screen3=Toplevel(screen)
  screen3.title(" Success ")  
  screen3.geometry("200x150") 
  screen3.configure(bg="SlateGray1")
  Label(screen3,text="Login Successful!!",bg="SlateGray3").pack()
  Button(screen3,text="OK", height="1", width="15", bg="DarkSlateGray3", command=delete_screen3).pack()


def delete_screen4():
    screen4.destroy()  

def password_invalid():
  global screen4
  screen4=Toplevel(screen)
  screen4.title(" Invalid Password ")  
  screen4.geometry("200x150") 
  screen4.configure(bg="SlateGray1")
  Label(screen4,text="Invalid Password!!",bg="SlateGray3").pack()
  Button(screen4,text="OK", height="1", width="15", bg="DarkSlateGray3", command=delete_screen4).pack()


def delete_screen5():
    screen5.destroy()   

def user_not_found():
  global screen5
  screen5=Toplevel(screen)
  screen5.title(" Invalid User ")  
  screen5.geometry("200x150") 
  screen5.configure(bg="SlateGray1")
  Label(screen5,text="User not found!!",bg="SlateGray3").pack()
  Button(screen5,text="OK", height="1", width="15", bg="DarkSlateGray3", command=delete_screen5).pack()

def login_verify():
  global username1
  username1=username_verify.get()
  password1=password_verify.get()  

  username_entry1.delete(0,END)
  password_entry1.delete(0,END)
  
  list_of_files=os.listdir()
  if username1 in list_of_files:
      file1=open(username1,'r')
      verify=file1.read().splitlines()
      if password1 in verify:
          login_success()
      else:
          password_invalid()
  else:
      user_not_found()
      

def login():
  global screen2
  screen2=Toplevel(screen)
  screen2.title(" LOGIN ")  
  screen2.geometry("400x300") 
  screen2.configure(bg="SlateGray1")

  global username_verify
  global password_verify

  username_verify=StringVar()
  password_verify=StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2,text="Please Enter Your Details to Login",bg="SlateGray3").pack()
  Label(screen2,text="").pack()
  Label(screen2,text="Username",bg="SlateGray3").pack()
  username_entry1=Entry(screen2, textvariable=username_verify)
  username_entry1.pack()
  Label(screen2,text="Password",bg="SlateGray3").pack()
  password_entry1= Entry(screen2,textvariable=password_verify)
  password_entry1.pack()
  Label(screen2,text="").pack()
  Button(screen2,text="Login", height="2", width="30", bg="DarkSlateGray3", command=login_verify).pack()
  
def main_screen():
  global screen
  screen=Tk() 
  screen.title("LOGIN OR SIGNUP ")  
  screen.geometry("400x300") 
  screen.configure(bg="SlateGray1")
  Label(text="RENT YOUR IDEAL CAR ", bg="SlateGray3", width="30", height="2", font=("Arial", 13)).pack() 
  Label(text="").pack()
  Button(text="LOGIN", height="2", width="30",command=login).pack()
  Label(text="").pack()   
  Button(text="REGISTER NOW", height="2", width="30", command=register).pack()
  Label(text="").pack()  
  screen.mainloop()

main_screen()

#***************************************************************************************************************

print('__________________THE NEW WAYFARERS_________________')
print('Rent your ideal car anywhere in kochi!')

#_______Storing user data________

def delete_root1():
    root1.destroy()

import datetime
import pickle
fobj_user=open('D:\\THE NEW WAYFARERS\\'+username1,'a+')
u={}
plc=['panampilly nagar','kaloor','ernakulam south','marine drive','fort kochi','maradu','kakkanad','vytilla',
     'tripunithura','edapally','palarivattom','perumbavoo','aluva','angamaly'] 
ans='y'
while ans=='y':
  
    year=int(input('Enter year-'))
    month=int(input('Enter month-'))
    date=int(input('Enter date-'))
    date1=datetime.datetime(year,month,date,00,00,00)
    print(date1)
    date2=datetime.datetime.now()
    date3=datetime.datetime(2022,0o1,0o1,00,00,00)
    if date2<=date1<date3:
        print()
        p=print('THE NEW WAYFARERS branches at')
        for i in plc:
            print(i,end=' ')
            print()
    
        frm=input('Enter pickup destination- ')
        to=input('Enter drop off destination- ')
        if to in plc and frm in plc:
            fobj_user.write(str(date1)+'\t') 
            fobj_user.write(frm+'\t')
            fobj_user.write(to+'\n')
            print()
            print('Cars available...')
            #_____________Options____________
            e={}
            efile=open("D:\\THE NEW WAYFARERS\\Carrental.txt",'rb')
            try:
                print('%20s'%'SLNO','%15s'%'CARNAME','%20s'%'MODEL','%20s'%'FUEL','%20s'%'MODE')
                while True:
                    e=pickle.load(efile)
                    val=e.values()
                    print()
                    for i in val:
                        print('%20s'%i,end='')
                    print()
                
            except EOFError:
                print()
                efile.close()
            #____________Choice________________
            ch=int(input('Enter your choice number of car- '))
            time=int(input('Enter hours required-'))
            u1={}
            flag=0
            u1file=open("D:\\THE NEW WAYFARERS\\Carrental.txt",'rb')
            try:
                while True:
                    u1=pickle.load(u1file)
                    if u1['no']==ch:
                        print(u1)
                        fobj_user.write('\n')
                        fobj_user.write(str(u1['no'])+'\t')
                        fobj_user.write(u1['car']+'\t')
                        fobj_user.write(u1['model']+'\n')
                        chdic=u1
                        flag=1
                
            except EOFError:
                 if flag==0:
                     print('Choice Invalid!!')
                 else:
                     root1=Tk()
                     root1.title('<<<<<<<<<<<<YOUR CHOICE OF CAR!!!>>>>>>>>>>>>')
                     canvas=Canvas(root1,width=900,height=500)
                     canvas.pack()
                     img=PhotoImage(file='D:\\THE NEW WAYFARERS\\images car\\car'+str(ch)+'.png')
                     canvas.create_image(0,0, image=img, anchor=NW)
                     Button(root1,text="OK", height="2", width="30", bg="DarkSlateGray3", command=delete_root1).pack()
                     root1.mainloop()

                     print('Your booking for',chdic['car'],'is successful!')
                     print()
                     print('Renting rate per hour= 70 rupees')
                     print('Additional charge for petrol=300 rupees')      
                     print('Total FARE for',time,'hrs includinging fuel charges-',(time*70)+300,'rupees')
                     print('Enjoy your ride...')
                     
                      
                     u1file.close()
        else:
            print('Destination not available')
        ans=input('Book another car..? (y/n)')
    else:
        print("Invalid date entered!!Pleaase try again...")
fobj_user.close()

#________Read company data____________ use if u wanna check
detail=input('Do you want to view your account deatils..?(y/n)')
if detail=="y":
    E={}
    Efile=open("D:\\THE NEW WAYFARERS\\"+username1)
    s=Efile.read()
    print(s)
else:
  print('Thank you for your Patronagr..!!')
Efile.close()
