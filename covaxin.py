import time
from cowin_api import CoWinAPI
from twilio.rest import Client

def dial_number():
    """Dials one or more phone numbers from a Twilio phone number."""
    # number change krlena atleast mera no. hta dena to me se..
    client = Client("Token", "Key")
    call = client.calls.create(to="+reciever_num",
                               from_="Sender_num",
                               url="provided_url")
    print(call.sid)


cowin = CoWinAPI()

# you can also opt for pin code.
states = cowin.get_states()
# print(states) 20-mp
state_id = '20'

cowin = CoWinAPI()
districts = cowin.get_districts(state_id)
# print(districts)  314 - indore

from cowin_api import CoWinAPI

district_id = '314'

# ye update krte rehna.
date = '24-05-2021'  # Optional. Takes today's date by default

min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit
i=0
while True:
	try:
	    cowin = CoWinAPI()
	    available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
	    if len(available_centers['centers'])>0:
	        print()
	        print(available_centers['centers'])
	        dial_number()
	        break
	    else:
	        print(f"{i}",end="")
	    time.sleep(5)
	    print(end="\r")
	    i+=1
	except:
		print(0)