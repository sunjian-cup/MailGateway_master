import base64
import poplib
from email.parser import Parser
from email import header
#from numpy.core import unicode
import json


class MailError(Exception):  # 创建一个新的exception类来抛出自己的异常。
    # 异常应该继承自 Exception 类，包括直接继承，或者间接继承
    def __init__(self, errorinfor):
        self.error = errorinfor

    def __str__(self):
        return self.error




class MailServer(object):

    def __init__(self):
        self.address163 = 'howie_test@163.com'
        self.passwd163 = 'w123456w'
        self.popServer163 = 'pop.163.com'
        self.addressYeah = 'howie_test@yeah.net'
        self.passwdYeah = 'w123456w'
        self.popServerYeah = 'pop.yeah.net'
        self.addressTom = 'howie_test@tom.com'
        self.passwdTom = 'w123456'
        self.popServerTom = 'pop.tom.com'

    def get_mail_info(self, s):
        try:
            nickname, account = s.split(' ')
        except Exception:
            print(s)
        # try:
        #     # 获取字串的编码信息
        #     charset = nickname.split('?')[1]
        #     # print('编码：{}'.format(charset))
        #     nickname = nickname.split('?')[3]
        #     nickname = str(base64.decodebytes(nickname.encode(encoding=charset)), encoding=charset)
        #     account = account.lstrip('<')
        #     account = account.rstrip('>')
        # except Exception:
        #     pass
        # return nickname, account

    def decode_base64(self, s, charset='utf8'):
        return str(base64.decodebytes(s.encode(encoding=charset)), encoding=charset)

    def decode_byte(self, bstr, charset='utf8'):
        bstr.decode(charset)

    def openDebug(self):
        self.server.set_debuglevel(1)

    def isConnect(self, info):
        if info.split(' ')[0] == '+OK':
            return True
        else:
            return False

    def connect(self):
        self.server = poplib.POP3(self.popServerTom)
        info = self.server.getwelcome().decode('utf8')
        if self.isConnect(info) == False:
            raise MailError('连接163邮件服务器异常')

    def login(self):
        self.server.user(self.addressTom)
        self.server.pass_(self.passwdTom)

    def getMailTotalNum(self):
        self.resp, self.mails, self.octets = self.server.list()
        return self.mails

    def close(self):
        self.server.close()

    def my_unicode(self, s, encoding):
        if encoding:
            return unicode(s, encoding)
        else:
            return unicode(s)

    def getAllMailData(self):
        datas = []
        for i in range(1, len(self.mails)):
            response_status, mail_message_lines, octets = self.server.retr(i)
            msg_content = b'\r\n'.join(mail_message_lines).decode('gbk')
            msg = Parser().parsestr(text=msg_content)
            # print(msg)
            # break
            # 获取发件人详情
            # fromstr = msg.get('From')
            # print(fromstr)
            # print(fromstr)
            # from_nickname, from_account = self.get_mail_info(fromstr)
            # print(from_nickname)
            # # 获取收件人详情
            # tostr = msg.get('To')
            # print(tostr)
            # to_nickname, to_account = self.get_mail_info(tostr)
            # 获取主题信息，也就是标题内容
            subject = msg.get('Subject')
            subject = header.decode_header(subject)
            subject = self.my_unicode(subject[0][0], subject[0][1])
            print(subject)
            # 获取时间信息，也即是邮件被服务器收到的时间
            received_time = msg.get("Date")
            datas.append({subject: received_time})
        with open('cache.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(datas))
        # print(datas)
        return datas

    def findMailBySubject(self, subject):
        with open('cache.json', 'r', encoding='utf-8') as f:
            datas = json.loads(f.read())
        for data in datas:
            print(subject, data)
            if subject in data:
                return data
        return {}

    def inputSubjects(self):
        text = input('粘贴所有需要检查的邮箱\n')
        # text = text.split('\r\n')
        print(text)

if __name__ == '__main__':
    mailServer = MailServer()
    mailServer.connect()
    mailServer.login()
    mailServer.getMailTotalNum()
    mailServer.getAllMailData()
    mailServer.close()
    #
    # print(mail.findMailBySubject('测试邮件_EOF_1581681524652705556'))
    # mailServer.inputSubjects()