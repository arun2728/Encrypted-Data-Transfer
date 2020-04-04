from cryptography.fernet import Fernet
from tkinter import *
import socket
from tkinter import messagebox
import os
import time

# sending text  ..................................................................................

def send_text():
    f = Fernet(key)
    token = f.encrypt(str.encode(post_cmd.get()))
    print(token)
    s.send(token)
    # s.send(key)

    posts.destroy()

# sending file --------------------------------------------

def send_file():
    global file_name
    global file_path
    print(file_name.get(),file_path.get())
    fd = os.open(file_path.get(),os.O_RDONLY)
    n = os.path.getsize(file_path.get())
    print(n)
    read_bytes = os.read(fd,n)
    print(read_bytes)
    data = "File"+file_name.get()+"^"+str(read_bytes,"utf-8")
    f = Fernet(key)
    token = f.encrypt(str.encode(data))
    s.send(token)
    posts.destroy()
# image transfer-----------

def send_image():
    global image_name
    global image_path
    f = Fernet(key)
    fd = os.open(image_path.get(), os.O_RDONLY)
    size = os.path.getsize(image_path.get())
    read_bytes = os.read(fd, size)
    token = f.encrypt(read_bytes)
    print(size)
    data = "Image"+str(size)+"^"+image_name.get()
    s.send(str.encode(data))
    time.sleep(2)
    s.send(token)
    posts.destroy()


def send_audio():
    global audio_name
    global audio_path
    f = Fernet(key)
    fd = os.open(audio_path.get(), os.O_RDONLY)
    size = os.path.getsize(audio_path.get())
    read_bytes = os.read(fd, size)
    token = f.encrypt(read_bytes)
    print(size)
    print(read_bytes)
    data = "Audio" + str(size) + "^" + audio_name.get()
    s.send(str.encode(data))
    time.sleep(2)
    s.send(read_bytes)
    print(token)
    print(len(token))
    posts.destroy()

# disconnect ..................................................................................
def disconnects():
    s.send(str.encode("Disconnect"))
    s.close()
    print('Disconnected to server...')
    root.destroy()


# Transfering Simple Text----------------------

def Text_transfer():
    global posts
    global post_cmd
    posts = Toplevel(root)
    posts.geometry('600x600')
    post_cmd = StringVar()
    Label(posts, text="Enter the message to send : ").place(x=40, y=50)
    Entry(posts, textvariable=post_cmd).place(x=250, y=50)
    Button(posts, text='Send', command=send_text, fg="green").place(x=400, y=100)
    posts.bind('<Return>', lambda  event = None : send_text())
    posts.mainloop()

# Transfering file ----------

def File_transfer():
    global posts
    global file_name
    global file_path
    posts = Toplevel(root)
    posts.geometry('600x600')
    file_name = StringVar()
    file_path = StringVar()
    Label(posts, text="Enter the File name : ").place(x=40, y=50)
    Entry(posts, textvariable=file_name).place(x=250, y=50)
    Label(posts, text="Enter the File path : ").place(x=40, y=100)
    Entry(posts, textvariable=file_path).place(x=250, y=100)
    Button(posts, text='Send', command=send_file, fg="green").place(x=300, y=150)
    posts.bind('<Return>', lambda event=None: send_file())
    posts.mainloop()

# IMage transfer ----------------

def Image_transfer():
    global posts
    global image_name
    global image_path
    posts = Toplevel(root)
    posts.geometry('600x600')
    image_name = StringVar()
    image_path = StringVar()
    Label(posts, text="Enter the Image name : ").place(x=40, y=50)
    Entry(posts, textvariable=image_name).place(x=250, y=50)
    Label(posts, text="Enter the Image path : ").place(x=40, y=100)
    Entry(posts, textvariable=image_path).place(x=250, y=100)
    Button(posts, text='Send', command=send_image, fg="green").place(x=300, y=150)
    posts.bind('<Return>', lambda event=None: send_image())
    posts.mainloop()

#--Audio transfer----------

def Audio_transfer():
    global posts
    global audio_name
    global audio_path
    posts = Toplevel(root)
    posts.geometry('600x600')
    audio_name = StringVar()
    audio_path = StringVar()
    Label(posts, text="Enter the Audio name : ").place(x=40, y=50)
    Entry(posts, textvariable=audio_name).place(x=250, y=50)
    Label(posts, text="Enter the Audio path : ").place(x=40, y=100)
    Entry(posts, textvariable=audio_path).place(x=250, y=100)
    Button(posts, text='Send', command=send_audio, fg="green").place(x=300, y=150)
    posts.bind('<Return>', lambda event=None: send_audio())
    posts.mainloop()

# connects ..................................................................................
def displays_conn():
    connec.destroy()
    print("IP address : ", ip_add.get(), "\nPort Number :", port_num.get())
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ip_add.get()
    port = port_num.get()
    s.connect((host, port))  # here we just connect the server
    messagebox.showinfo('Status', "Connection Established")
    s.send(key)


def connects():
    global connec
    global ip_add
    global port_num
    connec = Toplevel(root)
    connec.geometry('600x600')

    ip_add = StringVar()
    port_num = IntVar()

    Label(connec, text='Enter IP address : ').place(x=40, y=50)
    Entry(connec, textvariable=ip_add).place(x=250, y=50)

    Label(connec, text='Enter Port Number : ').place(x=40, y=150)
    Entry(connec, textvariable=port_num).place(x=250, y=150)

    Button(connec, text='Connect', command=displays_conn).place(x=400, y=100)
    connec.bind('<Return>', lambda event=None: displays_conn())
    connec.mainloop()


# menu ..................................................................................

def adjustWindow(window):
    w = 600  # width for the window size
    h = 600  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)  # calculate x and y coordinates for the Tk window
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(False, False)  # disabling the resize option for the window
    # window.configure(background='#174873') # making the background white of the window


# validate the entry data and makes a new entry into the database


def menu():
    global root
    global key
    key = Fernet.generate_key()

    # global s
    root = Tk()
    adjustWindow(root)
    Label(root, text="Encrypted Data Transfer System", width="500", height="2", font=("Calibri", 22, 'bold'), fg='white',
          bg='green').pack()
    Button(root, text='Connect', command=connects, fg="green").place(x=50, y=150)
    Button(root, text='Disconnect', command=disconnects, fg="red").place(x=250, y=150)
    Text_button = Button(root, text='Text Transfer', command=Text_transfer, fg="blue")
    Text_button.place(x=50, y=250)
    Button(root, text='File Transfer', command=File_transfer, fg="blue").place(x=250, y=250)
    Button(root, text='Image Transfer', command=Image_transfer, fg="blue").place(x=150, y=350)
    Button(root, text='Audio Transfer', command=Audio_transfer, fg="blue").place(x=300, y=350)

    root.bind('<Escape>', lambda event=None: root.destroy())
    root.mainloop()


menu()
