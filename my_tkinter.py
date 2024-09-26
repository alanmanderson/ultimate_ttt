import tkinter
import tkinter.filedialog

top = tkinter.Tk()
top.withdraw()
file_name = tkinter.filedialog.askopenfilename(parent=top)
top.destroy()
print(file_name)
