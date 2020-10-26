from transmitter import Transmitter
from mailServer import MailServer
import time
import json
import os


class Controller(object):

    def __init__(self):
        self.tr = Transmitter()

    def snedSaleEmailToAllTestMailAddress(self, site, mail_address_list, environment, mode_name='', sleepTime=0):
        if site == 'china':
            for mail_address in mail_address_list:
                self.tr.sendMailFromChinaSale(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'thailand':
            for mail_address in mail_address_list:
                self.tr.sendMailFromThailandSale(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'indonesia':
            for mail_address in mail_address_list:
                self.tr.sendMailFromIndonesiaSale(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'international':
            for mail_address in mail_address_list:
                self.tr.sendMailFromInternationalSale(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        else:
            raise Exception('传入的站点错误，无法执行')

    def snedProdCEmailToAllTestMailAddress(self, site, mail_address_list, environment, mode_name='', sleepTime=0):
        if site == 'china':
            for mail_address in mail_address_list:
                self.tr.sendMailFromChinaProdC(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'thailand':
            for mail_address in mail_address_list:
                self.tr.sendMailFromThailandProdC(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'indonesia':
            for mail_address in mail_address_list:
                self.tr.sendMailFromIndonesiaProdC(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'international':
            for mail_address in mail_address_list:
                self.tr.sendMailFromInternationalProdC(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        else:
            raise Exception('传入的站点错误，无法执行')

    def snedProdHEmailToAllTestMailAddress(self, site, mail_address_list, environment, mode_name='', sleepTime=0):
        if site == 'china':
            for mail_address in mail_address_list:
                self.tr.sendMailFromChinaProdH(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'thailand':
            for mail_address in mail_address_list:
                self.tr.sendMailFromThailandProdH(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'indonesia':
            for mail_address in mail_address_list:
                self.tr.sendMailFromIndonesiaProdH(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'international':
            for mail_address in mail_address_list:
                self.tr.sendMailFromInternationalProdH(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        else:
            raise Exception('传入的站点错误，无法执行')

    def snedSaleEmailToAllTestMailAddressBlacklist(self, site, mail_address_list, environment, mode_name='', sleepTime=0):
        if site == 'china':
            for mail_address in mail_address_list:
                self.tr.sendMailFromChinaSaleBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'thailand':
            for mail_address in mail_address_list:
                self.tr.sendMailFromThailandSaleBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'indonesia':
            for mail_address in mail_address_list:
                self.tr.sendMailFromIndonesiaSaleBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'international':
            for mail_address in mail_address_list:
                self.tr.sendMailFromInternationalSaleBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        else:
            raise Exception('传入的站点错误，无法执行')

    def snedProdCEmailToAllTestMailAddressBlacklist(self, site, mail_address_list, environment, mode_name='', sleepTime=0):
        if site == 'china':
            for mail_address in mail_address_list:
                self.tr.sendMailFromChinaProdCBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'thailand':
            for mail_address in mail_address_list:
                self.tr.sendMailFromThailandProdCBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'indonesia':
            for mail_address in mail_address_list:
                self.tr.sendMailFromIndonesiaProdCBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'international':
            for mail_address in mail_address_list:
                self.tr.sendMailFromInternationalProdCBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        else:
            raise Exception('传入的站点错误，无法执行')

    def snedProdHEmailToAllTestMailAddressBlacklist(self, site, mail_address_list, environment, mode_name='', sleepTime=0):
        if site == 'china':
            for mail_address in mail_address_list:
                self.tr.sendMailFromChinaProdHBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'thailand':
            for mail_address in mail_address_list:
                self.tr.sendMailFromThailandProdHBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'indonesia':
            for mail_address in mail_address_list:
                self.tr.sendMailFromIndonesiaProdHBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        elif site == 'international':
            for mail_address in mail_address_list:
                self.tr.sendMailFromInternationalProdHBlacklist(environment=environment, mode_name=mode_name, mail_address=mail_address)
                time.sleep(sleepTime)
        else:
            raise Exception('传入的站点错误，无法执行')

    def autoTest(self, site, environment, case_file_name, sleep_time):
        with open('cases/{}'.format(case_file_name), 'r', encoding='utf-8') as f:
            cases = json.loads(f.read())
        for case in cases:
            time.sleep(sleep_time)
            self.tr.autoTest(site, environment, case)

    def findMailOnServer(self, mails):
        mailServer = MailServer()
        mailServer.connect()
        mailServer.login()
        while True:
            print('*'*100)
            mailServer.getMailTotalNum()
            mailServer.getAllMailData()
            status = True
            for i in mails:
                print(mailServer.findMailBySubject(i))
                if mailServer.findMailBySubject(i) != {}:
                    print(i, '*OK*')
                else:
                    print(i, '*不OK*')
                    status = False
            print('*'*100)
            if status == True:
                break
            time.sleep(5)
        mailServer.close()

if __name__ == '__main__':
    controller = Controller()
    mail_address_list = [
        'howie_test@163.com',
        'howie_test@126.com',
        'howie_test@yeah.net',
        'howie_test@outlook.com',
        'howie_test@hotmail.com',
        'howie_test@sohu.com',
        'howie.w.test@gmail.com',  #未开通
        'howie_test@tom.com',
        'howie_test@sina.com',
        'howie_test@yahoo.com',  #未开通
        'wanghongwei47@jd.com',  # 未开通
        '2387171346@qq.com',
        # 'howie666@126.com',
        # 'howie_test2@yeah.net'
    ]
    # for i in range(10):
    controller.snedSaleEmailToAllTestMailAddress(
        site='china',
        mail_address_list=mail_address_list,
        environment='yfb',
        mode_name='测试邮件_EOF',
        sleepTime=1
        )
    # while True:
    #     controller.findMailOnServer(controller.tr.mailSubject)

    # controller.autoTest(
    #     site='international',
    #     environment='online',
    #     case_file_name='国际站.json',
    #     sleep_time=1
    # )