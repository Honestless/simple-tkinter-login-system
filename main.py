import tkinter as tk
from tkinter import messagebox
# import json

class LoginScreen:
    def __init__(self):
        # Main loop
        self.screen = tk.Tk()
        self.screen.geometry("300x250")
        self.screen.title("Login System 1.0")
        self.lbl1 = tk.Label(text="Login System 1.0", bg="grey", width="300", height="2", font=("Calibri", 13))
        self.lbl2 = tk.Label(text="")
        self.btn1 = tk.Button(text="Login", height="2", width="30", command=self.login)
        self.lbl3 = tk.Label(text="")
        self.btn2 = tk.Button(text="Register", height="2", width="30", command=self.registration_form)
        self.screen1 = None
        self.reg_email = None
        self.reg_first_name = None
        self.reg_last_name = None
        self.reg_password = None
        self.reg_password2 = None
        self.reg_email_label = None
        self.reg_entry_email = None
        self.reg_first_name_label = None
        self.reg_entry_first_name = None
        self.reg_last_name_label = None
        self.reg_entry_last_name = None
        self.reg_entry_username = None
        self.reg_password_label = None
        self.reg_entry_password = None
        self.reg_repeat_password_label = None
        self.reg_entry_repeat_password = None
        self.reg_register_btn = None
        # login
        self.screen2 = None
        self.email_login_label = None
        self.email_login = None
        self.password_login_label = None
        self.password_login = None
        self.login_label = None
        self.response = None
        self.email = None
        self.password = None
        self.login_btn = None
        self.login_state = False

    def loop(self):
        self.lbl1.pack()
        self.lbl2.pack()
        self.btn1.pack()
        self.lbl3.pack()
        self.btn2.pack()
        self.screen.mainloop()

    def login(self):
        self.screen2 = tk.Toplevel(self.screen)
        self.screen2.title("Login")
        self.screen2.geometry("300x300")
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.email_login_label = tk.Label(self.screen2, text="Email * ").pack()
        self.email_login = tk.Entry(self.screen2, textvariable=self.reg_email)
        self.email_login.pack()
        self.password_login_label = tk.Label(self.screen2, text="Password * ").pack()
        self.password_login = tk.Entry(self.screen2, textvariable=self.reg_password, show="*")
        self.password_login.pack()
        self.login_btn = tk.Button(self.screen2, padx=25, text="login", command=self.check_login).pack()

    def check_login(self):
        email = self.email_login.get()
        password = self.password_login.get()
        print(email)
        print(password)
        try:
            with open('users.txt', 'r') as usersFile:
                content = usersFile.readlines()
                for line in content:
                    editedLines = line.strip('\n').split(
                        ',')
                    print(editedLines)
                    if email == editedLines[0] and password == editedLines[1]:
                        messagebox.showinfo('SUCCESS', 'LOGGED IN!')
                        self.jump_to_app()

            messagebox.showerror('ERROR', 'INCORRECT LOGIN!')
            exit()

        except FileNotFoundError:
            messagebox.showerror('ERROR', 'USERS.TXT WAS NOT FOUND')
            exit()

    def registration_form(self):
        self.screen1 = tk.Toplevel(self.screen)
        self.screen1.title("Register")
        self.screen1.geometry("300x300")
        self.reg_email = tk.StringVar()
        self.reg_first_name = tk.StringVar()
        self.reg_last_name = tk.StringVar()
        self.reg_password = tk.StringVar()
        self.reg_password2 = tk.StringVar()
        self.reg_email_label = tk.Label(self.screen1, text="Email Address * ").pack()
        self.reg_entry_email = tk.Entry(self.screen1, textvariable=self.reg_email)
        self.reg_entry_email.pack()
        self.reg_first_name_label = tk.Label(self.screen1, text="First Name * ").pack()
        self.reg_entry_first_name = tk.Entry(self.screen1, textvariable=self.reg_first_name)
        self.reg_entry_first_name.pack()
        self.reg_last_name_label = tk.Label(self.screen1, text="Last Name * ").pack()
        self.reg_entry_last_name = tk.Entry(self.screen1, textvariable=self.reg_last_name)
        self.reg_entry_last_name.pack()
        self.reg_password_label = tk.Label(self.screen1, text="Password * ").pack()
        self.reg_entry_password = tk.Entry(self.screen1, textvariable=self.reg_password, show="*")
        self.reg_entry_password.pack()
        self.reg_repeat_password_label = tk.Label(self.screen1, text="Repeat Password * ").pack()
        self.reg_entry_repeat_password = tk.Entry(self.screen1, textvariable=self.reg_password2, show="*")
        self.reg_entry_repeat_password.pack()
        self.reg_register_btn = tk.Button(self.screen1, text="Register", command=self.register_user).pack()
        self.screen1.mainloop()

    def register_user(self):
        if self.reg_password.get() != self.reg_password2.get():
            self.response = messagebox.showinfo("Error", "Passwords doesn't match!")
        elif len(self.reg_entry_password.get()) < 7:
            self.response = messagebox.showinfo("Error", "Passwords must be at least 7 characters.")
        elif len(self.reg_entry_email.get()) < 1:
            self.box_not_filled()
        elif len(self.reg_first_name.get()) < 1:
            self.box_not_filled()
        elif len(self.reg_entry_last_name.get()) < 1:
            self.box_not_filled()
        else:
            file = open("users.txt", "a")
            file.write(self.reg_entry_email.get())
            file.write(",")
            file.write(self.reg_entry_password.get())
            file.write(",")
            file.write(self.reg_first_name.get())
            file.write(",")
            file.write(self.reg_entry_last_name.get())
            file.write("\n")
            file.close()
            self.confirm_registration()

    def confirm_registration(self):
        self.response = messagebox.showinfo("App name", "Your account has been created, please login.")
        self.screen1.destroy()

    def box_not_filled(self):
        self.response = messagebox.showinfo("Error", "Make sure to fill all fields marked with '*'")

    def jump_to_app(self):
        main_app.app()

class MainApp:
    def __init__(self):
        self.response = None
        self.main_screen = LoginScreen()

    def loop(self):
        self.main_screen.loop()

    def app(self):
        self.response = messagebox.showinfo("Error", "Make sure to fill all fields marked with '*'")

main_app = MainApp()
main_app.loop()
