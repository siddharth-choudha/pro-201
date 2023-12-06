from tkinter import *

def calculate_simple_interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())

    si = (p * r * t) / 100
    result_text.set(f"Simple Interest: {si}")

root = Tk()
root.title("Simple Interest Calculator")

principal_label = Label(root, text="Principal:")
principal_label.grid(row=0, column=0)
principal_entry = Entry(root)
principal_entry.grid(row=0, column=1)

rate_label = Label(root, text="Rate (%):")
rate_label.grid(row=1, column=0)
rate_entry = Entry(root)
rate_entry.grid(row=1, column=1)

time_label = Label(root, text="Time (years):")
time_label.grid(row=2, column=0)
time_entry = Entry(root)
time_entry.grid(row=2, column=1)

calculate_button = Button(root, text="Calculate", command=calculate_simple_interest)
calculate_button.grid(row=3, column=1)

result_text = StringVar()
result_label = Label(root, textvariable=result_text)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()