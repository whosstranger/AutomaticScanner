import sys, pyfiglet, csv, wfuzz, signal
import nmap

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
    print("Scanning...")
    ep.scan(hosts = ip, arguments = '-p- --open --min-rate 5000 -n -Pn')
    print("Command executed: " + ep.command_line()) #Showing the command
    for host in ep.all_hosts():
        for proto in ep[host].all_protocols():
            lport = ep[host][proto].keys()
            sorted(lport)
            for port in lport:
                print ('Port: %s  State: %s' % (port, ep[host][proto][port]['state']))
elif option == "2": #Services
    a = input("Place the IP: ")
    print("Scanning...")
    ep.scan(hosts = a, arguments = '-sCV -n -Pn')
    print("Command executed: " + ep.command_line()) #Showing the command
    print(ep.csv())

elif option == "3": #Fuzzing
    z = input('Place the URL: ')
    print("Example: http://127.0.0.1/FUZZ")
    for r in wfuzz.fuzz(url=z, hc=[404], payloads=[("file",dict(fn="/usr/share/wfuzz/wordlist/general/big.txt"))]):
        print(r)

elif option == "4": #Help
    print("""Choose One:
                1 - nmap.
                2 - wfuzz. """)
    help = input("Which one do you need help? ")
    if help == "1":
        print("""Quick and easy command: 
                    -p- --open: Search only open ports
                    --min-rate 5000: Number of sent threads
                    -n: Do not apply dns resolution
                    -Pn: Do not perform dns discovery
                    """)
