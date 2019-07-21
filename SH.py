import time,os
from email.mime.text import MIMEText
import smtplib
def faemeil(xxx='您的实时程序已经无响应。。。\n已尝试复活'):
      subject = "程序崩溃通知"
      content = f"<h4>{xxx}</h4>"  # 邮件内容
      sender = "18381801393@163.com"  # 发件人
      password = 'a18381801393'  # 刚才我们在163邮箱里设置的授权密码
      receivers = ["1019157263@qq.com"]  # 收件人
      for receiver in receivers:
          message = MIMEText(content, "html", "utf-8")
          message["From"] = sender
          message["To"] = receiver
          message["Subject"] = subject
       
          smtp = smtplib.SMTP_SSL('smtp.163.com', 994)
          smtp.login(sender, password)
          smtp.sendmail(sender, [receiver], message.as_string())
          smtp.close()

t=120
b=open('xx.log','r').read()
print(b)
print('守护程序开始启动...')
while 1:
   print(f'计时{t}秒中....')
   for i in range(t*10):
      time.sleep(0.1)
      print(i,end="\r")
   f=open('xx.log','r')
   a=f.read()
   print(a)
   if a==b:
      print('程序死了....')
      print('发邮件')
      faemeil()#fayoujian 
      print('程序结束.....')
      os.system('python CJCX.py')#尝试复活
   else:
      b=a

