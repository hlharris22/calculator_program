#######################################
## Hunter's Small Calculator Program ##
## version 1.0                       ##
#######################################

"""Future functionality
-Restrict all keyboard presses except for numbers and operators
-Allow user to clr char at cursor (index -1)
-add ability to work with fractions
-Change colors, sizing and formatting
-Allow user to change the theme of calculator window (pokemon!)
-Restrict resizing of the window
-Store history of calculations in an excel file
-create an .exe for the program
Testing changes
Testing changes 2
Fetch Testing"""


import tkinter as tk
from settings import Settings


class HuntersCalculator:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.settings = Settings()

        # Entry Widget
        self.entry = tk.Entry(self.frame, bd=15)
        self.entry.grid(row=1, column=1, columnspan=4, sticky=tk.W + tk.E)

        self.frame.pack(expand=True, fill='both')

        """Mathematical Operation Buttons"""
        # Addition button
        button_plus = tk.Button(self.frame,
                                text='+',
                                font="Verdana 19 bold",
                                width=self.settings.button_width,
                                height=self.settings.button_height,
                                command=self.addition)
        button_plus.grid(row=3, column=4)

        # Subtraction button
        self.button_minus = tk.Button(self.frame,
                                      text='-',
                                      font="Verdana 19 bold",
                                      width=self.settings.button_width,
                                      height=self.settings.button_height,
                                      command=self.subtraction)
        self.button_minus.grid(row=4, column=4)

        # Division Button
        self.button_division = tk.Button(self.frame,
                                         text='/',
                                         font="Verdana 19 bold",
                                         width=self.settings.button_width,
                                         height=self.settings.button_height,
                                         command=self.division)
        self.button_division.grid(row=6, column=4)

        # Multiplication Button
        self.button_multiplication = tk.Button(self.frame,
                                               text='*',
                                               font="Verdana 19 bold",
                                               width=self.settings.button_width,
                                               height=self.settings.button_height,
                                               command=self.multiplication)
        self.button_multiplication.grid(row=5, column=4)

        # Equals Button
        self.button_equals = tk.Button(self.frame,
                                       text='=',
                                       font="Verdana 19 bold",
                                       width=self.settings.button_width,
                                       height=self.settings.button_height,
                                       command=self.equals)
        self.button_equals.grid(row=6, column=3)

        # Decimal Button
        self.button_decimal = tk.Button(self.frame,
                                        text='.',
                                        font="Verdana 19 bold",
                                        width=self.settings.button_width,
                                        height=self.settings.button_height,
                                        command=self.decimal)
        self.button_decimal.grid(row=6, column=2)

        # Clear Button
        button_clear = tk.Button(self.frame,
                                 text='clr',
                                 font="Verdana 19 bold",
                                 width=self.settings.button_width,
                                 height=self.settings.button_height,
                                 command=self.clear)
        button_clear.grid(row=2, column=4)

        """Number Buttons"""

        # 0 Button
        self.button_0 = tk.Button(self.frame,
                                  text='0',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "0"))
        self.button_0.grid(row=6, column=1)

        # 1 Button
        self.button_1 = tk.Button(self.frame,
                                  text='1',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "1"))
        self.button_1.grid(row=5, column=3)

        # 2 Button
        self.button_2 = tk.Button(self.frame,
                                  text='2',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "2"))
        self.button_2.grid(row=5, column=2)

        # 3 Button
        self.button_3 = tk.Button(self.frame,
                                  text='3',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "3"))
        self.button_3.grid(row=5, column=1)

        # 4 Button
        self.button_4 = tk.Button(self.frame,
                                  text='4',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "4"))
        self.button_4.grid(row=4, column=3)

        # 5 Button
        self.button_5 = tk.Button(self.frame,
                                  text='5',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "5"))
        self.button_5.grid(row=4, column=2)

        # 6 Button
        self.button_6 = tk.Button(self.frame,
                                  text='6',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "6"))
        self.button_6.grid(row=4, column=1)

        # Decimal 7
        self.button_7 = tk.Button(self.frame,
                                  text='7',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "7"))
        self.button_7.grid(row=3, column=3)

        # 8 Button
        self.button_8 = tk.Button(self.frame,
                                  text='8',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "8"))
        self.button_8.grid(row=3, column=2)

        # 9 Button
        self.button_9 = tk.Button(self.frame,
                                  text='9',
                                  font="Verdana 19 bold",
                                  width=self.settings.button_width,
                                  height=self.settings.button_height,
                                  command=lambda: self.entry.insert(self.entry.index("insert"), "9"))
        self.button_9.grid(row=3, column=1)

    """Functions defining the actions occurring during button presses"""

    # Function defining the actions occurring when the "+" button is pressed
    def addition(self):
        self.entry.insert(self.entry.index("insert"), "+")

    # Function defining the actions occurring when the "-" button is pressed
    def subtraction(self):
        self.entry.insert(self.entry.index("insert"), "-")

    # Function defining the actions occurring when the "/" button is pressed
    def division(self):
        self.entry.insert(self.entry.index("insert"), "/")

    # Function defining the actions occurring when the "*" button is pressed
    def multiplication(self):
        self.entry.insert(self.entry.index("insert"), "*")

    # Function defining the actions occurring when the "=" button is pressed
    def equals(self):
        calculation_string = "".join([i for i in self.entry.get() if not i.isalpha()])
        print(eval(calculation_string))
        self.entry.delete(first=0, last="end")
        self.entry.insert(0, eval(calculation_string))

    # Function defining the actions occurring when the "." button is pressed
    def decimal(self):
        self.entry.insert(self.entry.index("insert"), ".")

    # Function defining the actions occurring when the "clr" button is pressed
    def clear(self):
        if self.entry.selection_present():
            self.entry.delete(first=self.entry.index("sel.first"), last=self.entry.index("sel.last"))
        else:
            self.entry.delete(first=int(len(self.entry.get()) - 1), last=None)



def main():
    root = tk.Tk()
    app = HuntersCalculator(root)
    root.wm_title("Hunter's Calculator")
    root.mainloop()


if __name__ == '__main__':
    main()
