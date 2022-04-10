
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
import pymysql
import pyttsx3
import PyPDF2


#---------------------------------------------------------------Login Function --------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()	


def login():
	if user_name.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password",parent=win)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="audiobook")
			cur = con.cursor()

			cur.execute("select * from userdetails where username=%s and password = %s",(user_name.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

			else:
				messagebox.showinfo("Success" , "Successfully Login" , parent = win)
				close()
				main()
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)

#---------------------------------------------------------------End Login Function ---------------------------------

#---------------------------------------------------- Main Panel -----------------------------------------
def main():

	des = Tk()
	des.title("AudioBook")
	des.configure(bg=bg)
	des.maxsize(width=800 ,  height=500)
	des.minsize(width=800 ,  height=500)

	def click():
		global path
		path = filedialog.askopenfilename()
		print(path)

	def play():
		if path:
			book = open(path, 'rb')
			pdfReader = PyPDF2.PdfFileReader(book)
			pages = pdfReader.numPages

			speaker = pyttsx3.init()
			for num in range(10, pages):
				page = pdfReader.getPage(num)
				text = page.extractText()
				speaker.say(text)
				speaker.runAndWait()



	# heading label
	heading = Label(des , text = f"Welcome : {user_name.get()}" , font = 'Verdana 20 bold', bg=bg)
	heading.place(x=220 , y=50)

	openbook = Label(des, text="Please choose a PDF", font = 'Verdana 20',bg=bg)
	openbook.place(x=220, y=150)
	open_PDF = Button(des, text='Open', width=20 , bg='red',command=click)
	open_PDF.place(x=300, y=200)

	playl=Label(des, text="Press this button to start your book", font="Verdana 20", bg=bg)
	playl.place(x=220, y=250)
	play = Button(des, text='Play', width=20,bg='red',command=play)
	play.place(x=300, y=300)

#-----------------------------------------------------End Main Panel -------------------------------------
#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
	# signup database connect 
	def action():
		if first_name.get()=="" or last_name.get()=="" or email.get()=="" or user_name.get()=="" or password.get()=="" or veri_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
		elif password.get() != veri_pass.get():
			messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
		else:
			try:
				con = pymysql.connect(host="localhost",user="root",password="",database="audiobook")
				cur = con.cursor()
				cur.execute("select * from userdetails where username=%s",user_name.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
				else:
					cur.execute("insert into userdetails(first_name,last_name,email,username,password) values(%s,%s,%s,%s,%s)",
						(
						first_name.get(),
						last_name.get(),
						email.get(),
						user_name.get(),
						password.get()
						))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
					clear()
					switch()
				
			except Exception as es:
				messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)

	# close signup function			
	def switch():
		winsignup.destroy()

	# clear data function
	def clear():
		first_name.delete(0,END)
		last_name.delete(0,END)
		email.delete(0,END)
		user_name.delete(0,END)
		password.delete(0,END)
		veri_pass.delete(0,END)


	# start Signup Window	

	winsignup = Tk()
	winsignup.title("Audiook Registration Window")
	winsignup.configure(bg=bg)
	winsignup.maxsize(width=500 ,  height=600)
	winsignup.minsize(width=500 ,  height=600)


	#heading label
	heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold', bg=bg)
	heading.place(x=80 , y=60)

	# form data label
	first_name = Label(winsignup, text= "First Name :" , font='Verdana 10 bold', bg=bg)
	first_name.place(x=80,y=130)

	last_name = Label(winsignup, text= "Last Name :" , font='Verdana 10 bold', bg=bg)
	last_name.place(x=80,y=160)

	email = Label(winsignup, text = "Email :" , font='Verdana 10 bold', bg=bg)
	email.place(x=80,y=190)

	user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold', bg=bg)
	user_name.place(x=80,y=220)

	password = Label(winsignup, text= "Password :" , font='Verdana 10 bold', bg=bg)
	password.place(x=80,y=250)

	veri_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold', bg=bg)
	veri_pass.place(x=60,y=280)

	# Entry Box ------------------------------------------------------------------

	first_name = StringVar()
	last_name = StringVar()
	email = StringVar()
	user_name = StringVar()
	password = StringVar()
	veri_pass = StringVar()


	first_name = Entry(winsignup, width=40 , textvariable = first_name)
	first_name.place(x=200 , y=133)


	
	last_name = Entry(winsignup, width=40 , textvariable = last_name)
	last_name.place(x=200 , y=163)

	
	email = Entry(winsignup, width=40, textvariable = email)
	email.place(x=200 , y=193)

	
	user_name = Entry(winsignup, width=40,textvariable = user_name)
	user_name.place(x=200 , y=223)

	
	password = Entry(winsignup, width=40, textvariable = password)
	password.place(x=200 , y=253)

	
	veri_pass= Entry(winsignup, width=40 ,show="*" , textvariable = veri_pass)
	veri_pass.place(x=200 , y=283)


	# button login and clear

	btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
	btn_signup.place(x=200, y=313)


	btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
	btn_login.place(x=280, y=313)


	sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
	sign_up_btn.place(x=350 , y =20)


	winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------	


	

#------------------------------------------------------------ Login Window -----------------------------------------
bg = '#00ffff'
win = Tk()

# app title
win.title("AudioBook Login Window")
win.configure(bg=bg)

# window size
win.maxsize(width=500 ,  height=500)
win.minsize(width=500 ,  height=500)


#heading label
heading = Label(win , text = "Login" , font = 'Verdana 25 bold', bg=bg)
heading.place(x=80 , y=150)

username = Label(win, text= "User Name :" , font='Verdana 10 bold', bg=bg)
username.place(x=80,y=220)

userpass = Label(win, text= "Password :" , font='Verdana 10 bold',bg=bg)
userpass.place(x=80,y=260)

# Entry Box
user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)


# button login and clear

btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)


btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(win , text="Switch To Sign up" , command = signup )
sign_up_btn.place(x=350 , y =20)



win.mainloop()

#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------
