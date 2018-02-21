"""
Name:           Tkinter Exercise - a simple calculator
Description:    iOS calculator simulator
Date:           2/21/2018
Author:         Haowei Wu
"""

import tkinter

class Calculator:
    # Params
    app_title = "A simple calculator"
    disp_font = ("Helvetica", 25, "bold")
    btn_font = ("Helvetica", 20, "bold")

    def __init__(self, root):
        self.root = root
        self.initialize()
    
    def initialize(self):
        # Variables
        self.ans = "0"
        self.operator = None
        self.user_input = ""
        self.last_user_input = ""
        self.is_result = False
        self.ever_equals = False
        self.true_equal = False
        # GUI
        self.set_title()
        self.set_display()
        self.set_buttons()
        # Clear
        self.clear()
    
    def set_title(self):
        self.root.title(self.app_title)
    
    def set_display(self):
        self.display = tkinter.Entry(self.root, font=self.disp_font, justify=tkinter.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, sticky="news", ipady=10)
    
    def set_buttons(self):
        # row 1
        self.btn_clear = tkinter.Button(self.root, text="C", font=self.btn_font, command=lambda: self.btn_press("C"))
        self.btn_clear.grid(row=1, column=0, sticky="news")
        self.btn_negative = tkinter.Button(self.root, text="+/-", font=self.btn_font, command=lambda: self.btn_press("+/-"))
        self.btn_negative.grid(row=1, column=1, sticky="news")
        self.btn_percent = tkinter.Button(self.root, text="%", font=self.btn_font, command=lambda: self.btn_press("%"))
        self.btn_percent.grid(row=1, column=2, sticky="news")
        self.btn_divide = tkinter.Button(self.root, text="÷", font=self.btn_font, command=lambda: self.btn_press("/"))
        self.btn_divide.grid(row=1, column=3, sticky="news")
        # row 2
        self.btn_7 = tkinter.Button(self.root, text="7", font=self.btn_font, command=lambda: self.btn_press("7"))
        self.btn_7.grid(row=2, column=0, sticky="news")
        self.btn_8 = tkinter.Button(self.root, text="8", font=self.btn_font, command=lambda: self.btn_press("8"))
        self.btn_8.grid(row=2, column=1, sticky="news")
        self.btn_9 = tkinter.Button(self.root, text="9", font=self.btn_font, command=lambda: self.btn_press("9"))
        self.btn_9.grid(row=2, column=2, sticky="news")
        self.btn_multiply = tkinter.Button(self.root, text="x", font=self.btn_font, command=lambda: self.btn_press("*"))
        self.btn_multiply.grid(row=2, column=3, sticky="news")
        # row 3
        self.btn_4 = tkinter.Button(self.root, text="4", font=self.btn_font, command=lambda: self.btn_press("4"))
        self.btn_4.grid(row=3, column=0, sticky="news")
        self.btn_5 = tkinter.Button(self.root, text="5", font=self.btn_font, command=lambda: self.btn_press("5"))
        self.btn_5.grid(row=3, column=1, sticky="news")
        self.btn_6 = tkinter.Button(self.root, text="6", font=self.btn_font, command=lambda: self.btn_press("6"))
        self.btn_6.grid(row=3, column=2, sticky="news")
        self.btn_minus = tkinter.Button(self.root, text="-", font=self.btn_font, command=lambda: self.btn_press("-"))
        self.btn_minus.grid(row=3, column=3, sticky="news")
        # row 4
        self.btn_1 = tkinter.Button(self.root, text="1", font=self.btn_font, command=lambda: self.btn_press("1"))
        self.btn_1.grid(row=4, column=0, sticky="news")
        self.btn_2 = tkinter.Button(self.root, text="2", font=self.btn_font, command=lambda: self.btn_press("2"))
        self.btn_2.grid(row=4, column=1, sticky="news")
        self.btn_3 = tkinter.Button(self.root, text="3", font=self.btn_font, command=lambda: self.btn_press("3"))
        self.btn_3.grid(row=4, column=2, sticky="news")
        self.btn_plus = tkinter.Button(self.root, text="+", font=self.btn_font, command=lambda: self.btn_press("+"))
        self.btn_plus.grid(row=4, column=3, sticky="news")
        # row 5
        self.btn_0 = tkinter.Button(self.root, text="0", font=self.btn_font, command=lambda: self.btn_press("0"))
        self.btn_0.grid(row=5, column=0, columnspan=2, sticky="news")
        self.btn_dot = tkinter.Button(self.root, text=".", font=self.btn_font, command=lambda: self.btn_press("."))
        self.btn_dot.grid(row=5, column=2, sticky="news")
        self.btn_equal = tkinter.Button(self.root, text="=", font=self.btn_font, command=lambda: self.btn_press("="))
        self.btn_equal.grid(row=5, column=3, sticky="news")


    def clear(self):
        self.ans = "0"
        self.operator = None
        self.user_input = ""
        self.last_user_input = ""
        self.ever_equals = False
        self.is_result = False
        self.update_display("0")
        self.true_equal = False
        
    
    def update_display(self, content):
        self.display.delete(0, tkinter.END)
        self.display.insert(0, content)

    def calculation(self, ans, user_input, operator):
        ans = float(ans)
        user_input = float(user_input)
        if operator != None:
            if operator == "+":
                ans = ans + user_input
            if operator == "-":
                ans = ans - user_input
            if operator == "*":
                ans = ans * user_input
            if operator == "/":
                ans = ans / user_input
            return(str(ans))
        else:
            return(str(user_input))


    def btn_press(self, press):

        digits = [str(i) for i in range(10)]
        operators = ["+","-","*","/"]
        
        if press == "C":
            self.clear()

        if self.display.get() == "Error":
            pass
        else:
            if press in digits:
                if self.true_equal:
                    self.clear()
                self.user_input += press
                self.update_display(self.user_input)
                self.is_result = False

            if press in operators:
                if not self.ever_equals and (not self.operator):
                    if self.user_input=="":
                        self.user_input = "0"
                    self.ans = self.user_input
                    self.user_input = ""
                if self.operator and self.user_input !="":
                    self.btn_press("=")
                self.operator = press
                self.true_equal = False

            if press == ".":
                if "." not in self.user_input:
                    if self.user_input == "":
                        self.user_input = "0."
                    else:
                        self.user_input = self.user_input + "."
                    self.update_display(self.user_input)
                    self.is_result = False
                
            if press == "+/-":
                if self.is_result:
                    self.ans = str(-float(self.ans))
                    self.update_display(self.ans)
                else:
                    if self.user_input == "":
                        self.user_input = "0"
                    self.user_input = str(-float(self.user_input))
                    self.update_display(self.user_input)

            if press == "%":
                if self.is_result:
                    self.ans = str(float(self.ans)/100)
                    self.update_display(self.ans)
                else:
                    if self.user_input == "":
                        self.user_input = "0"
                    self.user_input = str(float(self.user_input)/100)
                    self.update_display(self.user_input)              

            if press == "=":
                if self.user_input == "":
                    self.user_input = self.last_user_input
                    if self.user_input == "":
                        self.user_input = self.ans
                try:
                    self.ans = self.calculation(self.ans, self.user_input, self.operator)
                    self.last_user_input = self.user_input
                    self.user_input = ""
                    self.update_display(self.ans)
                    self.ever_equals = True
                    self.is_result = True
                    self.true_equal = True
                except:
                    self.update_display("Error")
            

if __name__ == "__main__":
    root = tkinter.Tk()
    Calculator(root)
    root.mainloop()
