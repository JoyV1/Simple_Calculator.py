import tkinter as tk

the_creation_of_screen = tk.Tk()
the_creation_of_screen.title("calculator")
the_creation_of_screen.resizable(False,False)

the_screen_text = tk.StringVar(value="")

the_screen_text_display = tk.Entry(
    the_creation_of_screen,
    textvariable=the_screen_text,
    font=("arial", 28),
    bd=0,
    justify="right",
)
the_screen_text_display.grid(row=0, column=0, columnspan=4, sticky="nswe", ipady=12) 

the_creation_of_screen.bind('<Return>', lambda e: displaying_the_answer())
the_creation_of_screen.bind('<BackSpace>', lambda e: delete_the_last_character())

the_screen_text_display.configure(validate="key", validatecommand=(the_creation_of_screen.register(lambda char: char in "0123456789+-x÷.%="), "%S"))

def clear_the_screen():
    the_screen_text.set("")

def delete_the_last_character():
    the_screen_text.set(the_screen_text.get()[:-1])

def converting_the_symbols(symbols):
    return symbols.replace("x", "*").replace("÷", "/")

def rounding_the_number(number):
    return int(number) if number == int(number) else number

def the_new_value_on_the_screen(new_value):
    the_screen_text.set(the_screen_text.get() + new_value)

def displaying_the_answer():
    try:
        the_answer = eval(converting_the_symbols(the_screen_text.get()))
        the_screen_text.set(str(rounding_the_number(the_answer)))
    except:
        the_screen_text.set("Error")

def change_the_signs():
    the_number_on_the_screen = the_screen_text.get()
    if the_number_on_the_screen:
        if the_number_on_the_screen.startswith("-"):
            the_screen_text.set(the_number_on_the_screen[1:])
        else:
            the_screen_text.set("-" + the_number_on_the_screen)

def taking_percentages():
    try:
        the_answer = eval(converting_the_symbols(the_screen_text.get())) / 100
        the_screen_text.set(str(rounding_the_number(the_answer)))
    except:
        the_screen_text.set("Error")

creation_of_the_buttons = [
    ("AC", clear_the_screen), ("DEL", delete_the_last_character), ("%", taking_percentages), ("÷", lambda: the_new_value_on_the_screen("÷")),
    ("7", lambda: the_new_value_on_the_screen("7")), ("8", lambda: the_new_value_on_the_screen("8")), ("9", lambda: the_new_value_on_the_screen("9")), ("x", lambda: the_new_value_on_the_screen("x")),
    ("4", lambda: the_new_value_on_the_screen("4")), ("5", lambda: the_new_value_on_the_screen("5")), ("6", lambda: the_new_value_on_the_screen("6")), ("-", lambda: the_new_value_on_the_screen("-")),
    ("1", lambda: the_new_value_on_the_screen("1")), ("2", lambda: the_new_value_on_the_screen("2")), ("3", lambda: the_new_value_on_the_screen("3")), ("+", lambda: the_new_value_on_the_screen("+")),
    ("±", change_the_signs), ("0", lambda: the_new_value_on_the_screen("0")), (".", lambda: the_new_value_on_the_screen(".")), ("=", displaying_the_answer),
]

the_row_number = 1
the_column_number = 0

for the_button_text, the_button_command in creation_of_the_buttons:
    the_button = tk.Button(
        the_creation_of_screen,
        text=the_button_text,
        font=("arial", 20),
        width=4,
        height=2,
        command=the_button_command,
        bd=0,
        relief="flat",
        activebackground="#e0e0e0",
        cursor="hand2",
    )
    
    the_button.bind("<Enter>", lambda e, b=the_button: b.configure(bg="#d0d0d0"))
    the_button.bind("<Leave>", lambda e, b=the_button: b.configure(bg="SystemButtonFace"))
  
    the_button.grid(row=the_row_number, column=the_column_number, sticky="nswe", padx=1, pady=1)
    
    the_column_number += 1
    if the_column_number > 3:
        the_column_number = 0
        the_row_number += 1

for i in range(4):
    the_creation_of_screen.columnconfigure(i, weight=1)
for i in range(6):
    the_creation_of_screen.rowconfigure(i, weight=1)


the_creation_of_screen.mainloop()
