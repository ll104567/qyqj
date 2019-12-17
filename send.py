#!/usr/bin/python3

import smtplib
import email
import time
import sys
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

HOST = 'smtp.163.com'  #smtp服务器地址
SUBJECT = 'aliyun邮件提醒'    # title 
FROM = 'll104567i@163.com' # 你发送邮箱

TO = '1045670921@qq.com'	#往哪发
TEXT = 'This is a test 2'
message = MIMEMultipart('related')

if len(sys.argv) == 2:
    TEXT = sys.argv[1]
else:
    print('Usage: python {} "text"'.format(sys.argv[0]))
    sys.exit(1)

message_text = MIMEText(TEXT, 'plain', 'utf-8')	#第一个是正文
message.attach(message_text)

message['From'] = FROM
message['To'] = TO
message['Subject'] = SUBJECT

email_client = smtplib.SMTP_SSL()
email_client.connect(HOST, '465')
print('loading...')
result = email_client.login(FROM, 'waawdr135') #这写
print('Notication:', result)
email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
email_client.close()
