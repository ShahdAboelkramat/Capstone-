import socket
import threading
from tkinter import Tk, Text, Scrollbar, Button, END
from tkinter import *
import tkinter as tk



def start_server():
    def handle_client(client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                '''if message:
                    display_message(f"Client: {message}")
                else:
                    break'''
            except:
                break
        client_socket.close()

    def accept_connections():
        while True:
            client_socket, addr = server_socket.accept()
            #display_message(f"Connection established with {addr}")
            threading.Thread(target=handle_client, args=(client_socket,)).start()



    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    threading.Thread(target=accept_connections, daemon=True).start()

    #display_message("Server started and waiting for connections...")

# GUI Setup for Server
root=tk.Tk()
root.title("Server")

about = Frame(root, bg="lightblue")  
about.place(x=0, y=0, relwidth=1, relheight=1)  
text2 = Label(about, text="shahd", font=("Arial", 20), fg="black")
text2.place(x=50, y=100)


home = Frame(root, bg="lightgreen")
home.place(x=10, y=50, relwidth=1, relheight=1)

text1 = Label(home, text="Hello", font=("Arial", 20), fg="black")
text1.place(x=50, y=100)

button_frame = Frame(root, bg="gray")
button_frame.place(x=0, y=0, relwidth=1)


start_btn = Button(button_frame, text="Start Server", command=start_server)
start_btn.pack(side="left", padx=20, pady=20)

abo = Button(button_frame, text="About Us", command=lambda: about.tkraise())
abo.pack(side="left", padx=20, pady=20)


home_btn = Button(button_frame, text="Home", command=lambda: home.tkraise())
home_btn.pack(side="left", padx=20, pady=20)


home.tkraise()
root.mainloop()
