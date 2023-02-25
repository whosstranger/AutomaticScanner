#!/bin/bash

#Author: WhosStranger

#Colors
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

echo -e "\n${yellowColour}[!]${endColour} ${turquoiseColour}By WhosStranger${endColour}"

trap ctrl_c INT

function ctrl_c(){
	echo -e "\n${yellowColour}[*]${endColour} ${purpleColour}Leaving...${endColour}"
	exit 0
}

function tools(){
 
  dependecies=(nmap ffuf)
  echo -e "\n${yellowColour}[!]${endColour} ${purpleColour}Checking necessary tools${endColour}" 
  
  for program in "${dependecies[@]}"; do
    echo -ne "\n${yellowColour}[+]${endColour} ${blueColour}Tool${endColour} ${purpleColour}$program...${endColour}"

    test -f /usr/bin/$program #Which
    
    if [ "$(echo $?)" == "0" ];then
      echo -e "${greenColour}(V)${endColour}"
    else
      echo -e "${redColour}(X)${endColour}"
      echo -e "\n${yellowColour}[!]${endColour} ${blueColour}Installing the tool${endColour} ${purpleColour}$program...${endColour}"
      apt install $program -y > /dev/null 2>&1
      sleep 1
      echo -e "\n${yellowColour}[!]${endColour} ${blueColour}Successfully installed tool.${endColour}"
    fi;sleep 1
  done
}

function scan(){
  sleep 1; clear
  echo -e "\n${yellowColour}[-]${endColour} ${blueColour}Nmap = ${endColour}${purpleColour}n${endColour}"
  echo -e "\n${yellowColour}[-]${endColour} ${blueColour}ffuf = ${endColour}${purpleColour}w${endColour}"
  echo -ne "\n${yellowColour}[?]${endColour} ${blueColour}Choose an option: ${endColour}" && read Option

  if [ "$Option" == "n" ];then
    echo -ne "\n${yellowColour}[+]${endColour} ${blueColour}Type the IP address: ${endColour}" && read IP
    echo -e "\n${yellowColour}[!]${endColour} ${purpleColour}Starting scanning...${endColour}\n"
    nmap -p- --open --min-rate 5000 -n -Pn -sS $IP > OpenPorts
    nmap -sCV -n -Pn $IP > Services
    echo -e "\n${yellowColour}[*]${endColour} ${blueColour}Scanning and information saved successfully.${endColour}"
  elif [ "$Option" == "w" ];then
    echo -ne "\n${yellowColour}[+]${endColour} ${blueColour}Type the IP address: ${endColour}" && read URL
    echo -e "\n${yellowColour}[!]${endColour} ${purpleColour}Starting fuzzing...${endColour}\n"
    ffuf -t 1000 -mc 200 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://$URL/FUZZ
    echo -e "\n${yellowColour}[*]${endColour} ${blueColour}Fuzzing successfully.${endColour}"
  else 
    echo "\n ${yellowColour}{X}${endColour} ${blueColour}Select a correct option.${endColour}"
  fi
}


#Main Function
if [ "$(id -u)" == "0" ]; then
  tools
  scan
else 
  echo -e "\n${yellowColour}[*]${endColour} ${turquoiseColour}Remember to run it as root.${endColour}\n"
fi
