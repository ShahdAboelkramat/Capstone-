import socket
from tkinter import Tk, Text, Entry, Button, END

def connect_to_server():
    def send_message():
        message = message_entry.get()
        if message:
            client_socket.send(message.encode('utf-8'))
            display_message(f"You: {message}")
            message_entry.delete(0, END)

    def display_message(msg):
        text_area.config(state='normal')
        text_area.insert(END, msg + '\n')
        text_area.config(state='disabled')
        text_area.see(END)

    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    display_message("Connected to server.")
    send_button.config(command=send_message)

# GUI Setup for Client
root = Tk()
root.title("Client")
root.attributes('-fullscreen', True)

# Optional: Exit fullscreen with the "Escape" key
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

# Bind the "Escape" key to exit fullscreen
root.bind('<Escape>', exit_fullscreen)

text_area = Text(root, height=20, width=50, state='disabled')
text_area.pack()

message_entry = Entry(root, width=40)
message_entry.pack()

send_button = Button(root, text="Send")
send_button.pack()

connect_to_server()

root.mainloop()
