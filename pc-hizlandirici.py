import os
from time import sleep
os.system("color a")
os.system("cls")
print("YONETICI OLARAK CALISITIR")
username = input("Oturumunuzun Kullanici Adi : ")
print("SILINECEK DOSYALAR LISTLENIYOR  !!!")
sleep(2)
os.system("clear")
os.system("cd C:/$Recycle.Bin/S-1-5-21-3278290568-885335064-1029729800-1001 && ls")
os.system("cd C:/Windows/temp && ls")
os.system("cd C:/Users/" + (username) + "/Recent && ls")
os.system("cd C:/Users/" + (username) + "/AppData/Local/Temp && ls")
os.system("cd C:/Users/" + (username) + "/AppData/Roaming/Microsoft/Windows/Recent && ls")

print("""




Sil=1 Silme=0 : """)
soru = input("Seciminizi Girin  :  ")

if int(soru) ==1:
    os.system("cd C:/Intel/Logs && rm -rf *")
    os.system("cd C:/$Recycle.Bin/S-1-5-21-3278290568-885335064-1029729800-1001 && rm -rf *")
    os.system("cd C:/Windows/temp && rm -rf *")
    os.system("cd C:/Users/" + (username) + "/Recent && rm -rf *")
    os.system("cd C:/Users/" + (username) + "/AppData/Local/Temp && rm -rf *")
    os.system("cd C:/Users/" + (username) + "/AppData/Roaming/Microsoft/Windows/Recent && rm -rf *")
else:
    print("BAY BAY")
