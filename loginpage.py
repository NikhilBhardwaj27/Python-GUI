from tkinter import *

#creating login page for sample testing

class login:

	def __init__(self,root):

		self.root = root

		self.frame = Frame(self.root,bg='OrangeRed2',width=800,height=600) #creating frame 

		self.label = Label(self.frame,text='Log In',bg='OrangeRed2', #creating login Label
		fg='honeydew',font=('Georgia',40,'bold')) 

		self.name = Label(self.frame,text='Enter Username : ',   
		bg='OrangeRed2',fg='honeydew',font=('Arial',20,'bold'))  #creating Username label

		self.nameE = Entry(self.frame,bg='honeydew',fg='gray20',
                width=40,font=('Arial',20,'bold'))

		self.password = Label(self.frame,text='Enter Password : ',bg='OrangeRed2', #creating Password label
		fg='honeydew',font=('Arial',20,'bold'))                                      

		self.passwordE = Entry(self.frame,bg='honeydew',fg='gray20',
		width=40,font=('Arial',20,'bold'),show='*')

		self.button = Button(self.frame,text='Submit',bg='gray80',fg='gray12',   #creating Button
		font=('Georgia',20,'bold'),cursor='hand2',command=self.click)

		# packing and layouts

		self.label.place(x=40,y=40,width=200,height=80)

		self.name.place(x=100,y=140,width=240,height=60)

		self.password.place(x=100,y=220,width=240,height=60)

		self.nameE.place(x=380,y=150,width=300,height=40)

		self.passwordE.place(x=380,y=230,width=300,height=40)

		self.button.place(x=270,y=350,width=150,height=60)

		self.frame.pack()

	# Handling events on button clicks
	def click(self):
		 self.pas = self.passwordE.get()
		
		 self.res = Entry(self.frame,bg='honeydew',fg='gray20',  #creating entry widget for showing password
                 width=40,font=('Arial',20,'bold'))
 
		 self.text1 = Text(self.frame,bg='honeydew',
		 	fg='gray20',font=('Arial',20,'bold'),wrap=NONE)  #embedding text in entry widget 

		 self.text1.insert(CURRENT,self.pas)

		 self.label3 = Label(self.frame,text='Your Password is: ',
		 bg='OrangeRed2',fg='honeydew',font=('Arial',20,'bold'))

		 #packing and layouts

		 self.res.place(x=420,y=450,width=280,height=40)

		 self.label3.place(x=130,y=450,width=280,height=40)

		 self.text1.place(x=420,y=450,width=280,height=40)
               
#creating root window
root = Tk()

root.title('Graphics')

root.geometry('800x600')

obj = login(root)

root.mainloop()
