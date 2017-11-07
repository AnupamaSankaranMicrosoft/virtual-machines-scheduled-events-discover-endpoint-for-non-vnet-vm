How does endpoint discovery work?
===
The mechanism to discover the Scheduled Events Service IP address is to resend a DHCP request. In the centralized DHCP service, the response is customized 
by carrying the IP address inside the DHCP response option 245. The endpoint discovery script uses the same mechanism to determine 
the Scheduled Events IP address. Once the IP address is obtained, it is made available as part of the environment variable both in Windows and Linux worlds.

Running the discovery script
===
### `Pre-requesites`: Install python 2.4+ 

### `Windows:`

Once you have installed python, open an admin cmd window. Run the script by calling “python discovery.py”. 
If you want to include any of the optional switches, you can do so by calling “python discovery.py –debug”.

### `Linux:`

Once you have installed python, run the script by calling “sudo python discovery.py”. You can include any/all of the 
optional switches.

<br>

Discovering the endpoint
===
By default, upon discovering the Scheduled Events Service IP address, the script adds it to the environment variables. The variable name in both Windows and 
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


## Example 1: Output to environment variable
* __How to run__: 
```cmd
C:\python> python discovery.py
Cloud Control endpoint IP address: 168.63.129.16
Adding Cloud Control endpoint IP to the environment

SUCCESS: Specified value was saved.
```
* The host ip is stored in an environment variable %**CLOUDCONTROLIP** by default when running the script with no parameters

## Example 2: Output to registry location
* __How to run__: 
```cmd
C:\python> python discovery.py --outputreg
Cloud Control endpoint IP address: 168.63.129.16
Adding Cloud Control endpoint IP to the environment

SUCCESS: Specified value was saved.
Adding Cloud Control endpoint to registry location HKEY_LOCAL_MACHINE\Software\CloudControl
('168.63.129.16', 1)
```
* For windows VMs, this will set the host IP address for scheduled events in the registry at HKEY_LOCAL_MACHINE\Software\CloudControl

<br>

Creating the Scheduled Events URL with the discovered IP address. 
===
* Once you have the IP address for scheduled events, you can create the scheduled events url with the following format: 

        http://{IPADDRESS}/metadata/scheduledevents?api-version=2017-08-01


## For an example of using the discovery script, please look at [sample.py]()