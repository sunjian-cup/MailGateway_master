import json
import requests

def getUrl(host, interface, alias, method, appid):
    url = 'http://{}/{}/{}/{}/{}/jsf'.format(host, interface, alias, method, appid)
    return url

def getHeader(token=''):
    return {'token': token}

def getBody(account='', token='', type='', mail_info={}):
    body = {}
    body['account'] = account
    body['token'] = token
    body['tpye'] = type
    for info in mail_info:
        body[info] = mail_info[info]
    return json.dumps(body)

def send(url, header, body):
    response = requests.post(url=url, headers=header, data=body)
    return response.text