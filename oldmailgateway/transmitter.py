import Config
import Jsf
import json
import mode
import sys

class Transmitter(object):

    def __init__(self):
        self.mailSubject = []

    def sendMailFromChinaSale(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineChinaSale()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbChinaSale()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpChinaSaleGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromChinaSaleBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineChinaSale()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbChinaSale()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpChinaSaleBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromChinaProdC(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineChinaProd()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbChinaProd()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpChinaProdCGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromChinaProdCBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineChinaProd()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbChinaProd()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpChinaProdCBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromChinaProdH(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineChinaProd()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbChinaProd()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpChinaProdHGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromChinaProdHBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineChinaProd()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbChinaProd()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpChinaProdHBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromThailandSale(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineThailand()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbThailand()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpThailandSaleGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromThailandSaleBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineThailand()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbThailand()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpThailandSaleBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromThailandProdC(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineThailand()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbThailand()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpThailandProdCGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromThailandProdCBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineThailand()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbThailand()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpThailandProdCBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromThailandProdH(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineThailand()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbThailand()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpThailandProdHGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromThailandProdHBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineThailand()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbThailand()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpThailandProdHBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response


    def sendMailFromIndonesiaSale(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineIndonesia()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbIndonesia()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpIndonesiaSaleGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromIndonesiaSaleBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineIndonesia()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbIndonesia()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpIndonesiaSaleBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromIndonesiaProdC(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineIndonesia()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbIndonesia()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpIndonesiaProdCGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromIndonesiaProdCBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineIndonesia()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbIndonesia()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpIndonesiaProdCBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromIndonesiaProdH(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineIndonesia()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbIndonesia()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpIndonesiaProdHGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromIndonesiaProdHBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineIndonesia()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbIndonesia()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpIndonesiaProdHBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response


    def sendMailFromInternationalSale(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineInternational()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbInternational()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpInternationalSaleGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromInternationalSaleBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineInternational()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbInternational()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpInternationalSaleBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromInternationalProdC(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineInternational()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbInternational()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpInternationalProdCGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromInternationalProdCBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineInternational()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbInternational()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpInternationalProdCBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromInternationalProdH(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineInternational()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbInternational()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpInternationalProdHGeneral()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def sendMailFromInternationalProdHBlacklist(self, mode_name='', environment='', mail_address=''):
        if environment == 'online':
            jsf = Config.getJsfOnlineInternational()
        elif environment == 'yfb':
            jsf = Config.getJsfYfbInternational()
        else:
            raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        http = Config.getHttpInternationalProdHBlacklist()
        send_mail_parameter = Config.getsendMailParameter()
        if mode_name != '':
            this_mode = mode.choiseMode(mode_name)
        else:
            this_mode = {}
        if mail_address != '':
            send_mail_parameter['mailAddress'] = mail_address
        send_mail_parameter.update(this_mode)
        send_mail_parameter['title'] = send_mail_parameter['title'] + '_' + send_mail_parameter.get('businessID')
        self.mailSubject.append(send_mail_parameter['title'])
        body = Jsf.getBody(
            account=http.get('account'),
            token=http.get('token'),
            type=http.get('type'),
            mail_info=send_mail_parameter
        )
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('businessID:', send_mail_parameter.get('businessID'))
        print('url:', url)
        print('header:', header)
        print('body:', body)
        response = Jsf.send(url=url, header=header, body=body)
        print(response)
        return response

    def autoTest(self, site, environment, body):
        if site == 'chinaSale':
            if environment == 'online':
                jsf = Config.getJsfOnlineChinaSale()
            elif environment == 'yfb':
                jsf = Config.getJsfYfbChinaSale()
            else:
                raise Exception('环境错误')
        elif site == 'chinaProd':
            if environment == 'online':
                jsf = Config.getJsfOnlineChinaProd()
            elif environment == 'yfb':
                jsf = Config.getJsfYfbChinaProd()
            else:
                raise Exception('环境错误')
        elif site == 'thailand':
            if environment == 'online':
                jsf = Config.getJsfOnlineThailand()
            elif environment == 'yfb':
                jsf = Config.getJsfYfbThailand()
            else:
                raise Exception('环境错误')
        elif site == 'indonesia':
            if environment == 'online':
                jsf = Config.getJsfOnlineIndonesia()
            elif environment == 'yfb':
                jsf = Config.getJsfYfbIndonesia()
            else:
                raise Exception('环境错误')
        elif site == 'international':
            if environment == 'online':
                jsf = Config.getJsfOnlineInternational()
            elif environment == 'yfb':
                jsf = Config.getJsfYfbInternational()
            else:
                raise Exception('环境错误')
        header = Jsf.getHeader(jsf.get('token'))
        url = Jsf.getUrl(
            host=jsf.get('host'),
            interface=jsf.get('interface'),
            alias=jsf.get('alias'),
            method=jsf.get('method'),
            appid=jsf.get('appid')
        )
        function_name = sys._getframe().f_code.co_name
        print('function name: {}'.format(function_name))
        print('caseName:', body.get('title'))
        print('url:', url)
        print('header:', header)
        print('body:', json.dumps(body))
        response = Jsf.send(url=url, header=header, body=json.dumps(body))
        print(response)
        return response


if __name__ == '__main__':
    t = Transmitter()
    print(t.sendMailFromChinaSale(mode_name='测试邮件_EOF', environment='yfb', mail_address='howie666@126.com'))
    # print(t.sendMailFromChinaSaleBlacklist(mode_name='测试邮件_短html'))
    # print(t.sendMailFromChinaProdC(mode_name='测试邮件_短html'))
    # print(t.sendMailFromChinaProdCBlacklist(mode_name='测试邮件_短html'))
    # print(t.sendMailFromChinaProdH(mode_name='测试邮件_短html'))
    # print(t.sendMailFromChinaProdHBlacklist(mode_name='测试邮件_短html'))
    # print(t.sendMailFromThailandSale(mode_name='测试邮件_短html'))
    # print(t.sendMailFromThailandSaleBlacklist(mode_name='测试邮件_短html'))
    # print(t.sendMailFromThailandProdC(mode_name='测试邮件_短html'))
    # print(t.sendMailFromThailandProdCBlacklist(mode_name='测试邮件_短html'))
    # print(t.sendMailFromThailandProdH(mode_name='测试邮件_短html'))
    # print(t.sendMailFromThailandProdHBlacklist(mode_name='测试邮件_短html'))
    # print(t.sendMailFromIndonesiaSale(mode_name='测试邮件_短html'))
    # print(t.sendMailFromIndonesiaSaleBlacklist(mode_name='测试邮件_短html'))
    # print(t.sendMailFromIndonesiaProdC(mode_name='测试邮件_短html'))
    # print(t.sendMailFromIndonesiaProdCBlacklist(mode_name='测试邮件_短html'))
    # print(t.sendMailFromIndonesiaProdH(mode_name='测试邮件_短html'))
    # print(t.sendMailFromIndonesiaProdHBlacklist(mode_name='测试邮件_短html'))