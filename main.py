import json
from ldap3.core import exceptions
from ldap3 import Server, Connection, ALL, NTLM
# import tkinter as tk
from tkinter import messagebox
from tkinter import *
window = Tk()
# from tkinter import ttk

configuration = json.load(open("config.json", "r"))

server = Server(configuration['SERVER'], get_info=ALL)
# conn = Connection(server, user=configuration['DOMAIN']+"\\"+configuration['USERNAME'],
#                  password=configuration['PASSWORD'], authentication=NTLM, auto_bind=True)
conn = None
# if conn.start_tls == True:
#    print("TLS STARTED")
#    print(conn)
# else:
#    print("TLS NOT STARTED")
#    print(conn)
# print(conn.extend.standard.who_am_i())


lun_var = StringVar()
lpw_var = StringVar()


def submit():
    try:
        name = lun_var.get()
        password = lpw_var.get()

        print("The name is : " + name)
        print("The password is : " + password)
        print("Working...")
        conn = Connection(server, user=configuration['DOMAIN']+"\\"+name,
                          password=password, authentication=NTLM)
        if not conn.bind():
             print('Unable to authenticate: ', conn.result)
             raise exceptions.LDAPInvalidCredentialsResult
        else:
            print("Authenticated!")
    except exceptions.LDAPSocketOpenError:
        messagebox.showinfo(message="Cannot access AD Server!")
    except exceptions.LDAPUnknownAuthenticationMethodError:
        messagebox.showinfo(message="You must enter a username and password!")
    except exceptions.LDAPInvalidCredentialsResult:
        messagebox.showinfo(message="Invalid Credentials!")


#    lun_var.set("")
#    lpw_var.set("")


window.title("Login")
window.geometry("200x100")
window.resizable(width=False, height=False)
# frm_entry = tk.Frame(master=window)

login_username = Entry(master=window, textvariable=lun_var, width=12)
lbl_lun = Label(master=window, text="USERNAME")
login_password = Entry(
    master=window, textvariable=lpw_var, width=12, show="*")
lbl_lpw = Label(master=window, text="PASSWORD")

sub_btn = Button(window, text='Login', command=submit)

login_username.grid(row=0, column=0)
lbl_lun.grid(row=0, column=1)
login_password.grid(row=1, column=0)
lbl_lpw.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)


# window.grid(row=0, column=0, padx=10)
# button_widget = tk.Button(window, text="Login")
# button_widget.pack()
mainloop()
