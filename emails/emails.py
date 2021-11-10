import sendgrid
import os
from sendgrid.helpers.mail import *

def sendemail():
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("ivanterminator333@gmail.com")
    to_email = To("protsailo31@gmail.com")
    subject = "Pizza"
    content = Content("Pizza", "Proszę potwierdzić zamówienie")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

