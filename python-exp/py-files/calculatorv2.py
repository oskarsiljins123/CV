import tkinter as tk
field_text=""
def add_to_field(sth):
    global field_text
    field_text=field_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text)
def calculate():
    global field_text
    try:
        result=str(eval(field_text))
        field.delete("1.0","end")
        field.insert("1.0",result)
    except (SyntaxError, ZeroDivisionError, NameError):
        result="error"
        field.delete("1.0","end")
        field.insert("1.0",result)
def clear():
    global field_text
    field_text=""
    field.delete("1.0","end")
    field.delete("1.0","end")

window=tk.Tk()
window.geometry("300x300")
field=tk.Text(window,height=2,width=21,font=("monoscope",24))
field.grid(row=1,column=1,columnspan=4)

btn_1 = tk.Button(window,text="1",command=lambda: add_to_field(1),width=5,font=("monoscope",14))
btn_1.grid(row=4,column=1)

btn_2 = tk.Button(window,text="2",command=lambda: add_to_field(2),width=5,font=("monoscope",14))
btn_2.grid(row=4,column=2)

btn_3 = tk.Button(window,text="3",command=lambda: add_to_field(3),width=5,font=("monoscope",14))
btn_3.grid(row=4,column=3)

btn_4 = tk.Button(window,text="4",command=lambda: add_to_field(4),width=5,font=("monoscope",14))
btn_4.grid(row=3,column=1)

btn_5 = tk.Button(window,text="5",command=lambda: add_to_field(5),width=5,font=("monoscope",14))
btn_5.grid(row=3,column=2)

btn_6 = tk.Button(window,text="6",command=lambda: add_to_field(6),width=5,font=("monoscope",14))
btn_6.grid(row=3,column=3)

btn_7 = tk.Button(window,text="7",command=lambda: add_to_field(7),width=5,font=("monoscope",14))
btn_7.grid(row=2,column=1)


btn_8 = tk.Button(window,text="8",command=lambda: add_to_field(8),width=5,font=("monoscope",14))
btn_8.grid(row=2,column=2)

btn_9 = tk.Button(window,text="9",command=lambda: add_to_field(9),width=5,font=("monoscope",14))
btn_9.grid(row=2,column=3)

btn_0 = tk.Button(window,text="0",command=lambda: add_to_field(0),width=5,font=("monoscope",14))
btn_0.grid(row=5,column=1)

btn_dot = tk.Button(window,text=".",command=lambda: add_to_field("."),width=5,font=("monoscope",14))
btn_dot.grid(row=5,column=2)

btn_clear = tk.Button(window,text="C",command= clear,width=5,font=("monoscope",14))
btn_clear.grid(row=5,column=3)

btn_plus = tk.Button(window,text="+",command=lambda: add_to_field("+"),width=5,font=("monoscope",14))
btn_plus.grid(row=2,column=4)

btn_minus = tk.Button(window,text="-",command=lambda: add_to_field("-"),width=5,font=("monoscope",14))
btn_minus.grid(row=3,column=4)

btn_divide = tk.Button(window,text="/",command=lambda: add_to_field("/"),width=5,font=("monoscope",14))
btn_divide.grid(row=4,column=4)

btn_multiply = tk.Button(window,text="x",command=lambda: add_to_field("*"),width=5,font=("monoscope",14))
btn_multiply.grid(row=5,column=4)

btn_calc = tk.Button(window,text="=",command=calculate,width=5,font=("monoscope",14))
btn_calc.grid(row=6,column=1,columnspan=4)

window.mainloop()