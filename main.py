import tkinter as tk
from tkinter import messagebox

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
        
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2)
        
        self.expenses_listbox = tk.Listbox(root, width=40)
        self.expenses_listbox.grid(row=3, column=0, columnspan=2)
            
    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        
        if amount and category:
            self.expenses_listbox.insert(tk.END, f"{category}: ${amount}")
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both amount and category")
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTracker(root)
    root.mainloop()