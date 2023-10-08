import os
import time
import psutil
def rambot():
    try:
        count=0;
        old_set = set(list(psutil.process_iter()))
        l=[]
        while True:
            count=count+1
            new_set = set(list(psutil.process_iter()))
            added = new_set
            for p in added:
                l.append( p.name())
                x=p.name()
                print(x)
                y=os.path.abspath(x)
                print(y)

            old_set = new_set
            time.sleep(0.1)
            if count>4:
                break
    except:
        pass
    for i in l:
        try:
            #os.system('taskkill /f /im '+i)
            #
            print(i)
        except:
            pass
rambot()
