# -*- coding: utf-8 -*-
from __future__ import division
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from random import randint, choice
import time

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

numbers = {}
for x in range(7):
    numbers[x] = str(choice([630, 847, 708])) + str(randint(1000000, 9999999))

texts = {0: {'text': "hey, saw ur cars for sale at oakbrook, been meaing to text, still available?", 'number': 0, 'wait': 73},
         1: {'text': "Hi there! I saw your post on Craigslist for the car! Would love to meet to check it out!", 'number': 1, 'wait': 25},
         2: {'text': "hey, so is it still available or did u sell it", 'number': 1, 'wait': 18},
         3: {'text': "responding to your craigslist ad about the car, would you take $500?", 'number': 2, 'wait': 37},
         4: {'text': "it looked nice in the pic but couldn’t tell how nice, it still run pretty good?", 'number': 2, 'wait': 2},
         5: {'text': "hey so my dads inthe hospital, could we meet rreal quick to buy the car", 'number': 0, 'wait': 23},
         6: {'text': "ill be out ur way in a couple hrs if we can meet", 'number': 0, 'wait': 7},
         7: {'text': "Saw your car at Oakbrook Thursday night! Is that for real? Seems too good to be true", 'number': 3, 'wait': 66},
         8: {'text': "I’m interested in buying your car if it’s still available. Looks in good condition. Fair price.", 'number': 4, 'wait': 32},
         9: {'text': "did you get my texts? i really need to buy your car soon, can we meet up", 'number': 0, 'wait': 6},
         10: {'text': "you sell car for 1000? i saw in parking lot. would love to buy/", 'number': 5, 'wait': 21},
         11: {'text': "Hi! Are you still selling your red Cruze for only $1,000? I’m super interested!", 'number': 6, 'wait': 15},
         12: {'text': "hey im outside ur house ur not answring r u home???", 'number': 0, 'wait': 6}
         }

send_from = 'teddysbots@gmail.com'
password = r'goillini'
send_to = ['6309817815@vtext.com']
subject = ''

for x in sorted(texts):
    value = texts[x]
    time.sleep(value['wait'])
    body = value['text']
    reply_to = numbers[value['number']]
    send_mail(send_from, password, send_to, reply_to, subject, body)
    send_mail(send_from, password, '3097122185@vtext.com', subject, body)