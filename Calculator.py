import tkinter as tk
import tkinter.font as tkFont

# create display
root = tk.Tk()
root.geometry('280x345')
root.resizable(0, 0)
root.title('Calculator')
text = tk.StringVar()

# set font of label
font = tkFont.Font(family="Arial", size=25, weight="bold")
# set label position
lbl = tk.Label(root, textvariable=text, font=font, anchor='se', padx=10, pady=10)
lbl.pack(side=tk.TOP, fill=tk.X, ipady=20)
# create frame to hold buttons
frame = tk.Frame(root)
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# take inputs of digits


def value(num):
    result = text.get()
    text.set('')
    result = str(result)+str(num)
    print(result)
    text.set(result)

# store operator to preform calculation


def operation(operator):
    global first_value
    global symbol
    first_num = text.get()
    symbol = operator
    first_value = float(first_num)
    text.set('')

# checks operator to preform calculation and check if int value


def button_equal():
    next_value = text.get()
    text.set('')
    if symbol == "+":
        result = first_value + float(next_value)
    elif symbol == "-":
        result = first_value - float(next_value)
    elif symbol == "x":
        result = first_value * float(next_value)
    elif symbol == "÷":
        result = first_value / float(next_value)
    if (result).is_integer():
        text.set(int(result))
    else:
        text.set(float(result))

# clears the label


def clear():
    text.set(' ')

# removes a single digit from value


def delete():
    result = text.get()
    result = result[:-1]
    text.set(result)

# changes the value to position if negative, vice versa


def negate():
    result = text.get()
    result = int(result)
    if result > 0:
        result = '-' + str(result)
    elif result < 0:
        result = result * (-1)
    text.set(result)


# create buttons and functions given
btnCE = tk.Button(frame, text="CE", bg='#EBEBEB', bd=1, relief='solid', command=lambda: clear())
btnClear = tk.Button(frame, text="C", bg='#EBEBEB', bd=1, relief='solid', command=lambda: clear())
btnDel = tk.Button(frame, text="DEL", bg='#EBEBEB', bd=1, relief='solid', command=lambda: delete())
btnDiv = tk.Button(frame, text="÷", bg='#EBEBEB', bd=1,
                   relief='solid', command=lambda: operation('÷'))
btn7 = tk.Button(frame, text="7", bg='white', bd=1, relief='solid', command=lambda: value(7))
btn8 = tk.Button(frame, text="8", bg='white', bd=1, relief='solid', command=lambda: value(8))
btn9 = tk.Button(frame, text="9", bg='white', bd=1, relief='solid', command=lambda: value(9))
btnMult = tk.Button(frame, text="x", bg='#EBEBEB', bd=1,
                    relief='solid', command=lambda: operation('x'))
btn4 = tk.Button(frame, text="4", bg='white', bd=1, relief='solid', command=lambda: value(4))
btn5 = tk.Button(frame, text="5", bg='white', bd=1, relief='solid', command=lambda: value(5))
btn6 = tk.Button(frame, text="6", bg='white', bd=1, relief='solid', command=lambda: value(6))
btnSub = tk.Button(frame, text="-", bg='#EBEBEB', bd=1,
                   relief='solid', command=lambda: operation('-'))
btn1 = tk.Button(frame, text="1", bg='white', bd=1, relief='solid', command=lambda: value(1))
btn2 = tk.Button(frame, text="2", bg='white', bd=1, relief='solid', command=lambda: value(2))
btn3 = tk.Button(frame, text="3", bg='white', bd=1, relief='solid', command=lambda: value(3))
btnAdd = tk.Button(frame, text="+", bg='#EBEBEB', bd=1,
                   relief='solid', command=lambda: operation('+'))
btnNeg = tk.Button(frame, text="+/-", bg='white', bd=1, relief='solid', command=lambda: negate())
btn0 = tk.Button(frame, text="0", bg='white', bd=1, relief='solid', command=lambda: value(0))
btnDot = tk.Button(frame, text=".", bg='white', bd=1,
                   relief='solid', command=lambda: value('.'))
btnEqual = tk.Button(frame, text="=", bg='#A9CCD4', bd=1, relief='solid', command=button_equal)

# position the buttons within the frame
btnCE.grid(column=0, row=0, sticky='nesw')
btnClear.grid(column=1, row=0, sticky='nesw')
btnDel.grid(column=2, row=0, sticky='nesw')
btnDiv.grid(column=3, row=0, sticky='nesw')
btn7.grid(column=0, row=1, sticky='nesw')
btn8.grid(column=1, row=1, sticky='nesw')
btn9.grid(column=2, row=1, sticky='nesw')
btnMult.grid(column=3, row=1, sticky='nesw')
btn4.grid(column=0, row=2, sticky='nesw')
btn5.grid(column=1, row=2, sticky='nesw')
btn6.grid(column=2, row=2, sticky='nesw')
btnSub.grid(column=3, row=2, sticky='nesw')
btn1.grid(column=0, row=3, sticky='nesw')
btn2.grid(column=1, row=3, sticky='nesw')
btn3.grid(column=2, row=3, sticky='nesw')
btnAdd.grid(column=3, row=3, sticky='nesw')
btnNeg.grid(column=0, row=4, sticky='nesw')
btn0.grid(column=1, row=4, sticky='nesw')
btnDot.grid(column=2, row=4, sticky='nesw')
btnEqual.grid(column=3, row=4, sticky='nesw')

# Equal space the buttons in a table of 4x5
frame.columnconfigure([0, 1, 2, 3], weight=1)
frame.rowconfigure([0, 1, 2, 3, 4], weight=1)

# call the program
root.mainloop()
