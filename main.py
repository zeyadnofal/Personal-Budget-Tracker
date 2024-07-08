import tkinter as tk
from tkinter import StringVar, messagebox

class BudgetTracker:
    def __init__(self, root) -> None:
        #initialize UI
        self.root = root
        self.root.title("Personal Budget Tracker")
        
        #create UI elements
        self.amount_label = tk.Label(root, text="Amount: ")
        self.amount_label.grid(row=0, column=0)
        
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)
        
        self.category_label = tk.Label(root, text="Category: ")
        self.category_label.grid(row=1, column=0)
        
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)
        
        self.type_label = tk.Label(root, text="Type: ")
        self.type_label.grid(row=2, column=0)

        options = ["Expense", "Income"]
        self.variable = StringVar(root)
        self.type_entry = tk.OptionMenu(root, self.variable, *options)
        self.type_entry.grid(row=2, column=1)
        
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=0, columnspan=2)
        
        self.expenses_listbox = tk.Listbox(root, width=40)
        self.expenses_listbox.grid(row=4, column=0, columnspan=2)
        
        self.delete_button = tk.Button(root, text="Delete Expense", command=self.delete_expense)
        self.delete_button.grid(row=5, column=0, columnspan=2)

    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        type = self.variable.get()
        
        if amount and category and type:
            self.expenses_listbox.insert(tk.END, f"{category}: ${amount} | {type}")
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both amount and category")
    
    def delete_expense(self):
        if self.expenses_listbox.curselection() == ():
            messagebox.showwarning("Error", "There are no entries to delete")

        else:
            self.expenses_listbox.delete(self.expenses_listbox.curselection())

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTracker(root)
    root.mainloop()