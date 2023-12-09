from tkinter import *

calculation=""

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
def evaluvate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")
window = Tk()
window.title('Calculator')
window.geometry("300x275")
text_result = Text(window,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)
btn1=Button(master=window,text="1",command=lambda: add_calculation(1),width=5,font=("Arial",14))
btn1.grid(row=2,column=1)
btn2=Button(master=window,text="2",command=lambda: add_calculation(2),width=5,font=("Arial",14))
btn2.grid(row=2,column=2)
btn3=Button(master=window,text="3",command=lambda: add_calculation(3),width=5,font=("Arial",14))
btn3.grid(row=2,column=3)
btn4=Button(master=window,text="4",command=lambda: add_calculation(4),width=5,font=("Arial",14))
btn4.grid(row=3,column=1)
btn5=Button(master=window,text="5",command=lambda: add_calculation(5),width=5,font=("Arial",14))
btn5.grid(row=3,column=2)
btn6=Button(master=window,text="6",command=lambda: add_calculation(6),width=5,font=("Arial",14))
btn6.grid(row=3,column=3)
btn7=Button(master=window,text="7",command=lambda: add_calculation(7),width=5,font=("Arial",14))
btn7.grid(row=4,column=1)
btn8=Button(master=window,text="8",command=lambda: add_calculation(8),width=5,font=("Arial",14))
btn8.grid(row=4,column=2)
btn9=Button(master=window,text="9",command=lambda: add_calculation(9),width=5,font=("Arial",14))
btn9.grid(row=4,column=3)
btn0=Button(master=window,text="0",command=lambda: add_calculation(0),width=5,font=("Arial",14))
btn0.grid(row=5,column=2)
btn_plus=Button(master=window,text="+",command=lambda: add_calculation("+"),width=5,font=("Arial",14))
btn_plus.grid(row=2,column=4)
btn_minus=Button(master=window,text="-",command=lambda: add_calculation("-"),width=5,font=("Arial",14))
btn_minus.grid(row=3,column=4)
btn_multi=Button(master=window,text="*",command=lambda: add_calculation("*"),width=5,font=("Arial",14))
btn_multi.grid(row=4,column=4)
btn_div=Button(master=window,text="/",command=lambda: add_calculation("/"),width=5,font=("Arial",14))
btn_div.grid(row=5,column=4)
btn_open=Button(master=window,text="(",command=lambda: add_calculation("("),width=5,font=("Arial",14))
btn_open.grid(row=5,column=1)
btn_close=Button(master=window,text=")",command=lambda: add_calculation(")"),width=5,font=("Arial",14))
btn_close.grid(row=5,column=3)
btn_clear=Button(master=window,text="C",command=clear_field,width=11,font=("Arial",14))
btn_clear.grid(row=6,column=1,columnspan=2)
btn_equals=Button(master=window,text="=",command=evaluvate_calculation,width=11,font=("Arial",14))
btn_equals.grid(row=6,column=3,columnspan=2)
window.mainloop()
