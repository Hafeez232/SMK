from tkinter import *
from tkinter import messagebox

win = Tk()

result1 = messagebox.askokcancel("Hafeez ","Hello")
print(result1)# Yes = True , No = False

result2 = messagebox.askyesno("Hafeez","Hello")
print(result2)# Yes = True , No = False

result3 = messagebox.askyesnocancel("Hafeez","Hello")
print(result3)# Yes = True , No = False , cancel = None

messagebox.showinfo("Hello", "I dont know what to write")
messagebox.showwarning("warning", "I dont know what to write")
messagebox.showerror("error", "Brain not found XD")

win.mainloop()
