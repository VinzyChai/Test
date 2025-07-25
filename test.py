import tkinter as tk

class CounterApp:
    def __init__(self, master):
        self.master = master
        self.counter = 1

        master.title("Counter 1-10")

        self.label = tk.Label(master, text=str(self.counter), font=("Helvetica", 32))
        self.label.pack(pady=20)

        button_frame = tk.Frame(master)
        button_frame.pack()

        self.minus_button = tk.Button(button_frame, text="-", font=("Helvetica", 20), width=5, command=self.decrease)
        self.minus_button.grid(row=0, column=0, padx=10)

        self.plus_button = tk.Button(button_frame, text="+", font=("Helvetica", 20), width=5, command=self.increase)
        self.plus_button.grid(row=0, column=1, padx=10)

    def increase(self):
        if self.counter < 10:
            self.counter += 1
            self.label.config(text=str(self.counter))

    def decrease(self):
        if self.counter > 1:
            self.counter -= 1
            self.label.config(text=str(self.counter))

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
