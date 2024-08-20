# Simple Network Packet Analyzer
Network Packet Analyzer

This is a simple python tool used to sniff packets of mainly TCP and UDP protocols and capture their ip addresses, port numbers, protocol type and the payload data in the each packet. It by default captures for 10 seconds and stores the captured packet data in the file every 1 second for regular updates. 

DISCLAIMER: This tool has been developed only for educational purposes and the developer of this tool does not encourage any type of unethical use of this tool. The developer is not responsible or take responsibility for any sort of misuse of the tool by any person.   

Requirements:
- Python 3 and above
- Python supportive IDE
- Scapy,schedule,time library installed in your IDE

To install libraries:
- Go to your IDE terminal or CMD prompt
- run the following commands to install the required libraries
  > "pip install scapy"
  > "pip install schedule"
  > "pip install time"

Feature: 
- You can change the capture time and timeout according to your requirement
- You can specify custom path where you want your file to be created and saved 
- Packet details is automatically stored in a file called "pkt_data.txt"

Note: Default file path is "C:/" drive

How to use:
- Download the python file and open it in an IDE of your choice
- Make the above mentioned changes (optional)
- Execute the python tool
- View your captured data from the "pkt_data.txt" file

Note: If you see (b'') in your pkt_data.txt under the payload field, then do not misunderstand this for an error. It just means that there was no payload found in the packet captured.

Have a fun time seeing what your device does in the back when you are not doing anything or doing something on the network or on the Internet.
  
