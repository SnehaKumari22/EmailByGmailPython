import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import time
import os

sendTo="aaa.ckms@gmail.com"
sendFrom="team.l.stg@gmail.com"
fileTosend="abc.txt"
msg=MIMEMultipart()
msg["FROM"]=sendFrom
if(type(sendTo)==type([])):
   if(len(sendTo)>1):
    sendTo=", ".join(sendTo)
   else: 
      sendTo=sendTo[0]
msg["To"]=sendTo
msg["Subject"]="Parsing Notification"
msg.preamble="Unable to get attachment"

ctype,encoding=mimetypes.guess_type(fileTosend)
if ctype is None or encoding is not None:
    ctype="application/octet-stream"
    
maintype,subtype=ctype.split('/',1)
body="Hi,  \n\n  Input file successfuly parsed.\n\n Thanks and Regards,\n Team L"

try:
    script_dir=os.path.dirname(os.path.abspath(__file__))
    fp=open(os.path.join(script_dir,fileTosend),'rb')
    attachment=MIMEBase(maintype,subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition","attachment",fileName=fileTosend)
    msg.attach(attachment)
    print("file attached")
except:
    print("file not attached")
    
try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('username@gmail.com', 'passsword')
    server.sendmail(sendFrom, sendTo, msg.as_string())
    server.close()
 
    print( 'Email sent!')
except Exception as e:
    print(e)  
    print ('Something went wrong...')