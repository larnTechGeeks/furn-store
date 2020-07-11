import os
import africastalking

def notify_admin(phone, message):
    username = os.environ.get('AFRICATALKING_USERNAME')
    api_key = os.environ.get('AFRICATALKING_API_KEY')
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    recipients = [phone,]

    #message = 'Welcome to RayMoney our esteemed Customer, to proceed provide the given Code and proceed with registration and Confirm your oan limit. Code: R-'+str(message)
    #sender = "Africa's talking"
    try:
        #Once this is done, that's it! We'll handle the rest
        response = sms.send(message, recipients)
        print(response)
    except Exception as e:
        print(f"Error has Occurred.. {e}")