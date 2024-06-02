from tkinter import*
import tkinter.font as font

cal = Tk()    ### Creating the main Window 
cal.geometry("395x472")  ### Setting the geometry of the window
cal.resizable(0,0) ##  This prevents from resizing the window.
cal.title ("Calculator")   ### Assigning the name to Window

expression = ""
inputText = StringVar()


####  Input Frame where the user can view the entered text

inputFrame = Frame(cal, width=395, height=30, bd=0, highlightbackground="black", highlightcolor="crimson", highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 20 ), textvariable=inputText, width=30,fg="black", bg="white", bd=0, justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=10)

#Button Frame
myFont = font.Font(family='Arial',size=9,weight="bold",slant="roman")
button_frame = Frame(cal,width=390, height=300, bg="grey")
button_frame.pack()


def click_button(item):        # This function continuously updates the input field whenever the number is entered.
    global expression
    inputText.set(inputText.get()+(str(item)))

def clear_button():                # This  function clears the last input item.
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clear_all():                 # This function clears the input field.
    inputText.set("")    

def equal_button():
    result = ""
    try:
        result = eval(inputText.get())      # This function evalutes the string expression directly.
        inputText.set(result)
    except:
        result = "_ERROR_"
        inputText.set(result)    
    

#### Layout of Calculator i.e Numbers and Operations.

clearall = Button(button_frame, text = "C",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: clear_all()).grid(row = 1, column = 0, padx = 1, pady = 1)
l_bracket= Button(button_frame, text = "(",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("(")).grid(row = 1, column = 1, padx = 1, pady = 1)
r_bracket = Button(button_frame, text = ")",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(")")).grid(row = 1, column = 2, padx = 1, pady = 1)
clear = Button(button_frame, text = "DLT",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: clear_button()).grid(row = 1, column = 3, padx = 1, pady = 1)


power = Button(button_frame, text = "^",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("**")).grid(row = 2, column = 0, padx = 1, pady = 1)
pie = Button(button_frame, text = "p",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(3.1415)).grid(row = 2, column = 1, padx = 1, pady = 1)
exp  = Button(button_frame, text = "e",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(2.7182)).grid(row = 2, column = 2, padx = 1, pady = 1)
divide_= Button(button_frame, text = "/",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("/")).grid(row = 2, column = 3, padx = 1, pady = 1)

seven = Button(button_frame, text = "7",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(7)).grid(row = 3, column = 0, padx = 1, pady = 1,)
eight = Button(button_frame, text = "8",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
nine = Button(button_frame, text = "9",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
multiply = Button(button_frame, text = "*",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("*")).grid(row = 3, column = 3, padx = 1, pady = 1)

four = Button(button_frame, text = "4",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(4)).grid(row = 4, column = 0, padx = 1, pady = 1)
five = Button(button_frame, text = "5",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(5)).grid(row = 4, column = 1, padx = 1, pady = 1)
six = Button(button_frame, text = "6",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(6)).grid(row = 4, column = 2, padx = 1, pady = 1)
minus = Button(button_frame, text = "-",font=myFont,fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("-")).grid(row = 4, column = 3, padx = 1, pady = 1)

one = Button(button_frame, text = "1",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(1)).grid(row = 5, column = 0, padx = 1, pady = 1)
two = Button(button_frame, text = "2",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(2)).grid(row = 5, column = 1, padx = 1, pady = 1)
three = Button(button_frame, text = "3",font=myFont, fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(3)).grid(row = 5, column = 2, padx = 1, pady = 1)
plus = Button(button_frame, text = "+", font=myFont,fg = "white", width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("+")).grid(row = 5, column = 3, padx = 1, pady = 1)

point = Button(button_frame, text = ".", fg = "white",font=myFont, width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(".")).grid(row = 6, column = 0, padx = 1, pady = 1)
zero = Button(button_frame, text = "0", fg = "white", font=myFont,width = 13, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(0)).grid(row = 6, column = 1, padx = 1, pady = 1)
equals = Button(button_frame, text = "=", fg = "white",font=myFont, width = 27, height = 4, bd = 0, bg = "black", cursor = "hand2", command = lambda: equal_button()).grid(row = 6, column = 2, columnspan = 2, padx = 1, pady = 1)

cal.mainloop()   ### Running the main Loop


