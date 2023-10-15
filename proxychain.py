import socket
import os 
import subprocess
inputFolderName = "inputProxy.txt"
outputFolderName = "outputProxy.txt"

print("__________________________________________")
os.system("figlet Proxy Chain Checker")
print("__________________________________________\n")

timeoutLimit = """"

0.1 _ Fast / Low Reliability (68/300)
1.0 _ Medium / Considered Reliable (100/300)
5.0 _ Slow / High Reliability - Useless (150/300)

[!]: 0.5 is okey.
[!]: Enter a value between 0.1 - 5

Enter a timeout limit :  """

x = float(input(timeoutLimit))

def connection(ip, port):

    try:
        with socket.create_connection((ip, port), timeout=x):
            return True

    except:
        return False

working_list = []
not_working_list = []

try:
    with open(inputFolderName, "r") as file:

        for line in file:
            ip, port = line.strip().split(":")
            port = int(port)  # port değerini integer'a dönüştür
            parts = ip, port
            
            if connection(ip, port):
                working_list.append(parts)
                print(f"[+] Working {ip}:{port}")
            else:
                not_working_list.append(parts)
                print(f"[-] Not Working {ip}:{port}")

except :

    print(f"[*] There is no file named {inputFolderName}")

with open(outputFolderName,"a") as config :

    for ip,port in working_list:

        config.write(f"{ip}:{port}\n")

print("\n\n")
print("__________________________________________")
print(f"[*] All the working proxy nodes saved in {outputFolderName}")
print("__________________________________________")
