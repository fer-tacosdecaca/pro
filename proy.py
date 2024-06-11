from tkinter import *

a = Tk()
a.geometry("700x700")
a.title("proyecto")
ti = Label(a, text="iniciar cesion",font=20)
n = Label(a, text="Nombre:")
co = Label(a, text="Contraseña:")
ca = Label(a, text="Captcha:")
ti.place(relx=0.45, rely=0.1)
n.place(relx=0.3, rely=0.3)
co.place(relx=0.3, rely=0.4)
ca.place(relx=0.3, rely=0.5)


en = Entry(a)
con = Entry(a)
can = Entry(a)
en.place(relx=0.6, rely=0.3)
con.place(relx=0.6, rely=0.4)
can.place(relx=0.6, rely=0.5)

ba = Button(a,text="mostrar perfil")
ap = Button(a,text="actualizar perfil")
ba.place(relx=0.65, rely=0.7)
ap.place(relx=0.35, rely=0.7)



a.mainloop()
