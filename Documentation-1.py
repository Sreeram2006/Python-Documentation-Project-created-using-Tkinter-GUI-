from tkinter import * #pip install tkintertable
from PIL import ImageTk, Image #pip install pillow
from tkhtmlview import *
from tkhtmlview.html_parser import HTML #pip install tkhtmlview
root=Tk()
root.iconbitmap("python-logo.ico")
root.title("Python Documentation")
root.geometry("1000x1000")
root.config(bg="#00ff91") # 00ff91 is a sea green shade

#functions
def python_3():
    pyth_scr=Toplevel(root)
    pyth_scr.title('Installing Python 3 on Windows')
    pyth_scr.config(bg="white")
    HTMLLabel(pyth_scr, html="<p>Open up your browser. Go to python.org. Click on the 'Downloads' section and download it for Windows.</p><p>By default, if you click download, it will be downloaded for Windows Operating System.</p><p>But there are options for Mac OS, Linux, Solaris,Unix etc....</p><b><u>Important: </u></b><p>Remember to check the 'Add Python 3.9 to Path' option when downloading.</p>That will be a huge help while building games or GUI.</p><p>Python will be able to access your system to find the requirements you have asked for.</p><img src='python_org.png'>",bg="white",height=1000,width=1000).grid(row=0,column=0,sticky=N)
    

def code_editor():
    c_edit=Toplevel(root)
    c_edit.title("Choosing a code editor")
    c_edit.config(bg="yellow")
    HTMLLabel(c_edit, html="<p>Choosing a code editor for Python has various options like VS Code, Sublime Text 3, Atom and by far the best ranked PyCharm.</p><p>If you want only Python Development, then go with PyCharm.</p><p>But it has a paid version where you get advanced features which you don't get in the community version.</p><p>So its better to stick with the free ones like VS Code or Sublime Text.</p><p>I highly recommend using VS Code as it has all services like Intense Debugging, Auto complete, more than 5000 highly useful extensions and more.</p><p>Here are the links to download the code editors VS Code, Sublime Text, Atom, PyCharm</p><p></p><a href='https://code.visualstudio.com/download'>Download VS Code</a><br><a href='https://www.jetbrains.com/pycharm/download/#section=windows'>Download PyCharm</a><br><a href='https://www.sublimetext.com/3'>Download Sublime Text 3</a><br><a href='https://atom.io/'>Download Atom</a><br><img src='vscode.png'>",background="yellow",height=1000,width=1000).grid(row=0,column=0,sticky=N)

    HTMLLabel(c_edit, html="<img src='vscode.png'>").grid(row=6,column=0,sticky=N)


def get_start():
    pyth_start=Toplevel(root)
    pyth_start.title("Getting Started with Python")
    pyth_start.config(bg="#164dc4") #164dc4 is a semi-dark bluish kind of shade
    HTMLLabel(pyth_start, html="<p>Python is a programming language used for making desktop applications, GUI Apps, making websites using the Flask and Django frameworks.</p> It is also used in data science and machine learning</p><p><b><u>Important:</u></b> For the Python Code to run on your system editor you need to have the Python 3.9 Software. Refer to the previous for more information.</p><p>While using VS Code/PyCharm, please install these usefull extensions that will improve your speed and productivity while writing Python.</p><ol><li>Python Extension form Microsoft</li><li>PyLance Extension</li><li>Jupyter-Lab Extension</li><li>Tabnine/Kite extension for fast autocomplete</li><li>Beautify or Prettier extension (So that the code looks neat and uniform with auto indents and correct spacing!)</li></ol><img src='python-ext.png'>", background="#34e619", font=("Arial", 13),height=1000,width=1000).grid(row=0,column=0)

def print_statements():
    print_st=Toplevel(root)
    print_st.title("Print Statements in Python") 
    print_st.config(bg="#ff7b08")
    HTMLLabel(print_st, html="<p>Print Statements are the first thing that any bginner in Python should learn.</p><p>It is used to show certain text, numbers, output taken from input, variables, lists, arrays, etc... in something called a Terminal or an output box, in simpler words.</p><p>This is how a print statement looks</p><p>print('Hello world')</p><p>This prints the term Hello world in the Terminal.</p><p>You can also print integers, decimals, and even negative decimals.</p><p>print(35)</p><p>print(3.4)</p><p>print(-2)</p><img src='ouput1.png'>",height=1000,width=1000,background="cyan",foreground="white").grid(row=0, column=0, sticky=W)
    

def variables():
    var_scr=Toplevel(root)
    var_scr.title("Python Variables")
    var_scr.config(bg="#c9eb34") #c9eb34 is a ligh yellow shade
    HTMLLabel(var_scr, html="<p>Variables in Python are used to store any kind of data like strings,numbers,decimals, lists,arrays etc..</p><p>You can make n number of variables in Python, there is no limit.</p><p>How to create a variable:</p><img src='text_var.png'><p>To use a multi-word variable separate each word with an underscore(_).</p><p>Let us print these variables and show the output in the Terminal.</p><center><img src='print_var.png'></center><p>You shoud get the following output after wriitng and running the above code: </p> <img src='var_result.png'>", height=1000,width=1000,bg="white").grid(row=0,column=0,sticky=W)
def datatypes():
    data_scr =Toplevel(root)
    data_scr.title("Datatypes in Python")
    data_scr.config(bg="#8800ff") #8800ff is a purple shade
    HTMLLabel(data_scr, html="<p>Datatypes in in Python are of 8 types. They are: \
        <ol>\
        <li>Strings (Anything in single or doube quotes is treated as a string)</li>\
        <li>Integers (Whole numbers, both negative and positive)</li>\
        <li>Floats (Decimals)</li>\
        <li>Lists</li>\
        <li>Tuples (A list that can't be edited once created)</li>\
        <li>Sets</li>\
        <li>Dictionaries</li>\
        <li>Booleans (True and False)</li>\
        </ol>\
        <p>Below it is shown how they look like in Python code:</p> <img src='datatypes.png'><p><b><u>Very Important:</u></b>You cannot use the folowing names as variable names in Python as they are the names of datatypes: str, int, float, dict, bool, list.</p>",height=1000,width=1000,background="#ff6a00",font=('Calibri')).grid(row=0,column=0,sticky=W)

def typecasting():
    type_cast=Toplevel(root)
    type_cast.title("Typecasting in Python")
    type_cast.config(bg="#ffffff")
    HTMLLabel(type_cast, html="<p>Typecasting in Python means checking the datatype fo some random data and we try to convert them into another datatype.</p> <p>The most common type conversions are integers to floats and floats to integers.</p> <p>Checking the type and then coverting it to another datatype is done like this: <br><br> <img src='type-1.png'> <br> <br> <img src='type-2.png'> <p>You should get the following ouput:</p><img src='type-3.png'> ",height=1000,width=1000).grid(row=0,column=0,sticky=W)

def take_inp():
    input_screen=Toplevel(root)
    input_screen.title("Taking Input from a User")
    HTMLLabel(input_screen, html="<p>Taking input in Python is pretty easy.</p><p>The most common type of inputs taken are string type, integer type and float type.</p><p>By default, input type is set to string.</p><p>The input should always be stored in a variable.</p><p>Do this to take inputs of string, integer and float types from the user.</p> <p>Let us print them using the basic print function.</p><img src='inp-print.png'><p>This is how your ouput should look like: </p> <img src='inp-print2.png'>", height=1000, width=1000).grid(row=0,column=0,sticky=W)

def arithmetic():
    math_scr=Toplevel(root)
    math_scr.title("Arithmetic in Python")
    HTMLLabel(math_scr, html="<p>Following are the arithmetic operators and how to perform arithmetic calculations on them in Python.</p><img src='arithmetic.png'><p><b><u>Output of the above code:</u></b></p><img src='arithmetic_output.png'><p><b><u>Note:</u></b></p><p>While taking an input for a integer for arithmetic use int(input).</p>", height=1000,width=1000).grid(row=0,column=0,sticky=W)

def if_elif_else():
    if_scr=Toplevel(root)
    if_scr.title("If, Else and elif conditions")
    HTMLLabel(if_scr, html="<p>If, elif and else conditions are used for verification.</p><p>Example:</p><p>a=input('Enter some text: '))</p><p>if a=='Python':</p><p>\t print('Correct')</p><p>elif a=='programming':</p><p>\tprint('Almost correct')</p><p>else:</p><p>\t print('Incorrect')</p><p><b>Explanation:</p><p>We have asked an input from the user.</p><p>If that input is Python, we show correct. If the input is programming, we show almost correct.</p><p>if the user types anything else, we show incorrect.</p>", height=1000,width=1000).grid(row=0,column=0,sticky=W) #tabspace not working here

def calc():
    calc_scr=Toplevel(root)
    calc_scr.title("Building a calculator")
    HTMLLabel(calc_scr, html="<img src='calc_code.png'><p>Output:</p><img src='calc_output.png'>",height=1000,width=1000).grid(row=0,column=0,sticky=W)
    #Labels
Label(root, text="Welcome to the Python Documentation. Please select a topic below to start learning", bg="#ff0000", font=("Arial", 15,'bold'), width=125, fg="yellow").grid(row=0,column=0,sticky=N,padx=10,pady=10)

#Buttons
Button(root, text="Installing Python 3.9.5 on Windows", command=python_3,bg="black",fg="white",width=30, font=("Arial", 15)).grid(row=1,column=0,sticky=N)

Button(root,text="Choosing a Code Editor",bg="black", width=30, fg="white", font=("Arial", 15), command=code_editor).grid(row=2,column=0,padx=10,pady=10,sticky=N)
Button(root,text="Getting Started With Python",bg="black", width=30, fg="white", font=("Arial", 15),command=get_start).grid(row=3,column=0,sticky=N,padx=10,pady=10)
Button(root,text="Print Statements",bg="black", width=30, fg="white", font=("Arial", 15), command=print_statements).grid(row=4,column=0,sticky=N,padx=10,pady=10)
Button(root,text="Variables",bg="black", width=30, fg="white", font=("Arial", 15), command=variables).grid(row=5,column=0,sticky=N,padx=10,pady=10)
Button(root,text="Datatypes",bg="black", width=30, fg="white", font=("Arial", 15), command=datatypes).grid(row=6,column=0,sticky=N)
Button(root,text="Typecasting",bg="black", width=30, fg="white", font=("Arial", 15), command=typecasting).grid(row=7,column=0,sticky=N,padx=10,pady=10)
Button(root,text="Taking Input",bg="black", width=30, fg="white", font=("Arial", 15),command=take_inp).grid(row=8,column=0,sticky=N,padx=10,pady=10)
Button(root,text="Arithmetic in Python",bg="black", width=30, fg="white", font=("Arial", 15),command=arithmetic).grid(row=9,column=0,sticky=N,padx=10,pady=10)
Button(root,text="If, Elif and Else Conditions",bg="black", width=30, fg="white", font=("Arial", 15),command=if_elif_else).grid(row=10,column=0,sticky=N,padx=10,pady=10)
Button(root,text="Building a Calculator",bg="black", width=30, fg="white", font=("Arial", 15), command=calc).grid(row=11,column=0,sticky=N,padx=10,pady=10)


root.mainloop()