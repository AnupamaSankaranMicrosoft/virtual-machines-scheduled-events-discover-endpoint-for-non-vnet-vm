import urllib.request
import json

def get_scheduled_events(uri):
    events_json = urllib.request.urlopen(uri).read()
    print(events_json)
	

def approve_scheduled_event(events):
    print("To Do")
	
def get_host_ip_address():


get_scheduled_events("http://google.com")