### teams Bot ###
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response

### Utilities Libraries
import routers
import BotSkills as useful

# Router Info 
device_address = routers.router['host']
device_username = routers.router['username']
device_password = routers.router['password']

# RESTCONF Setup
port = '443'
url_base = "https://{h}/restconf".format(h=device_address)
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Bot Details
bot_email = 'NamBot1.0@webex.bot'
teams_token = 'YjM3M2YyZDMtOTdkYS00N2U4LWE4ZjEtYzY5OTU4MjUwZGM1Y2YzZjI3M2MtNzk5_P0A1_b34062fa-24f1-480f-a815-05d10d8cf4f2'
bot_url = "https://4412-144-13-254-61.ngrok.io"
bot_app_name = 'CNIT-381 Network Auto Chat Bot'
# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},],
)

# Create a function to respond to messages that lack any specific command
# The greeting will be friendly and suggest how folks can get started.
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Greetings {}, I am NamBot, I'm Your Branch Router Assistant  ".format(
        sender.firstName
    )
    response.markdown += "\n\nWhat do you want? I'm busy fixing our firewall labs \n**/help**."
    return response

##Doms Stuff
def ansible(incoming_msg):
    response = Response()
    response.markdown = "Here is the show version command, ansible is very cool\n"
    response.markdown += useful.ansibleskill()
    return response
def netmiko(incoming_msg):
    response = Response()
    response.markdown = "Here is some brief IP info, I know it might seem like a lot for your tiny brain\n"
    response.markdown += useful.netmikoskill()
    return response
def monitor(incoming_msg):
        useful.monitorskill()
def restconf(incoming_msg):
    """Return the arp table from device
    """
    response = Response()
    arps = useful.get_arp(url_base, headers,device_username,device_password)

    if len(arps) == 0:
        response.markdown = "I don't have any entries in my ARP table."
    else:
        response.markdown = "Here is the ARP information I know you ungrateful engineer. \n\n"
        for arp in arps:
            response.markdown += "* A device with IP {} and MAC {} are available on interface {}.\n".format(
               arp['address'], arp["hardware"], arp["interface"]
            )

    return response
def startup(incoming_msg):
    response = Response()
    response.markdown = "Here is the startup config, you should start studying if you need help with this\n"
    response.markdown += useful.netmikostartup()
    return response
def nroute(incoming_msg):
    response = Response()
    response.markdown = "Here is the routing table, this might hurt your tiny brain\n"
    response.markdown += useful.netmikoroute()
    return response
def rps(incoming_msg):
    response = Response()
    response.markdown = useful.uselessrps()
    return response
def pickuplines(incoming_msg):
    response = Response()
    response.markdown = useful.pickuplines()
    return response
def helpme(incoming_msg):
    response = Response()
    response.markdown = useful.uselesshelpme()
    return response
# Set the bot greeting.
bot.set_greeting(greeting)

# Add Bot's Commmands
bot.add_command("asv", "Show Version", ansible)
bot.add_command("acl", "Access List", netmiko)
bot.add_command("ms", "Start The Monitor", monitor)
bot.add_command("rcarp", "Check Arp Table", restconf)
bot.add_command("nisakmp", "Check Isakmp Policy", isakmp)
bot.add_command("nstart", "Check Startup Config", startup)
bot.add_command("pickup", "For the boys", pickuplines)
bot.add_command("nroute", "Show IP route table", nroute)


# Every bot includes a default "/echo" command.  You can remove it, or any
bot.remove_command("/echo")

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
