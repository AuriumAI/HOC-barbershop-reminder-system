import boto3, json
from datetime import datetime
import os

def lambda_handler(event, context):
    ses = boto3.client('ses')
    
    with open('appointments.json') as f:
        appointments = json.load(f)
    
    for person in appointments:
        name = person['name']
        email = person['email']
        appt_time = person['appointment_time']
        
        body = f"Hi {name}, just a reminder you have a cut scheduled at {appt_time} today at Creatr Barbershop. 💈"
        
        ses.send_email(
            Source=os.environ['SENDER_EMAIL'],
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Your Barbershop Appointment Reminder'},
                'Body': {'Text': {'Data': body}}
            }
        )
    
    return {"statusCode": 200, "body": "Emails sent"}
  
