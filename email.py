#included email code below due to the scoping issues on send_email()
import datetime as dt
import time
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email():

    def send_email(to_email, user):
    #create the smpt server and login
    dict_email = 'dark_blue9299@hotmail.com' #fill in w/ your email
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.ehlo()
    #context = ssl.create_default_context() #create secure SSL context
    server.starttls()
    server.login(dict_email, 'askimasli12') #replace password

    #create message object
    msg = MIMEMultipart()

    #message template
    message = ""
    for word in user.words:
        message += (word.text + " -> " + word.translated + "\n")

    #setup the parameters
    msg['From'] = dict_email
    msg['To'] = to_email
    msg['Subject'] = "Don't Forget To Skim Through!"

    #add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #send the message via the server
    server.send_message(msg)
    del msg

    #terminate the SMTP session and close connection
    server.quit()

def send_email_at(send_time, to_email):
    time.sleep(send_time.timestamp() - time.timestamp())
    send_email(to_email)
    print('email sent')


