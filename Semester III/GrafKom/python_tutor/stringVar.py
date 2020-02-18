import tkinter as tk

class Var(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.trace("w", self.showMessage)
        self.entry = tk.Entry(self, textvariable=self.var)
        self.btn = tk.Button(self, text="Clear", command=lambda: self.var.set(""))
        self.label = tk.Label(self)
        self.entry.pack()
        self.btn.pack()
        self.label.pack()

    def showMessage(self, *args):
        value = self.var.get()
        text = "Hello, {}".format(value) if value else ""
        self.label.config(text=text)

if __name__ == "__main__":
    app = Var()
    app.mainloop()
