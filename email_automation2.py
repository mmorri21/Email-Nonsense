import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(send_from, password, send_to, subject, body, files=[], server="smtp.gmail.com:587"):
    assert type(send_to)==list
    assert type(files)==list
    
    msg = MIMEMultipart('alternative')
    msg.add_header('reply-to', '123456789')
    msg['From'] = send_from + ' <' + '123456789' + '>'
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach( MIMEText(body, 'plain') )
    #for f in files:
    #    part = MIMEBase('application', "octet-stream")
    #    part.set_payload( open(f,"rb").read() )
    #    Encoders.encode_base64(part)
    #    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    #    msg.attach(part)
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
subject = ''
body = 'This is a test2.'
send_mail(send_from, password, send_to, subject, body)