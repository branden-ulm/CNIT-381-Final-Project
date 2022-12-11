# CNIT-381-Final-Project

## Project Description

This project involves the creation of a Webex automation chatbot to complete various assignments between a branch and HQ router, including running commands and checking the status of the branch router and automatically updating the tunnel IP address on the HQ router to maintain a VPN connection with the branch router as it dynamically changes. 

## Prerequisites
In order to run the code used in the lab, the following things are needed:

- Working Linux Environment
- Downloaded Code above
- Webex Account
- ChatBot Credentials

## Creating the ChatBot

#### Step One
First, a Webex developer account is going to be needed. Navigate to https://developer.webex.com to either login or create a new account. 

#### Step Two
Once logged in, click on the "Start Building Apps" button followed by the "Create a Bot" button to start creating your own bot. 

#### Step Three
Fill in the required bot information, making sure to write down the chatbot email, access token, and name to be used in a later section.

## Preparing the Linux Environment

#### Step One
Download the above files to an easily accessible folder directory. Run the configuration on both routers found in CSR1.txt and CSR2.txt.

#### Step Two
Open a terminal on the Linux environment. Install required packages using the following commands.
<pre><code>sudo snap install ngrok
pip3 install webexteanssdk
pip3 install webexteamsbot</code></pre>

#### Step Three
Run the following command to allow for a successful bot connection. 
<pre><code>ngrok http 5000</code></pre>
Leave the terminal open to keep the connection active and save the forwarding address highlighted below for the next step.

![Alt text](/Screenshots/ngrok.png)

## Connecting to the ChatBot

#### Step One
Open the 381Bot.py file in a text editor such as Visual Studio, change the following fields to match the information tailored to your specific bot and Linux Enviroment in the above steps. Save the following changes to the file.

![Alt text](/Screenshots/botinfo.png)

#### Step Two
Navigate to the directory in which the files were downloaded to, then run the following command in the terminal to start running the bot. The terminal should look like the screenshot below if it is running correctly.

![Alt text](/Sreenshots/projectrunning.png)

#### Step Three
Navigate to https://teams.webex.com, then click the Messaging Tab on left-had side followed by the "Start a Conversation" plus sign on the top of the page, then the "Send a Direct Message" link in the dropdown menu to add the bot. Enter the bot email, ending in @webex.bot to start chatting.

If done correctly, the chat screen should look simlar to the screenshot below.

![Alt text](/Screenshots/webexconvo.png)

If the bot does not respond to your messages, ![Alt text](/Screenshots/hamster.jpg = 100x100)
