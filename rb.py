import os
import time
import psutil


def rambooster():
    try:
        l=[]
        old_set = set(list(psutil.process_iter()))

        for i in old_set:
             l.append(i.name())
        print(l)
        for i in l:
          if i in['brave.exe','msedge.exe','chrome.exe','OneDrive.exe','Spotify.exe','mcafee-security.exe','EpicGamesLauncher.exe']:
             try:
               os.system('taskkill /f /im ' + i)
             except:
                  print("here")
                  pass
    except:
         pass




