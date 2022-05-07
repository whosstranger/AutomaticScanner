import sys, pyfiglet, csv, wfuzz, signal, nmap, os, time

def def_handler(sig, frame):
    print("\n\n[!] Going out...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

#Banner
banner = pyfiglet.figlet_format("Automatic Scanner", width = 200, font = "ogre")
print(banner)

#Choose the option
print("""Choose One:
        1 - Scan ports.
        2 - Scan services.
        3 - Fuzzing.
        4 - Help.
        """)
option = input("Place the option: ")

ep = nmap.PortScanner()

if option == "1": #Scan ports        
    ip = input("Place the IP: ")
    print("\n Scanning... \n") 
    ep.scan(hosts = ip, arguments = '-p- --open --min-rate 5000 -n -Pn')
    print("Command executed: " + ep.command_line() + '\n') #Showing the command
    for host in ep.all_hosts():
        for proto in ep[host].all_protocols():
            lport = ep[host][proto].keys()
            sorted(lport)
            for port in lport:
                print("-----------------------")
                print ('Port: %s  State: %s' % (port, ep[host][proto][port]['state']))
                print("-----------------------")
    info = input("\nDo you want to safe the information? (y/n): ")
    if info == "y":
        with open("Ports.txt","w") as file:
            file.write("Port: " + str(port)) 
            file.write("   State: open")           
        print("Saved information")
    elif info == "n":
        print("\n [!] Going out...")
elif option == "2": #Services
    a = input("Place the IP: ")
    print("\n Scanning... \n")
    ep.scan(hosts = a, arguments = '-sCV -n -Pn')
    print("Command executed: " + ep.command_line() + '\n') #Showing the command
    print("Prueba")

elif option == "3": #Fuzzing
    print("\n Example: http://127.0.0.1/FUZZ - Dont forget FUZZ \n")
    z = input('Place the URL: ')
    url = input('Place the Directory: ')
    print("\n Scanning... \n")
    s = wfuzz.FuzzSession(url=z)
    for r in s.fuzz(hc=[404],t=[200],payloads=[("file",dict(fn=url))]):
        print(r)
    info = input("\n Do you want to safe the information? (y/n): ")
    if info == "y":
        with open("Fuzzing","w") as file:
            file.write(str(r))
        print("\n [!] Saved information")
    elif info =="n":
        print("\n [!] Going out...")
elif option == "4": #Help
    print("""Choose One:
                1 - nmap.
                2 - wfuzz. \n """)
    help = input("Which one do you need help?: " )
    if help == "1":
        print("""Quick and easy command: 
                    -p- --open: Search only open ports
                    --min-rate 5000: Number of sent threads
                    -n: Do not apply dns resolution
                    -Pn: Do not perform dns discovery
                    """)
    elif help == "2":
        print("""Quick and easy command:
                    hc: Dont show the status code.
                    hh: Hide characters
                    -w: Dictionary to fuzzing
                    -u: WebSite
                    """)

