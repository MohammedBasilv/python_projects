from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os

# Create an instance of tkinter frame
win = Tk()
win.title("IMAGE ENCRYPTOR AND DECRYPTOR")
win.iconbitmap("./LOGO.ico")
win.configure(background="#4287f5")
win.attributes("-topmost", 1)

# Heading
heading = Label(win, text="Image Encryptor and Decryptor ", font="Impact 17 underline",background="#4287f5",fg="White",height=3)
heading.pack()
file_name = StringVar()
key = IntVar()  # Variable to store the encryption key
stored_key = None  # Variable to store the key used during encryption

# Set the geometry of tkinter frame
win.geometry("450x400")

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg *.jpeg *.png *.gif')])
    file_name.set(os.path.basename(file_path))
    return file_path

def encrypt():
    global file_path, stored_key
    path = file_path
    try:
        key_value = key.get()  # Get the key value from the text box
    except TclError:
        print("Invalid key value. Please enter an integer.")
        return

    # Store the key used for encryption
    stored_key = key_value

    # Print path of image file and encryption key that we are using
    print('The path of file : ', path)
    print('Key for encryption : ', key_value)

    # Open file for reading purpose
    with open(path, 'rb') as fin:
        # Storing image data in variable "image"
        image = fin.read()

    # Converting image into byte array to perform encryption easily on numeric data
    image = bytearray(image)

    # Performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key_value

    # Opening file for writing purpose
    with open(path, 'wb') as fout:
        # Writing encrypted data in image
        fout.write(image)

    # Clear the entry_key field after encryption
    entry_key.delete(0, END)

    messagebox.showinfo("Success", "Encryption Successful")

def decrypt():
    global file_path, stored_key
    path = file_path
    try:
        key_value = key.get()  # Get the key value from the text box
    except TclError:
        print("Invalid key value. Please enter an integer.")
        return

    # Check if the entered key matches the stored key
    if key_value != stored_key:
        messagebox.showerror("Invalid Key", "The key you entered is incorrect.")
        return

    # Print path of image file and decryption key that we are using
    print('The path of file : ', path)
    print('Key for decryption : ', key_value)

    # Open file for reading purpose
    with open(path, 'rb') as fin:
        # Storing image data in variable "image"
        image = fin.read()

    # Converting image into byte array to perform decryption easily on numeric data
    image = bytearray(image)

    # Performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key_value

    # Opening file for writing purpose
    with open(path, 'wb') as fout:
        # Writing decrypted data in image
        fout.write(image)

    # Clear the entry_key field after decryption
    entry_key.delete(0, END)

    messagebox.showinfo("Success", "Decryption Successful")

# Create the UI components

label = Label(win, text="Click the Button to browse the Files", font=('Georgia 10'),width=70, anchor=W ,background="#4287f5")

entry_file = Entry(win, textvariable=file_name, width=50)
label.pack(pady=8)
entry_file.pack(pady=8)

browse_button = ttk.Button(win, text="Browse", command=open_file)
browse_button.pack(pady=20)

key_label = Label(win, text="Enter Key for encryption of Image", font=('Georgia 10'),width=70, anchor=W,background="#4287f5")
key_label.pack(pady=10)
    
entry_key = Entry(win, textvariable=key, width=50, show="*")
entry_key.pack(pady=10)

# Clear the default "0" value from the key text box
entry_key.delete(0, END)

encrypt_button = Button(win, text="Encrypt",  command=encrypt, activebackground="blue" )
encrypt_button.pack(pady=10)

decript_button = Button(win, text="Decrypt",  command=decrypt, activebackground="blue")
decript_button.pack(pady=5)

# Run the application
win.mainloop()
