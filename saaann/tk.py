import tkinter as tk



def login():
    username =e1.get()
    password = e2.get()

    if username == "admin" and password == "1234":
        msg=tk.Label(window, text="Login Successful")
        msg.pack()
    else:
        msg1= tk.Label(window, text="Login Failed")
        msg1.pack()


window = tk.Tk()
window.title("Login Window")
window.geometry("400x300")
l1= tk.Label(window, text="Username")
l1.pack()

e1= tk.Entry(window)
e1.pack()


l2= tk.Label(window, text="Password")
l2.pack()

e2= tk.Entry(window, show="*")
e2.pack()


b= tk.Button(window, text="Login", command=login)
b.pack()

window.mainloop()