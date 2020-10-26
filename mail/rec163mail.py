import base64
import poplib
from email.parser import Parser
from email import header
from numpy.core import unicode
import json
import time


def connect(serverAddress):
    server = poplib.POP3(serverAddress)
    info = server.getwelcome().decode('utf8')
    if info.split(' ')[0] == '+OK':
        return server

def close(server):
    server.close()

def login(server, userName, passwd):
    server.user(userName)
    server.pass_(passwd)

def getMailTotal(server):
    _, mails, _ = server.list()
    return len(mails)

def my_unicode(s, encoding):
    if encoding:
        return unicode(s, encoding)
    else:
        return unicode(s)

def strpRecTime(strTime):
    struct_time = time.strptime(strTime, "%a, %d %b %Y %H:%M:%S +0800 (%Z)")
    strfTime = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
    return strfTime

def getAllMailData(server):
    datas = []
    try:
        i = 0
        while True:
            i += 1
            response_status, mail_message_lines, octets = server.retr(i)
            msg_content = b'\r\n'.join(mail_message_lines).decode('gbk')
            msg = Parser().parsestr(text=msg_content)
            # 获取主题信息，也就是标题内容
            subject = msg.get('Subject')
            subject = header.decode_header(subject)
            subject = my_unicode(subject[0][0], subject[0][1])
            # 获取时间信息，也即是邮件被服务器收到的时间
            received_time = msg.get("Date")
            strTime = strpRecTime(received_time)
            datas.append({subject: strTime})
    except poplib.error_proto:
        pass
    return datas

#def addNewMailToQue(mails):

def run():
    server = connect('pop.163.com')
    login(server, 'howie_test@163.com', 'w123456w')
    for i in range(10):
        result = getAllMailData(server)
        print(result)
        time.sleep(3)


if __name__ == '__main__':
    run()
