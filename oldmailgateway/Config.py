import json
import os
import time
import random

def createConfigFile():
    if 'config.json' not in os.listdir('.'):
        with open('config.json', 'w', encoding='utf-8'):
            pass
    else:
        print('配置文件已存在，无需创建')

def getAllConfig():
    with open('config.json', 'r', encoding='utf-8') as f:
        try:
            config_json_data = json.loads(f.read())
        except Exception:
            config_json_data = {}
            print('读取配置文件异常')
        finally:
            return config_json_data


def getJsfOnlineChinaSale():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_china_sale = jsf_data.get('host').get('china')
    interface_china_sale = jsf_data.get('interface')
    method_china_sale = jsf_data.get('method')
    appid_china_sale = jsf_data.get('appid').get('china_sale')
    token_china_sale = jsf_data.get('token').get('china_sale')
    alias_china_sale = jsf_data.get('alias').get('china_sale').get('online')
    return {
        'host': host_china_sale,
        'interface': interface_china_sale,
        'method': method_china_sale,
        'appid': appid_china_sale,
        'token': token_china_sale,
        'alias': alias_china_sale
    }

def getJsfYfbChinaSale():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_china_sale = jsf_data.get('host').get('china')
    interface_china_sale = jsf_data.get('interface')
    method_china_sale = jsf_data.get('method')
    appid_china_sale = jsf_data.get('appid').get('china_sale')
    token_china_sale = jsf_data.get('token').get('china_sale')
    alias_china_sale = jsf_data.get('alias').get('china_sale').get('yfb')
    return {
        'host': host_china_sale,
        'interface': interface_china_sale,
        'method': method_china_sale,
        'appid': appid_china_sale,
        'token': token_china_sale,
        'alias': alias_china_sale
    }

def getJsfOnlineChinaProd():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_china_prod = jsf_data.get('host').get('china')
    interface_china_prod = jsf_data.get('interface')
    method_china_prod = jsf_data.get('method')
    appid_china_prod = jsf_data.get('appid').get('china_prod')
    token_china_prod = jsf_data.get('token').get('china_prod')
    alias_china_prod = jsf_data.get('alias').get('china_prod').get('online')
    return {
        'host': host_china_prod,
        'interface': interface_china_prod,
        'method': method_china_prod,
        'appid': appid_china_prod,
        'token': token_china_prod,
        'alias': alias_china_prod
    }

def getJsfYfbChinaProd():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_china_prod = jsf_data.get('host').get('china')
    interface_china_prod = jsf_data.get('interface')
    method_china_prod = jsf_data.get('method')
    appid_china_prod = jsf_data.get('appid').get('china_prod')
    token_china_prod = jsf_data.get('token').get('china_prod')
    alias_china_prod = jsf_data.get('alias').get('china_prod').get('yfb')
    return {
        'host': host_china_prod,
        'interface': interface_china_prod,
        'method': method_china_prod,
        'appid': appid_china_prod,
        'token': token_china_prod,
        'alias': alias_china_prod
    }

def getJsfOnlineThailand():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_thailand = jsf_data.get('host').get('thailand')
    interface_thailand = jsf_data.get('interface')
    method_thailand = jsf_data.get('method')
    appid_thailand = jsf_data.get('appid').get('thailand')
    token_cthailand = jsf_data.get('token').get('thailand')
    alias_thailand = jsf_data.get('alias').get('thailand').get('online')
    return {
        'host': host_thailand,
        'interface': interface_thailand,
        'method': method_thailand,
        'appid': appid_thailand,
        'token': token_cthailand,
        'alias': alias_thailand
    }

def getJsfYfbThailand():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_thailand = jsf_data.get('host').get('thailand')
    interface_thailand = jsf_data.get('interface')
    method_thailand = jsf_data.get('method')
    appid_thailand = jsf_data.get('appid').get('thailand')
    token_cthailand = jsf_data.get('token').get('thailand')
    alias_thailand = jsf_data.get('alias').get('thailand').get('yfb')
    return {
        'host': host_thailand,
        'interface': interface_thailand,
        'method': method_thailand,
        'appid': appid_thailand,
        'token': token_cthailand,
        'alias': alias_thailand
    }

def getJsfOnlineIndonesia():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_indonesia = jsf_data.get('host').get('indonesia')
    interface_indonesia = jsf_data.get('interface')
    method_indonesia = jsf_data.get('method')
    appid_indonesia = jsf_data.get('appid').get('indonesia')
    token_indonesia = jsf_data.get('token').get('indonesia')
    alias_indonesia = jsf_data.get('alias').get('indonesia').get('online')
    return {
        'host': host_indonesia,
        'interface': interface_indonesia,
        'method': method_indonesia,
        'appid': appid_indonesia,
        'token': token_indonesia,
        'alias': alias_indonesia
    }

def getJsfYfbIndonesia():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_indonesia = jsf_data.get('host').get('indonesia')
    interface_indonesia = jsf_data.get('interface')
    method_indonesia = jsf_data.get('method')
    appid_indonesia = jsf_data.get('appid').get('indonesia')
    token_indonesia = jsf_data.get('token').get('indonesia')
    alias_indonesia = jsf_data.get('alias').get('indonesia').get('yfb')
    return {
        'host': host_indonesia,
        'interface': interface_indonesia,
        'method': method_indonesia,
        'appid': appid_indonesia,
        'token': token_indonesia,
        'alias': alias_indonesia
    }

def getJsfOnlineInternational():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_indonesia = jsf_data.get('host').get('international')
    interface_indonesia = jsf_data.get('interface')
    method_indonesia = jsf_data.get('method')
    appid_indonesia = jsf_data.get('appid').get('international')
    token_indonesia = jsf_data.get('token').get('international')
    alias_indonesia = jsf_data.get('alias').get('international').get('online')
    return {
        'host': host_indonesia,
        'interface': interface_indonesia,
        'method': method_indonesia,
        'appid': appid_indonesia,
        'token': token_indonesia,
        'alias': alias_indonesia
    }

def getJsfYfbInternational():
    all_config_data = getAllConfig()
    jsf_data = all_config_data.get('jsf')
    host_indonesia = jsf_data.get('host').get('international')
    interface_indonesia = jsf_data.get('interface')
    method_indonesia = jsf_data.get('method')
    appid_indonesia = jsf_data.get('appid').get('international')
    token_indonesia = jsf_data.get('token').get('international')
    alias_indonesia = jsf_data.get('alias').get('international').get('yfb')
    return {
        'host': host_indonesia,
        'interface': interface_indonesia,
        'method': method_indonesia,
        'appid': appid_indonesia,
        'token': token_indonesia,
        'alias': alias_indonesia
    }


def getHttpChinaSaleGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_china_sale_general = http_data.get('china').get('sale').get('general').get('account')
    token_china_sale_general = http_data.get('china').get('sale').get('general').get('token')
    type_china_sale_general = http_data.get('china').get('sale').get('type')
    return {
        'account': account_china_sale_general,
        'token': token_china_sale_general,
        'type': type_china_sale_general
    }

def getHttpChinaSaleBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_china_sale_blacklist = http_data.get('china').get('sale').get('blacklist').get('account')
    token_china_sale_blacklist = http_data.get('china').get('sale').get('blacklist').get('token')
    type_china_sale_blacklist = http_data.get('china').get('sale').get('type')
    return {
        'account': account_china_sale_blacklist,
        'token': token_china_sale_blacklist,
        'type': type_china_sale_blacklist
    }

def getHttpChinaProdCGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_china_prod_c_general = http_data.get('china').get('prod_c').get('general').get('account')
    token_china_prod_c_general = http_data.get('china').get('prod_c').get('general').get('token')
    type_china_prod_c_general = http_data.get('china').get('prod_c').get('type')
    return {
        'account': account_china_prod_c_general,
        'token': token_china_prod_c_general,
        'type': type_china_prod_c_general
    }

def getHttpChinaProdCBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_china_prod_c_blacklist = http_data.get('china').get('prod_c').get('blacklist').get('account')
    token_china_prod_c_blacklist = http_data.get('china').get('prod_c').get('blacklist').get('token')
    type_china_prod_c_blacklist = http_data.get('china').get('prod_c').get('type')
    return {
        'account': account_china_prod_c_blacklist,
        'token': token_china_prod_c_blacklist,
        'type': type_china_prod_c_blacklist
    }

def getHttpChinaProdHGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_china_prod_h_general = http_data.get('china').get('prod_h').get('general').get('account')
    token_china_prod_h_general = http_data.get('china').get('prod_h').get('general').get('token')
    type_china_prod_h_general = http_data.get('china').get('prod_h').get('type')
    return {
        'account': account_china_prod_h_general,
        'token': token_china_prod_h_general,
        'type': type_china_prod_h_general
    }

def getHttpChinaProdHBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_china_prod_h_blacklist = http_data.get('china').get('prod_h').get('blacklist').get('account')
    token_china_prod_h_blacklist = http_data.get('china').get('prod_h').get('blacklist').get('token')
    type_china_prod_h_blacklist = http_data.get('china').get('prod_h').get('type')
    return {
        'account': account_china_prod_h_blacklist,
        'token': token_china_prod_h_blacklist,
        'type': type_china_prod_h_blacklist
    }


def getHttpThailandSaleGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_thailand_sale_general = http_data.get('thailand').get('sale').get('general').get('account')
    token_thailand_sale_general = http_data.get('thailand').get('sale').get('general').get('token')
    type_thailand_sale_general = http_data.get('thailand').get('sale').get('type')
    return {
        'account': account_thailand_sale_general,
        'token': token_thailand_sale_general,
        'type': type_thailand_sale_general
    }

def getHttpThailandSaleBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_thailand_sale_blacklist = http_data.get('thailand').get('sale').get('blacklist').get('account')
    token_thailand_sale_blacklist = http_data.get('thailand').get('sale').get('blacklist').get('token')
    type_thailand_sale_blacklist = http_data.get('thailand').get('sale').get('type')
    return {
        'account': account_thailand_sale_blacklist,
        'token': token_thailand_sale_blacklist,
        'type': type_thailand_sale_blacklist
    }

def getHttpThailandProdCGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_thailand_prod_c_general = http_data.get('thailand').get('prod_c').get('general').get('account')
    token_thailand_prod_c_general = http_data.get('thailand').get('prod_c').get('general').get('token')
    type_thailand_prod_c_general = http_data.get('thailand').get('prod_c').get('type')
    return {
        'account': account_thailand_prod_c_general,
        'token': token_thailand_prod_c_general,
        'type': type_thailand_prod_c_general
    }

def getHttpThailandProdCBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_thailand_prod_c_blacklist = http_data.get('thailand').get('prod_c').get('blacklist').get('account')
    token_thailand_prod_c_blacklist = http_data.get('thailand').get('prod_c').get('blacklist').get('token')
    type_thailand_prod_c_blacklist = http_data.get('thailand').get('prod_c').get('type')
    return {
        'account': account_thailand_prod_c_blacklist,
        'token': token_thailand_prod_c_blacklist,
        'type': type_thailand_prod_c_blacklist
    }

def getHttpThailandProdHGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_thailand_prod_h_general = http_data.get('thailand').get('prod_h').get('general').get('account')
    token_thailand_prod_h_general = http_data.get('thailand').get('prod_h').get('general').get('token')
    type_thailand_prod_h_general = http_data.get('thailand').get('prod_h').get('type')
    return {
        'account': account_thailand_prod_h_general,
        'token': token_thailand_prod_h_general,
        'type': type_thailand_prod_h_general
    }

def getHttpThailandProdHBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_thailand_prod_h_blacklist = http_data.get('thailand').get('prod_h').get('blacklist').get('account')
    token_thailand_prod_h_blacklist = http_data.get('thailand').get('prod_h').get('blacklist').get('token')
    type_thailand_prod_h_blacklist = http_data.get('thailand').get('prod_h').get('type')
    return {
        'account': account_thailand_prod_h_blacklist,
        'token': token_thailand_prod_h_blacklist,
        'type': type_thailand_prod_h_blacklist
    }


def getHttpIndonesiaSaleGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_indonesia_sale_general = http_data.get('indonesia').get('sale').get('general').get('account')
    token_indonesia_sale_general = http_data.get('indonesia').get('sale').get('general').get('token')
    type_indonesia_sale_general = http_data.get('indonesia').get('sale').get('type')
    return {
        'account': account_indonesia_sale_general,
        'token': token_indonesia_sale_general,
        'type': type_indonesia_sale_general
    }

def getHttpIndonesiaSaleBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_indonesia_sale_blacklist = http_data.get('indonesia').get('sale').get('blacklist').get('account')
    token_indonesia_sale_blacklist = http_data.get('indonesia').get('sale').get('blacklist').get('token')
    type_indonesia_sale_blacklist = http_data.get('indonesia').get('sale').get('type')
    return {
        'account': account_indonesia_sale_blacklist,
        'token': token_indonesia_sale_blacklist,
        'type': type_indonesia_sale_blacklist
    }

def getHttpIndonesiaProdCGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_indonesia_prod_c_general = http_data.get('indonesia').get('prod_c').get('general').get('account')
    token_indonesia_prod_c_general = http_data.get('indonesia').get('prod_c').get('general').get('token')
    type_indonesia_prod_c_general = http_data.get('indonesia').get('prod_c').get('type')
    return {
        'account': account_indonesia_prod_c_general,
        'token': token_indonesia_prod_c_general,
        'type': type_indonesia_prod_c_general
    }

def getHttpIndonesiaProdCBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_indonesia_prod_c_blacklist = http_data.get('indonesia').get('prod_c').get('blacklist').get('account')
    token_indonesia_prod_c_blacklist = http_data.get('indonesia').get('prod_c').get('blacklist').get('token')
    type_indonesia_prod_c_blacklist = http_data.get('indonesia').get('prod_c').get('type')
    return {
        'account': account_indonesia_prod_c_blacklist,
        'token': token_indonesia_prod_c_blacklist,
        'type': type_indonesia_prod_c_blacklist
    }

def getHttpIndonesiaProdHGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_indonesia_prod_h_general = http_data.get('indonesia').get('prod_h').get('general').get('account')
    token_indonesia_prod_h_general = http_data.get('indonesia').get('prod_h').get('general').get('token')
    type_indonesia_prod_h_general = http_data.get('indonesia').get('prod_h').get('type')
    return {
        'account': account_indonesia_prod_h_general,
        'token': token_indonesia_prod_h_general,
        'type': type_indonesia_prod_h_general
    }

def getHttpIndonesiaProdHBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_indonesia_prod_h_blacklist = http_data.get('indonesia').get('prod_h').get('blacklist').get('account')
    token_indonesia_prod_h_blacklist = http_data.get('indonesia').get('prod_h').get('blacklist').get('token')
    type_indonesia_prod_h_blacklist = http_data.get('indonesia').get('prod_h').get('type')
    return {
        'account': account_indonesia_prod_h_blacklist,
        'token': token_indonesia_prod_h_blacklist,
        'type': type_indonesia_prod_h_blacklist
    }


def getHttpInternationalSaleGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_international_sale_general = http_data.get('international').get('sale').get('general').get('account')
    token_international_sale_general = http_data.get('international').get('sale').get('general').get('token')
    type_international_sale_general = http_data.get('international').get('sale').get('type')
    return {
        'account': account_international_sale_general,
        'token': token_international_sale_general,
        'type': type_international_sale_general
    }

def getHttpInternationalSaleBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_international_sale_blacklist = http_data.get('international').get('sale').get('blacklist').get('account')
    token_international_sale_blacklist = http_data.get('international').get('sale').get('blacklist').get('token')
    type_international_sale_blacklist = http_data.get('international').get('sale').get('type')
    return {
        'account': account_international_sale_blacklist,
        'token': token_international_sale_blacklist,
        'type': type_international_sale_blacklist
    }

def getHttpInternationalProdCGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_international_prod_c_general = http_data.get('international').get('prod_c').get('general').get('account')
    token_international_prod_c_general = http_data.get('international').get('prod_c').get('general').get('token')
    type_international_prod_c_general = http_data.get('international').get('prod_c').get('type')
    return {
        'account': account_international_prod_c_general,
        'token': token_international_prod_c_general,
        'type': type_international_prod_c_general
    }

def getHttpInternationalProdCBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_international_prod_c_blacklist = http_data.get('international').get('prod_c').get('blacklist').get('account')
    token_international_prod_c_blacklist = http_data.get('international').get('prod_c').get('blacklist').get('token')
    type_international_prod_c_blacklist = http_data.get('international').get('prod_c').get('type')
    return {
        'account': account_international_prod_c_blacklist,
        'token': token_international_prod_c_blacklist,
        'type': type_international_prod_c_blacklist
    }

def getHttpInternationalProdHGeneral():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_international_prod_h_general = http_data.get('international').get('prod_h').get('general').get('account')
    token_international_prod_h_general = http_data.get('international').get('prod_h').get('general').get('token')
    type_international_prod_h_general = http_data.get('international').get('prod_h').get('type')
    return {
        'account': account_international_prod_h_general,
        'token': token_international_prod_h_general,
        'type': type_international_prod_h_general
    }

def getHttpInternationalProdHBlacklist():
    all_config_data = getAllConfig()
    http_data = all_config_data.get('http')
    account_international_prod_h_blacklist = http_data.get('international').get('prod_h').get('blacklist').get('account')
    token_international_prod_h_blacklist = http_data.get('international').get('prod_h').get('blacklist').get('token')
    type_international_prod_h_blacklist = http_data.get('international').get('prod_h').get('type')
    return {
        'account': account_international_prod_h_blacklist,
        'token': token_international_prod_h_blacklist,
        'type': type_international_prod_h_blacklist
    }


def createBusinessId():
    return str(time.time()).replace('.', '')+str(random.randint(100, 999))

def getsendMailParameter():
    all_config_data = getAllConfig()
    send_mail_parameter = all_config_data.get('send_mail_parameter')
    send_mail_parameter['businessID'] = createBusinessId()
    return send_mail_parameter


if __name__ == '__main__':
    # print(getJsfYfbIndonesia())
    # print(getHttpIndonesiaSaleBlacklist())
    # print(getsendMailParameter())
    print(createBusinessId())