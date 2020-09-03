import datetime as dt
import time
import smtplib, ssl

def send_email(to_email):
    dict_email = 'dark_blue9299@hotmail.com' #fill in w/ your email
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    context = ssl.create_default_context() #create secure SSL context
    server.starttls(context=context)
    server.login(dict_email, 'askimasli12') #replace password

    #Email
    message = 'deneme emailidir, takma kafaya'
    server.sendmail(dict_email, to_email, message)
    server.quit()

def send_email_at(send_time, to_email):
    time.sleep(send_time.timestamp() - time.timestamp())
    send_email(to_email)
    print('email sent')


