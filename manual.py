from tkinter import *
def manual():
	win=Tk()
	
	win.title("Manual")
	win.geometry('750x350')
	

	lbl=Label(win,text="To open,save or create a new file got to file options and click the respective option.\nTo cut,copy or paste something go to edit options and click the respective option.\n To get help click on the Help button.\n \n ABOUT \n This notepad is built by a young programmer wit python using tkinter \nthis notepad is inspired from Windows Notepad ",font=("Arial",15))
	lbl.pack()

	win.mainloop()