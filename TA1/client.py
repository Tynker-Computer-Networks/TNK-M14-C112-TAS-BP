import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))
print("Connected with the server...")

# Don't inherit Tk as we need to create multiple windows
class GUI(Tk):
    def __init__(self):
        # Remove as we need to make multiple windows
        super().__init__()
        
        # Create a window using Tk()
        
        # Call withdraw() method from window
        

        # Create a screen login using Toplevel
        

        # Set title part of login screen instead of self
        self.title("Login")
        
        # use login screen instead of self
        self.resizable(width=False, height=False)
        
        # use login screen instead of self
        self.configure(width=400, height=300)

        # Add label to login screen by pass screen as first parameter
        self.page_label = Label(text = "Please login to continue",
                                font = "Helvetica 14 bold")
        self.page_label.place(relx = 0.2, rely = 0.07)
        
        # Add Entry to login screen by pass screen as first parameter
        self.name_entry = Entry( font = "Helvetica 14")
        self.name_entry.place(relwidth = 0.4,
                            relheight = 0.12,
                            relx = 0.35,
                            rely = 0.2)
        self.name_entry.focus()

        # Add label to login screen by pass screen as first parameter
        self.name_label = Label(  text = "Name:",
                                font = "Helvetica 12")
        self.name_label.place(relx = 0.1, rely = 0.2)
        
        # Add Button to login screen by pass screen as first parameter
        self.login_button = Button(text = "Login",
                                  font = "Helvetica 14 bold",
                                  # Change login function to go_ahead
                                  command = lambda: self.login(self.name_entry.get()))
        self.login_button.place(relx = 0.4, rely = 0.55)

        # Start mainloop from window
        


    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                print(message)
            except Exception as e:
                print("An error occurred!", e)
                client.close()
                break
    # Change name of the method to go_ahead() 
    def login(self, name):
        self.name = name
        
        receive_thread = Thread(target=self.receive)
        receive_thread.start()

def write():
    while True:
        message = '{}: {}'.format("nickname", input(''))
        client.send(message.encode('utf-8'))

write_thread = Thread(target=write)
write_thread.start()


app = GUI()
# remove starting mainloop from object
app.mainloop()
