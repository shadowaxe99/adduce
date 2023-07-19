```python
import tkinter as tk
from src import crm_system

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.crm_system = crm_system.CRMSystem()

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.signup_button = tk.Button(self.root, text="Signup", command=self.signup)

        self.deal_list = tk.Listbox(self.root)
        self.investor_list = tk.Listbox(self.root)
        self.company_list = tk.Listbox(self.root)

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        result = self.crm_system.login(username, password)
        if result:
            print("login_success")
        else:
            print("login_fail")

    def signup(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        result = self.crm_system.signup(username, password)
        if result:
            print("signup_success")
        else:
            print("signup_fail")

    def update_deal_list(self):
        self.deal_list.delete(0, tk.END)
        for deal in self.crm_system.get_deals():
            self.deal_list.insert(tk.END, deal)

    def update_investor_list(self):
        self.investor_list.delete(0, tk.END)
        for investor in self.crm_system.get_investors():
            self.investor_list.insert(tk.END, investor)

    def update_company_list(self):
        self.company_list.delete(0, tk.END)
        for company in self.crm_system.get_companies():
            self.company_list.insert(tk.END, company)

if __name__ == "__main__":
    root = tk.Tk()
    ui = UserInterface(root)
    root.mainloop()
```