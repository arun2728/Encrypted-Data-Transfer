# Encrypted-Data-Transfer
Wireless Data transfer between two devices connected on same network. You can transfer text, files and images.
Encryption is used to secure the files.

## Prerequisites
### 1. Cryptography : 
   a. pip install cryptography  (ignore if you already installed it)
   b. https://pypi.org/project/cryptography/

### 2. Tkinter : 
   pip install python-tk (ignore if you already installed it)
       

## Execution
1.Before running the files make sure that both the devices are connected on same network.
2. Sender.py is a GUI based application, run this on the device(from which data is to be transfered) exists.
3. Run Receiver.py on the device where data is to be stored.
4.Firstly establish a connection by clicking on ' connect ' on GUI and then :
  a. Enter IP Address of the device (where data is to be transfered)
  b. Enter port number 9998, you can change port number in Receiver.py
  c. Press Enter
5. Now you can select option based on your file type
6. Finally, to disconnect from Reciver click disconnect.
#### Note : To transfer any file you need to enter complete file path including file name.
