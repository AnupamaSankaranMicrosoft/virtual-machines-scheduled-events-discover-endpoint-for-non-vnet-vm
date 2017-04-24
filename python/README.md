# Overview

There are a total of 2 scripts:
1.	Discovery.py – This contains the core logic and is the entry point
2.	Util.py – This contains a bunch of utility/helper functions


## How does endpoint discovery work?

The mechanism to discover the CloudControl IP address is to resend a DHCP request. In the centralized DHCP service, the response is customized 
by carrying the CloudControl IP address inside the DHCP response option 245. The endpoint discovery script uses the same mechanism to determine 
the CloudControl IP address. Once the IP address is obtained, it is made available as part of the environment variable both in Windows and Linux worlds.


## Script usage

By default, upon discovering the CloudControl IP address, the script adds it to the environment variables. The variable name in both Windows and 
Linux is “CLOUDCONTROLIP”. However, the script has two additional modes of operation – “--debug” and “--donotaddtoenv” as listed below.

--debug: Enables running the script in debug mode wherein more logging is available for debugging purposes
--donotaddtoenv: Enables not adding the CloudControl IP as part of the environment variable

* python discovery.py -h
usage: discovery.py [-h] [--debug] [--donotaddtoenv]

optional arguments:
  -h, --help       show this help message and exit
  --debug          Enable running the script in debug mode
  --donotaddtoenv  Do not add the cloud control endpoint to environment
                   Variable

## Running the script on Windows and Linux

Pre-requesites: Install python 2.4+ 

Running on Windows: Once you have installed python, open an admin cmd window. Run the script by calling “python discovery.py”. 
If you want to include any of the optional switches, you can do so by calling “python discovery.py –debug”.

Running on Linux: Once you have installed python, run the script by calling “sudo python discovery.py”. You can include any/all of the 
optional switches.
