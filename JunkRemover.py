import os

def junk_remover():

        list1=[]
        for (dirpath,dirname,filenames) in os.walk(r"C:\Users\rayid\AppData\Local\Temp"):
            list1+=[os.path.join(dirpath,file) for file in filenames]
        for (dirpath,dirname,filenames) in os.walk(r"C:\Windows\Temp"):
            list1+=[os.path.join(dirpath,file) for file in filenames]
        for (dirpath,dirname,filenames) in os.walk(r"C:\Windows\Prefetch"):
            list1+=[os.path.join(dirpath,file) for file in filenames]
        print(list1)
        if list1:
            for i in list1:
                try:
                    os.remove(i)
                    print("removed"+i)
                except:
                    print("here")
                    pass
            print("SYSTEM CLEANED")
        else:
            print("Already cleared cache")


