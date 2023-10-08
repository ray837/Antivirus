import tkinter as tk
from tkinter import SUNKEN, filedialog
from FolderScan import folder_scanner
from JunkRemover import junk_remover
from rb import rambooster

from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("520x600")
window.title("Antivirus Software")
def show_frame(frame):
    frame.tkraise()

folder_path = tk.StringVar()



def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print("To SCAN:"+filename)
    folder_scanner(filename)




window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=100, weight=1)

frame1 = tk.Frame(window, bg="magenta2", relief=SUNKEN, width=100, height=200)
frm_buttons = tk.Frame(window, bg="DarkOrchid2", relief=tk.RAISED, bd=1)
frame1.grid(row=0, column=1)

# vframe
vframe = tk.Frame(window, bg="DarkOrchid2", relief=tk.RAISED, bd=1)
vbtn1 = tk.Button(vframe, text="Folder Scan", command=lambda: browse_button())
vbtn2 = tk.Button(vframe, text="Deep Scan", command=lambda: folder_scanner('C:\Program Files'))
vbtn_exit = tk.Button(vframe, text="Back", command=lambda: show_frame(frm_buttons))
vbtn1.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
vbtn2.grid(row=1, column=0, sticky="ew", padx=20, pady=20)
vbtn_exit.grid(row=2, column=0, sticky="ew", padx=20, pady=20)
vframe.grid(row=0, column=1)

# pframe
pframe = tk.Frame(window, bg="DarkOrchid2", relief=tk.RAISED, bd=1)
pbtn1 = tk.Button(pframe, text="Ram Booster", command=lambda: rambooster())
pbtn2 = tk.Button(pframe, text="Junk Cleaner", command=lambda: junk_remover())
pbtn_exit = tk.Button(pframe, text="Back", command=lambda: show_frame(frm_buttons))
pbtn1.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
pbtn2.grid(row=1, column=0, sticky="ew", padx=20, pady=20)
pbtn_exit.grid(row=2, column=0, sticky="ew", padx=20, pady=20)
pframe.grid(row=0, column=1)

for frame in (vframe, pframe):
    frame.grid(row=0, column=0, sticky='snew')

# Load the image
image = Image.open('forest2.png')
resized = image.resize((400, 600))
my_img = ImageTk.PhotoImage(resized)
img = ImageTk.PhotoImage(resized)
label = tk.Label(frame1, image=img)

btn_open = tk.Button(frm_buttons, text="Virus Scan", command=lambda: show_frame(vframe))
btn_save = tk.Button(frm_buttons, text="Performance ", command=lambda: show_frame(pframe))
btn_exit = tk.Button(frm_buttons, text="Exit", command=window.destroy)

btn_open.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
btn_save.grid(row=1, column=0, sticky="ew", padx=20, pady=20)
btn_exit.grid(row=2, column=0, sticky="ew", padx=20, pady=20)

frm_buttons.grid(row=0, column=0, sticky="ns")
label.grid(row=1, column=1)

show_frame(frm_buttons)

window.mainloop()
