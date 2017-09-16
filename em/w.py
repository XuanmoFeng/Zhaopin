#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from pa import Bei
import sys
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart 
reload(sys) 
sys.setdefaultencoding("utf-8")

def addimg(src,imgid):  
    fp = open(src, 'rb')  
    msgImage = MIMEImage(fp.read())  
    fp.close()  
    msgImage.add_header('Content-ID', imgid)  
    return msgImage

my_sender='fkmail@yeah.net'    # 发件人邮箱账号
my_pass = 'fengkai13142'              # 发件人邮箱密码
my=['763608087@qq.com',"2684586145@qq.com","1026880051@qq.com",'wsawy1996225@qq.com','120216630@qq.com','201531492@qq.com','1419325945@qq.com']      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
	url1="http://job.xidian.edu.cn/html/zpxx/nxqzph/"
	url2="http://job.xidian.edu.cn/html/zpxx/bxqzph/"
	sts='<html><table border="1">'
	sts+='<img src="cid:bei">'
	sts+='<img src="cid:nan">'
	sts+='</table></html>'
        msg= MIMEMultipart('related')
	msgtext=MIMEText(sts,'html','utf-8')
	msg.attach(msgtext)
	msg.attach(addimg('/root/9-9/out/bei.png','bei'))
	msg.attach(addimg('/root/9-9/out/nan.png','nan'))
        msg['From']=formataddr(["冯凯",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['Subject']="西安电子科技大学招聘会"                # 邮件的主题，也可以说是标题
        server=smtplib.SMTP_SSL("smtp.yeah.net", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
	for h in my:
       		msg['To']=formataddr(["FK",h])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        	server.sendmail(my_sender,[h,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
