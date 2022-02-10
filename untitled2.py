from tkinter import *
root = Tk()
root.title("Inheritance")
root.geometry("600x600")
def grade_3():
    lthre["text"]="45.0"
def grade_4():
    lfor["text"]="60.0"
def grade_5():
    lfiv["text"]="65.0"
three=Button(root,text="Grade 3",command=grade_3)
three.pack()
lthre=Label(root)
lthre.pack()
four=Button(root,text="Grade 4",command=grade_4)
four.pack()
lfor=Label(root)
lfor.pack()
five=Button(root,text="Grade 5",command=grade_5)
five.pack()
lfiv=Label(root)
lfiv.pack()

root.mainloop()