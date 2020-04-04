# Encrypted-Data-Transfer
Wireless Data transfer between two devices connected on same network. You can transfer text, files and images.
Encryption is used to secure the files.

## Prerequisites
### 1. Cryptography : 
   pip install cryptography (ignore if you already installed it). Link = "https://pypi.org/project/cryptography/"
 
### 2. Tkinter : 
   pip install python-tk (ignore if you already installed it)
       

## Execution  
Before running the files make sure that both the devices are connected on same network.
Sender.py is a GUI based application, run this on the device(from which data is to be transfered) exists.
Run Receiver.py on the device where data is to be stored.
Firstly establish a connection by clicking on ' connect ' on GUI and then :
  1. Enter IP Address of the device (where data is to be transfered)
  2. Enter port number 9998, you can change port number in Receiver.py
  3. Press Enter,
Now you can select option based on your file type
Finally, to disconnect from Reciver click disconnect.
#### Note : To transfer any file you need to enter complete file path including file name.
