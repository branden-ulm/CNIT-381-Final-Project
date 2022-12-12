from webexteamsbot import TeamsBot
from webexteamsbot.models import Response

import routers
import Skills as useful

# Router Info 
device_address = routers.router['host']
device_username = routers.router['username']
device_password = routers.router['password']

# apply information for restconf
port = '443'
url_base = "https://{h}/restconf".format(h=device_address)
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# bot info
bot_email = 'Mochi_@webex.bot' #Enter the bot email address
teams_token = 'NGI1NTEzYmQtNjQxMC00YmZhLThlNTMtZWRhODUzOWQ2Mjg2MDRhMzcxNjYtYTRj_P0A1_af949325-f1e2-44dc-a297-78a9bdf6f617' #Enter the bot access token
bot_url = "https://1d44-216-222-173-8.ngrok.io" #Enter the forwarding address from the ngrok command
bot_app_name = 'Mochi' #Enter the name of the ChatBot


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

# this function greats the user
def greeting(incoming_msg):
    sender = bot.teams.people.get(incoming_msg.personId)
    response = Response()
    response.markdown = "Hello {}, I am Mochi, your personal networking chat bot and dating guru.".format(
        sender.firstName
    )
    response.markdown += "\n\nWhat kind of help do you need? To see what I have to offer, all you have to do is ask for \n**/help**."
    return response
# function used to point to the skills file for specific skill
def show_run(incoming_msg):
    response = Response()
    response.markdown = "Here is the show run | sec interface.\n"
    response.markdown += useful.show_runskill()
    return response
def accesslist(incoming_msg):
    response = Response()
    response.markdown = "When you can't reach something, have you checked your access lists?\n"
    response.markdown += useful.accesslist()
    return response
def monitor(incoming_msg):
        useful.monitorskill()
def restconf(incoming_msg):
    """Returns arp table
    """
    response = Response()
    arps = useful.get_arp(url_base, headers,device_username,device_password)

    if len(arps) == 0:
        response.markdown = "I don't have any entries in my ARP table."
    else:
        response.markdown = "Here is the current ARP information. \n\n"
        for arp in arps:
            response.markdown += "* A device with IP {} and MAC {} are available on interface {}.\n".format(
               arp['address'], arp["hardware"], arp["interface"]
            )

    return response

def pickuplines(incoming_msg):
    response = Response()
    response.markdown = useful.pickuplines()
    return response
def helpme(incoming_msg):
    response = Response()
    response.markdown = useful.uselesshelpme()
    return response

bot.set_greeting(greeting)

# gives options for bot commands
bot.add_command("sri", "Shows the inteface section of running config", show_run)
bot.add_command("acl", "Access List", accesslist)
bot.add_command("ms", "Start The Monitor", monitor)
bot.add_command("arp", "This will show the arp table", restconf)
bot.add_command("pickup", "For the boys", pickuplines)

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
