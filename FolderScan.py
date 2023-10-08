
from tkinter import *
from tkinter import ttk
from malwarecheck import *
from remove import *

virusName = []


def rm():
    for k in virusName:
        virusRemover(k)
        print("Removed virus")



def folder_scanner(path):
    global vframe, virusName
    global l1, btn
    root = Tk()
    root.geometry("400x100")
    root.title("Scanning")
    l1 = Label(root)


    pro = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='indeterminate')

    pro.pack(pady=20)
    dir_list = list()
    vb = Button(root, text="Terminate", command=lambda: root.destroy())
    vb.pack()
    for (dirpath, dirnames, filename) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filename]
    print("this", dir_list)
    if len(dir_list) == 0:
        dir_list.append(path)

    for i in dir_list:
        l1.destroy()
        a = i
        pro.start(10)
        l1 = Label(root, text=a)
        l1.pack(padx=10)
        l1.update()
        print("im here")
        if malwarechecker(i) != 0:
            virusName.append(i)
        print(i)

    if len(virusName) == 0:
        l1.destroy()
        l1 = Label(root, text="Your System is Safe from virus", foreground="Green")
        l1.pack()
        print("Your System is Safe from virus")
    else:
        l1.destroy()
        msg = "Virus Found at :" + virusName
        l1 = Label(root, text=msg, foreground="Red")
        l1.pack()

        print("Virus is at", virusName)
        btn = Button(vframe, text="Remove Virus", command=lambda: rm())

    root.mainloop()
