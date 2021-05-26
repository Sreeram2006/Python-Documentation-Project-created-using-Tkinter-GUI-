from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
root=Tk()
root.iconbitmap("python-logo.ico")
#Functions
def pyedit():
    compiler=Toplevel(root)
    compiler.title('PyEdit')
    file_path = ''


    def set_file_path(path):
        global file_path
        file_path = path


    def open_file():
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r') as file:
            code = file.read()
            editor.delete('1.0', END)
            editor.insert('1.0', code)
            set_file_path(path)


    def save_as():
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = file_path
        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            set_file_path(path)


    def run():
        if file_path == '':
            save_prompt = Toplevel()
            text = Label(save_prompt, text='Please save your code before running it')
            text.pack()
            return
        command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,     shell=True)
        output, error = process.communicate()
        code_output.insert('1.0', output)
        code_output.insert('1.0',  error)


    menu_bar = Menu(compiler)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Open', command=open_file)
    file_menu.add_command(label='Save', command=save_as)
    file_menu.add_command(label='Save As', command=save_as)
    file_menu.add_command(label='Exit', command=exit)
    menu_bar.add_cascade(label='File', menu=file_menu)

    run_bar = Menu(menu_bar, tearoff=0)
    run_bar.add_command(label='Run', command=run)
    menu_bar.add_cascade(label='Run', menu=run_bar)

    compiler.config(menu=menu_bar)

    editor = Text().pack()

    code_output = Text(height=10).pack()
    compiler.mainloop()
#Labels
Label(root, text="Welcome to the Python Documentation. Please select a topic below to start learning", bg="#ff0000", font=("Arial", 15,'bold'), width=125, fg="yellow").grid(row=0,column=0,sticky=N,padx=10,pady=10)

#Buttons
Button(root, text="",bg="black",fg="white",width=30, font=("Arial", 15)).grid(row=1,column=0,sticky=N)
Button(root,text="",bg="black", width=30, fg="white", font=("Arial", 15), ).grid(row=2,column=0,padx=10,pady=10,sticky=N)
Button(root,text="",bg="black", width=30, fg="white", font=("Arial", 15)).grid(row=3,column=0,sticky=N,padx=10,pady=10)
Button(root,text="",bg="black", width=30, fg="white", font=("Arial", 15)).grid(row=4,column=0,sticky=N,padx=10,pady=10)
Button(root,text="",bg="black", width=30, fg="white", font=("Arial", 15)).grid(row=5,column=0,sticky=N,padx=10,pady=10)
Button(root,text="",bg="black", width=30, fg="white", font=("Arial", 15)).grid(row=6,column=0,sticky=N)
Button(root,text="",bg="black", width=30, fg="white", font=("Arial", 15)).grid(row=7,column=0,sticky=N,padx=10,pady=10)
Button(root,text="",bg="black", width=30, fg="white", font=("Arial", 15)).grid(row=8,column=0,sticky=N,padx=10,pady=10)
Button(root,text="",bg="black", width=30, fg="white", font=("Arial", 15)).grid(row=9,column=0,sticky=N,padx=10,pady=10)
Button(root,text="",bg="black", width=30, fg="white", font=("Arial", 15)).grid(row=10,column=0,sticky=N,padx=10,pady=10)
Button(root,text="Start coding!",bg="black", width=30, fg="white", font=("Arial", 15), command=pyedit).grid(row=11,column=0,sticky=N,padx=10,pady=10)
root.mainloop()