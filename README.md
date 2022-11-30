## Project Overview

For this project we are building a Webex automation chatbot that will communicate back to our branch and HQ routers (both Cisco CSR1000v) that will check the status on the branch router, run commands on the branch router, and run an automation script to have the IPSEC tunnel IP address on the HQ router change when a IP address change is detected on the WAN interface on the branch router to maintain the VPN connection.

## Setup

Download 381Bot.py, BotSkills.py, ansible.cfg, inventory.txt, and routers.py to a folder directory of your choice. On the machine that you are running the program on, you must have python 3.8.15 or later installed in order to run this program successfully as a prerequsite. 

As for our branch and HQ routers, a small amount of configuration has been added to them to create the VPN connection, as listed in CSR1.txt and CSR2.txt, with CSR1 being the HQ router.

First, you will want to open a terminal file and enter ngrok http 5000. This will open a reverse proxy connection so Webex and python can communicate with each other for a successful bot connection. Once this is running keep note of the forwarding address as this will be needed in the 381bot.py file. Do not close the terminal or end the process as the bot will no longer work if stopped.

Once you open 381bot.py in a text editor of your choice, you will want to change the bot_url to the forwarding address that ngrok gave you. You will then want to change the bot_email to the email address that is assigned to your bot in the Webex developer page. It should end with a @webex.bot address. Lastly, you will want to add your Webex authentication token to the teams_token. 

The other thing you may need to change are the router addresses used in our python files. For routers.py and BotSkills.py, the ip addresses used to connect to the branch and HQ routers may need to be changed depending on what addresses your routers have obtained.

Once these three things are changed, save the relavent files and run 381Bot.py via Python 3 in a terminal. The bot should now be running, head over to webex and message the bot, you should recieve a reply.

## Complete

You now have secuessfully set up our Webex bot. If you used our code it should look simmilar to below upon first greeting.

![Bot](/images/botfinished.png)
