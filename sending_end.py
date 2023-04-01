import smtplib

"""
server= smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
username = ''

password = ''
server.login(username,password)
server.sendmail(username,password,"This mail is for practice purpose")
print("mail sent")

"""
import smtplib

from email.mime.text import MIMEText


def sending(from_addr,to_addrs,messagee):
        # connect with Google's servers

        smtp_ssl_host = 'smtp.gmail.com'

        smtp_ssl_port = 465

        # use username or email to log in

        #username = ''
        username =from_addr

        if (from_addr==''):
                password = ''
        if (from_addr==''):
                password = ''




        # the email lib has a lot of templates

        # for different message formats,

        # on our case we will use MIMEText

        # to send only text

        message = MIMEText(messagee)
        print (message)

        message['subject'] = 'Hello'

        message['from'] = from_addr

        message['to'] = ', '.join(to_addrs)



        # we'll connect using SSL

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

        # to interact with the server, first we log in

        # and then we send the message

        server.login(username, password)

        server.sendmail(from_addr, to_addrs, message.as_string())

        server.quit()
        return("message sent")




from_addr = ''

to_addrs = ['']
