# Automatic Scanner
<h1 align="center">
  <img src="https://github.com/whosstranger/Scanner/blob/master/Images/Scanner.gif" alt="WhosStranger" />
</h1>
   
## Hey! 👋

I have created this script which allows to perform all the reconnaissance phase on CTF machines, it contains the nmap tool and wfuzz.

-Nmap is used for open port and port-associated services reconnaissance.

-Wfuzz is used to discover hidden routes in web sites.

## Usage 🔎:

Assign execution permissions.

```sh
chmod +x AutomaticScanner.py
```

Script execution.

```sh
python3 Scanner.py 127.0.0.1
```
You can choose 4 different options.
  1. Scan Ports.
  2. Scan Services.
  3. Fuzzing.
  4. Help.

Selection 1. 🕵️‍♂️
```sh
Place the ip: 127.0.0.1
```
When the IP address is sent, the nmap tool will start scanning the open ports of the sent IP. At the end of the scan it will display the open ports of the services and ask if you want to save the information obtained.

If the answer is "Y" the information will be saved in the current directory.

Selection 2. 🕵️‍♂️
```sh 
Place the ip: 127.0.0.1
```

When the IP address is sent, the nmap tool will start scanning the services on each port and print the results on the screen. At the end of the service scan it will ask if you want to save the information.

If the answer is "Y" the information will be saved in the current directory.

Selection 3. 🕵️‍♂️ 
```sh 
Place the URL: http://127.0.0.1/FUZZ 
``` 
You must attach the URL and the word FUZZ where you want to make the scan.

```sh 
Place the Directory: /home/stranger/Documents/SecLists/Fuzzing/LDAP.Fuzzing.txt
```
When you have added the URL with the word FUZZ, you must attach the path where the dictionaries are located to perform the search.

If you do not know where to find these dictionaries, I attach a repository in which there are several fuzzing dictionaries.

```
https://github.com/danielmiessler/SecLists
```

When the scan is finished you will be asked if you want to save the information.

When you say "Y" it will save to the current address.

Selection 4. 🕵️‍♂️

The last option is to give an explanation of how each tool is configured.
