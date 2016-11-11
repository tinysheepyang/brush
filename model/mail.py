#!/usr/bin/python
# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.Header import Header
from email.mime.multipart import MIMEMultipart

mailfrom = 
mailto = 
mailuser = 
mailpasswd = 
mailaddr = 
mailport = '25'



class mail:
    def __init__(self, environment,state, caseID, url, message, date):
        
        self.environment = environment
        self.state = state
        self.caseID = caseID
        self.url = url
        self.message = message
        self.date = date
        self.mail = smtplib.SMTP()
        self.msg = MIMEMultipart()

    def conn(self, mailaddr, mailport = '25'):
        self.mail.connect(mailaddr, mailport)

    def login(self, mailuser = mailfrom, mailpasswd = ''):
        self.mail.login(mailuser, mailpasswd)

    def makemsg(self):
        self.msg['From'] = mailfrom
        self.msg['To'] = mailto

        self.msg['Subject'] = Header('[自动化测试]线上环境测试 %s ' % self.state , charset = 'UTF-8')
        content = MIMEText("** ***** selenium ***** **\n\n \
                Environment: %s\n \
                State: %s\n \
                caseName: %s\n \
                Message: %s\n \
                URL: %s\n \
                Date/Time: %s\n " % (self.environment, self.state, self.caseID, self.url, self.message, self.date), _subtype='plain', _charset='UTF-8')

        self.msg.attach(content)

    def send(self, mailto):
        self.mail.sendmail(mailfrom, mailto, self.msg.as_string())

    def close(self):
        self.mail.quit()

def main():
    import getopt, sys
    opts, args = getopt.getopt(sys.argv[1:], 'e:c:s:u:m:d:t:',
                               ['environment=', 'caseID=', 'state=', 'url=', 'message=', 'date=', 'mailto='])

    for opt, arg in opts:
        
        # 环境
        if opt in ('-e', 'environment'):
            environment = arg
        # 验证状态
        if opt in ('-s', 'state'):
            state = arg
        #caseID
        if opt in ('-c','caseID'):
            caseID = arg

        if opt in ('-u', 'url'):
            url = arg

        if opt in ('-m', 'message'):
            message = arg

        # 时间
        if opt in ('-d', 'date'):
            date = arg
        #发送人
        if opt in ('-t', 'mailto'):
            mailto = arg

    report = mail(environment, state, caseID, message, url, date)
    report.conn(mailaddr, mailport)
    report.login(mailuser, mailpasswd)
    report.makemsg()
    for line in mailto.split(','):
        report.send(line)
    return(report.close())

if __name__ == '__main__':
    print(main())
