import smtplib
import email
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


HOST = 'smtp.163.com'  #smtp服务器地址
SUBJECT = 'title'    # title 
FROM = 'xxx@163.com' # 你发送邮箱

TO = '1045670921@qq.com'	#往哪发
TEXT = 'This is a test 2'
message = MIMEMultipart('related')


message_text = MIMEText(TEXT, 'plain', 'utf-8')	#第一个是正文
message.attach(message_text)

message['From'] = FROM
message['To'] = TO
message['Subject'] = SUBJECT

email_client = smtplib.SMTP_SSL()
email_client.connect(HOST, '465')
print('loading...')
result = email_client.login(FROM, 'password') #这写密码
print('Notication:', result)
email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
email_client.close()
