import requests
from bs4 import BeautifulSoup 
import smtplib
from email.mime.text import MIMEText
import os,time
su_old=24
def faemeil(xxx='默认'):
		subject = "成绩通知件"
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

while 1:
#for i in range(1):
	print("sleep 10s")
	#time.sleep(10)
	for i in range(100):
		time.sleep(0.1)
		print(i,end="\r")
	s = requests.Session()

	hea={
	"Host":"pro.mysuse.cn",
	"Connection":"keep-alive",
	"User-Agent":"Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/55.0.2883.87UBrowser/6.2.4098.3Safari/537.36",
	"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
	"Accept-Encoding":"gzip,deflate,br"
	}

	url="https://pro.mysuse.cn/jiaowu/grade"

	url2="https://pro.mysuse.cn/jiaowu/view"

	url3="https://pro.mysuse.cn/jiaowu/getGrade"

	da={
		"uid":"16011038025",
		"password":"a1019157263"
	}

	b=s.get(url,headers=hea)

	text=b.text

	# print(text)
	soup = BeautifulSoup(text, "html.parser")

	li=soup.find_all("meta")

	token=li[5]['content']
	f=open("xx.log","w").write(token)

	hea={
	"Host":"pro.mysuse.cn",
	"Connection":"keep-alive",
	"User-Agent":"Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/55.0.2883.87UBrowser/6.2.4098.3Safari/537.36",
	"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
	"Accept-Encoding":"gzip,deflate,br",
	"x-csrf-token":token

	}

	a=s.post(url,data=da,headers=hea)

	c=s.get(url3,headers=hea)
	js=c.json()
	su=(len(js['grades']))
	os.system('cls')
	print(su)
	print("令牌："+token)
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	li=[ f"课程名称：{i['kcmc']}，成绩：{i['cj']}" for i in js['grades']]
	
	print('\n'.join(li))
	if su>su_old:
		faemeil('</br>\n'.join(li))
	su_old=su

