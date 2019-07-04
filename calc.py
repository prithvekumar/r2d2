import tkinter

from tkinter import*
expression = ""
gui = Tk()
def press(num):
        global expression
        expression = expression + str(num) 
        equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression)) 
        equation.set(total)

    except:
        equation.set(" error ") 
        expression = ""

        
def clear(): 
	global expression 
	expression = "" 
	equation.set("")
def function():
    pass
	
if __name__ == "__main__":
    
    root_menu = tkinter.Menu(gui)
    gui.config(menu = root_menu)
    file_menu = tkinter.Menu(root_menu)
    root_menu.add_cascade(label = "File", menu = file_menu)
    file_menu.add_command(label = "New file.....", command = function) # it adds a option to the sub menu 'command' parameter is used to do some action
    file_menu.add_command(label = "Open files", command = function)
    file_menu.add_separator() # it adds a line after the 'Open files' option
    file_menu.add_command(label = "Exit", command = gui.quit)
    
    gui.configure(background="yellow")
	
    gui.title("Calculator")  
    gui.geometry("500x300")
	
    equation = StringVar() 
    field = Entry(gui, textvariable=equation,)
    field.grid(columnspan=6, ipadx=150, ipady=20) 
    equation.set('') 
     
    button1 = Button(gui, text=' 1 ', fg='red', bg='light blue',command=lambda: press(1), height=2, width=8) 
    button1.grid(row=2, column=0) 

    button2 = Button(gui, text=' 2 ', fg='red', bg='light blue',command=lambda: press(2), height=2, width=8) 
    button2.grid(row=2, column=1) 

    button3 = Button(gui, text=' 3 ', fg='red', bg='light blue',command=lambda: press(3), height=2, width=8) 
    button3.grid(row=2, column=2) 

    button4 = Button(gui, text=' 4 ', fg='red', bg='light blue',command=lambda: press(4), height=2, width=8) 
    button4.grid(row=3, column=0) 

    button5 = Button(gui, text=' 5 ', fg='red', bg='light blue',command=lambda: press(5), height=2, width=8) 
    button5.grid(row=3, column=1) 

    button6 = Button(gui, text=' 6 ', fg='red', bg='light blue',command=lambda: press(6), height=2, width=8) 
    button6.grid(row=3, column=2) 

    button7 = Button(gui, text=' 7 ', fg='red', bg='light blue',command=lambda: press(7), height=2, width=8) 
    button7.grid(row=4, column=0) 

    button8 = Button(gui, text=' 8 ', fg='red', bg='light blue',command=lambda: press(8), height=2, width=8) 
    button8.grid(row=4, column=1) 

    button9 = Button(gui, text=' 9 ', fg='red', bg='light blue',command=lambda: press(9), height=2, width=8) 
    button9.grid(row=4, column=2) 

    button0 = Button(gui, text=' 0 ', fg='red', bg='light blue',command=lambda: press(0), height=2, width=8) 
    button0.grid(row=5, column=0) 

    plus = Button(gui, text=' + ', fg='black', bg='red',command=lambda: press("+"), height=2, width=8) 
    plus.grid(row=2, column=3) 

    minus = Button(gui, text=' - ', fg='black', bg='red',command=lambda: press("-"), height=2, width=8) 
    minus.grid(row=3, column=3) 

    multiply = Button(gui, text=' * ', fg='black', bg='red',command=lambda: press("*"), height=2, width=8) 
    multiply.grid(row=4, column=3) 

    divide = Button(gui, text=' / ', fg='black', bg='red',command=lambda: press("/"), height=2, width=8) 
    divide.grid(row=5, column=3) 

    equal = Button(gui, text=' = ', fg='black', bg='red',command=equalpress, height=2, width=8) 
    equal.grid(row=5, column=2) 

    clear = Button(gui, text='Clear', fg='black', bg='red',command=clear, height=2, width=8) 
    clear.grid(row=5, column=1)

    square = Button(gui, text=' ** ', fg='black', bg='red',command=lambda: press("**"), height=2, width=8) 
    square.grid(row=2, column=4)

    obracket = Button(gui, text=' ( ', fg='black', bg='red',command=lambda: press("("), height=2, width=8) 
    obracket.grid(row=3, column=4)

    cbracket = Button(gui, text=' ) ', fg='black', bg='red',command=lambda: press(")"), height=2, width=8) 
    cbracket.grid(row=4, column=4)

    percent = Button(gui, text=' % ', fg='black', bg='red',command=lambda: press("%"),height=2, width=8) 
    percent.grid(row=5, column=4)
    
    gui.mainloop() 
