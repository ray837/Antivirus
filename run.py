from JunkRemover import junk_remover
from rb import rambooster

print('''

░█▀▄▀█ ░█──░█ 　 ─█▀▀█ ░█▄─░█ ▀▀█▀▀ ▀█▀ ░█──░█ ▀█▀ ░█▀▀█ ░█─░█ ░█▀▀▀█ 　 　 ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀ ▀▀█▀▀ ░█──░█ ─█▀▀█ ░█▀▀█ ░█▀▀▀ 
░█░█░█ ░█▄▄▄█ 　 ░█▄▄█ ░█░█░█ ─░█── ░█─ ─░█░█─ ░█─ ░█▄▄▀ ░█─░█ ─▀▀▀▄▄ 　 　 ─▀▀▀▄▄ ░█──░█ ░█▀▀▀ ─░█── ░█░█░█ ░█▄▄█ ░█▄▄▀ ░█▀▀▀ 
░█──░█ ──░█── 　 ░█─░█ ░█──▀█ ─░█── ▄█▄ ──▀▄▀─ ▄█▄ ░█─░█ ─▀▄▄▀ ░█▄▄▄█ 　 　 ░█▄▄▄█ ░█▄▄▄█ ░█─── ─░█── ░█▄▀▄█ ░█─░█ ░█─░█ ░█▄▄▄  
                                                                                                                ''')
from FolderScan import folder_scanner, virusName

while (True):
    print("\n1. FOLDER/FILE SCANNING\n2.DEEP SCANNING\n3. Junk File Remover\n 4.Ram Booster\n0.EXIT")
    n = int(input(""))
    if n == 1 :
        p = input(r"enter your Path to scan")
        folder_scanner(p)
    if  n == 2:
        folder_scanner('C:\Program Files')
    if n==3:
        junk_remover()
    if n==4:
        rambooster()
    else:
        print("THANKING FOR USING MY ANTIVIRUS SOFTWARE")
        break
