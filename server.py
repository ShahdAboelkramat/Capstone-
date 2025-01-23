import socket
import threading
from tkinter import Tk, Text, Scrollbar, Button, END
from tkinter import *


def start_server():
    def handle_client(client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    display_message(f"Client: {message}")
                else:
                    break
            except:
                break
        client_socket.close()

    def accept_connections():
        while True:
            client_socket, addr = server_socket.accept()
            display_message(f"Connection established with {addr}")
            threading.Thread(target=handle_client, args=(client_socket,)).start()

    def display_message(msg):
        text_area.config(state='normal')
        text_area.insert(END, msg + '\n')
        text_area.config(state='disabled')
        text_area.see(END)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    threading.Thread(target=accept_connections, daemon=True).start()

    display_message("Server started and waiting for connections...")

# GUI Setup for Server
root = Tk()
root.title("Server")


root.attributes('-fullscreen', True)

# Optional: Exit fullscreen with the "Escape" key
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

# Bind the "Escape" key to exit fullscreen
root.bind('<Escape>', exit_fullscreen)

#text_area = Text(root, height=20, width=50, state='disabled')
#text_area.pack(side='left', fill='y')

#scrollbar = Scrollbar(root, command=text_area.yview)
#scrollbar.pack(side='right', fill='y')

#text_area['yscrollcommand'] = scrollbar.set

Button(root, text="Start Server", command=start_server).pack()

root.mainloop()
