import tkinter as tk

def submit():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    course = course_entry.get()
    address = address_text.get("1.0",tk.END)

    print("Student Registration Details")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Course:", course)
    print("Address:", address)

# Main window
window = tk.Tk()
window.title("Student Registration Form")
window.geometry("400x400")

title = tk.Label(window, text="Student Registration Form", font=("Arial", 14))
title.pack(pady=10)

name_label = tk.Label(window, text="Name")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Age")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender")
gender_label.pack()

gender_var = tk.StringVar()
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").pack()

course_label = tk.Label(window, text="Course")
course_label.pack()
course_entry = tk.Entry(window)
course_entry.pack()

address_label = tk.Label(window, text="Address")
address_label.pack()
address_text = tk.Text(window, height=3, width=30)
address_text.pack()

submit_btn = tk.Button(window, text="Submit", command=submit)
submit_btn.pack(pady=10)

window.mainloop()