import smtplib,time,wmi,psutil
from email.mime.text import MIMEText
from auto_login.log import logger

e_from = '111119389@163.com'
password = '12301230aa'
host = 'smtp.163.com'
port = 25
subject = '自动登录结果通知'
logging = logger

def send(content, e_to = '76212133127108@qq.com'):
    msg = MIMEText(content)
    # logging.debug(msg.as_string())
    msg['Subject'] = subject
    msg['From'] = e_from
    msg['To'] = e_to
    #qq
    # s = smtplib.SMTP_SSL(host, port)
    #163
    s = smtplib.SMTP(host, port)
    try:
        s.login(e_from, password)
        s.sendmail(e_from, e_to, msg.as_string())
        logging.info('send success')
    except Exception as e:
        logging.info('send failure', e)
        pass
    finally:
        s.quit()