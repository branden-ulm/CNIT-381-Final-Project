import os
import sys
### For RESTCONF
import requests
import json
from netmiko import Netmiko
from netmiko import ConnectHandler
import subprocess
import time
import random

router = {'device_type': 'cisco_ios', 'host': '192.168.56.102', 'username': 'cisco','password': 'cisco123!','port': 22, 'secret': 'cisco', 'verbose': True}

def accesslist():
    connection = ConnectHandler(**router)
    prompt = connection.find_prompt()
    if '>' in prompt:
        connection.enable()
    #send commands and check output
    output = ""
    output += connection.send_command("show ip access-list")
    connection.disconnect()
    return output
def show_runskill():
    temp = subprocess.Popen("ansible router1 -i ./inventory.txt -m raw -a 'show run | sec interface' > temp.txt", shell=True, stdout = subprocess.PIPE)
    output = str(temp.communicate())
    output = ''
    time.sleep(1)
    temp = open("temp.txt","r")
    for line in temp:
        output= output + line
    temp.close()
    subprocess.Popen("rm temp.txt", shell=True, stdout = subprocess.PIPE)
    return output
def get_arp(url_base,headers,username,password):
    url = url_base + "/data/Cisco-IOS-XE-arp-oper:arp-data/"

    # this statement performs a GET on the specified url
    response = requests.get(url,
                            auth=(username, password),
                            headers=headers,
                            verify=False
                            )

    # return the json as text
    return response.json()['Cisco-IOS-XE-arp-oper:arp-data']['arp-vrf'][0]['arp-oper']
def monitorskill():
    prevIP = ""
    currIP = ""
    while True:
        #step 1, finding the changed address of branch router
        router = {'device_type': 'cisco_ios', 'host': '192.168.56.102', 'username': 'cisco','password': 'cisco123!','port': 22, 'secret': 'cisco', 'verbose': True}
        connection = ConnectHandler(**router)
        prompt = connection.find_prompt()
        if '>' in prompt:
            connection.enable()
        output = ""
        output += connection.send_command("show ip int GigabitEthernet2 | i Internet")
        connection.disconnect()
        currIP = output[output.find("is")+3:output.find("/")]
        if currIP != prevIP:
            comtosend = "set peer "+currIP
            #step 2, changing the vpn setting of router 2
            router2 = {'device_type': 'cisco_ios', 'host': '192.168.56.105', 'username': 'cisco','password': 'cisco123!','port': 22, 'secret': 'cisco', 'verbose': True}
            connection = ConnectHandler(**router2)
            prompt = connection.find_prompt()
            if '>' in prompt:
                connection.enable()
            output = connection.send_command("show run | i set peer")
            prevIP = output[output.find("peer")+4:]
            rempeercom = "no set peer "+prevIP
            connection.send_config_set(["crypto map Crypt 10 ipsec-isakmp", rempeercom])
            connection.send_config_set(["no crypto isakmp key cisco address "+prevIP])
            connection.send_config_set(["crypto map Crypt 10 ipsec-isakmp", comtosend])
            connection.send_config_set(["crypto isakmp key cisco address "+currIP])
            print("IP Changed from "+prevIP+" to "+currIP)
            prevIP = currIP
        time.sleep(30)
def netmikoisakmp(): ### BRANDEN PUT YOUR STUFF HERE (ACL)
    router = {'device_type': 'cisco_ios', 'host': '192.168.56.102', 'username': 'cisco','password': 'cisco123!','port': 22, 'secret': 'cisco', 'verbose': True}
    connection = ConnectHandler(**router)
    prompt = connection.find_prompt()
    if '>' in prompt:
        connection.enable()
    output = ""
    output += connection.send_command("show crypto isakmp policy")
    connection.disconnect()
    return output
def netmikostartup():
    router = {'device_type': 'cisco_ios', 'host': '192.168.56.102', 'username': 'cisco','password': 'cisco123!','port': 22, 'secret': 'cisco', 'verbose': True}
    connection = ConnectHandler(**router)
    prompt = connection.find_prompt()
    if '>' in prompt:
        connection.enable()
    output = ""
    output += connection.send_command("show startup-config")
    connection.disconnect()
    return output
def pickuplines():
    quotes = ["Are you a MAC address, because I'd put you on my ARP table?",
              "You had me at 'Hello World'", "Do you like firewalls? I use protection.", 
              "My server never goes down, but I would for you.",
              "Baby, you must be running on TCP - everytime I talk to you, you give me an ACK.",
              "seq 69 permit any any", "Are you my standby router, because you're hot.", 
              "You are my favorite mode, promiscuous... ", "ICMP; I see you and me.", 
              "I wish I was your keyboard so I could be your type.", "Are you my EIGRP Neighbor, because I want to form an adjacency.", 
              "If I'd put you in my trunk, you would be dynamic-desirable :)"]
    
    mysteryboy = random.randint(0,len(quotes)-1)
    return quotes[mysteryboy]