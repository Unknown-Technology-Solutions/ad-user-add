from ldap3 import Server, Connection, ALL, NTLM
import tkinter as tk
#from tkinter import *
#from tkinter import ttk
import json

configuration = json.load(open("config.json","r"))

server = Server(configuration['SERVER'], get_info=ALL)
conn = Connection(server, user=configuration['DOMAIN']+"\\"+configuration['USERNAME'], password=configuration['PASSWORD'], authentication=NTLM, auto_bind=True)
if conn.start_tls == True:
    print("TLS STARTED")
#    print(conn)
else:
    print("TLS NOT STARTED")
#    print(conn)
print(conn.extend.standard.who_am_i())


window = tk.Tk()
window.title("Test")
button_widget = tk.Button(window,text="Test")
button_widget.pack()
tk.mainloop()