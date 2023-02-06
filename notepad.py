# importing modules
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from manual import manual

# tkinter window basic setup
root = Tk()
root.title("Untitled- NOTEPAD")
root.rowconfigure(0,minsize=750)
root.columnconfigure(1,minsize=800)
root.configure(bg="light blue")
photo = PhotoImage(file = "Icon.png")
root.iconphoto(False, photo)

# all functions for each command
def save():
	file_location = asksaveasfilename(
		defaultextension="txt",
		filetypes=[("Text files","*.txt"),["All files","*.*"]])
	if not file_location:
		return
	with open(file_location,"w") as file:
		text=text_editor.get(1.0,END)
		file.write(text)
	root.title(f"NOTEPAD {file_location}")

def openfile():
	file_location = askopenfilename(
		filetypes=[("Text files","*.txt"),["All files","*.*"]])
	if not file_location:
		return
	text_editor.delete(1.0,END)
	with open(file_location,"r") as file:
		text=file.read()
		text_editor.insert(END,text)
	root.title(f"NOTEPAD {file_location}")


def new():
	text_editor.delete(1.0,END)
	root.title("Untitled- NOTEPAD")

def cut():
	text_editor.event_generate(("<<Cut>>"))
def copy():
	text_editor.event_generate(("<<Copy>>"))
def paste():
	text_editor.event_generate(("<<Paste>>"))

def undo():
	text_editor.edit_undo

# creating the place where you write the content of file
text_editor = Text(root,font="lucida 13",undo=True,wrap="none")
text_editor.grid(row=0,column=1,sticky="nsew")
text_editor.configure(bg='light blue')

# scroll bars
scroll = Scrollbar(text_editor)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll.set)

scroll1 = Scrollbar(text_editor,orient="horizontal")
scroll1.pack(side=BOTTOM,fill=X)
scroll1.config(command=text_editor.xview)
text_editor.config(xscrollcommand=scroll1.set)

# contains all options
frame= Frame(root,relief=RAISED,bd=3,bg="light grey")
frame.grid(row=0,column=0,sticky="ns")

# all options
fileoptionlbl = Label(frame,text="FILE OPTIONS")
fileoptionlbl.grid(column=0,row=0)


savebtn = Button(frame,text="SAVE",padx=5,pady=5,command=save)
savebtn.grid(column=0,row=1,padx=10,pady=10)


openbtn = Button(frame,text="OPEN",padx=5,pady=5,command=openfile)
openbtn.grid(column=0,row=2,padx=10,pady=10)

newbtn = Button(frame,text="NEW ",padx=5,pady=5,command=new)
newbtn.grid(column=0,row=3,padx=10,pady=10)



editoptionlbl = Label(frame,text="EDIT OPTIONS")
editoptionlbl.grid(column=0,row=4)


cutbtn = Button(frame,text="CUT",padx=5,pady=5,command=cut)
cutbtn.grid(column=0,row=5,padx=10,pady=10)


copybtn = Button(frame,text="COPY",padx=5,pady=5,command=copy)
copybtn.grid(column=0,row=6,padx=10,pady=10)

pastebtn = Button(frame,text="PASTE ",padx=5,pady=5,command=paste)
pastebtn.grid(column=0,row=7,padx=10,pady=10)

helpbtn = Button(frame,text="HELP",padx=15,pady=10,command=manual)
helpbtn.grid(column=0,row=8,padx=10,pady=10)

if __name__ == "__main__":
	root.mainloop()

