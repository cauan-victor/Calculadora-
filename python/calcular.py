import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        
        self.entry = tk.Entry(self.master, width=20, font=("Arial", 16), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(self.master, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
