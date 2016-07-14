# -*- coding: utf-8 -*-
from __future__ import division
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
def send_mail(send_from, password, send_to, reply_to, subject, body, server="smtp.gmail.com:587"):
    assert type(send_to)==list
    
    msg = MIMEMultipart('alternative')
    msg.add_header('reply-to', reply_to)
    msg['From'] = send_from + ' <' + reply_to + '>'
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach( MIMEText(body, 'plain') )
    smtp = smtplib.SMTP(server)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login(send_from, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

send_from = 'teddysbots@gmail.com'
password = 'goillini'
send_to = ['3097122185@vtext.com']
reply_to = '262966'
subject = ''
body = "Shipped: Your Amazon package with Pink Furby (Quantity 1,000) will be delivered Fri, Jul 15."
send_mail(send_from, password, send_to, reply_to, subject, body)
