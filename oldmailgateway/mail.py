from exchangelib import DELEGATE, Account, Credentials, ServiceAccount

creds = ServiceAccount(
    username='360buyad\wanghongwei47',
    password='Whw230581$')
account = Account(
    primary_smtp_address='wanghongwei47@jd.com',
    credentials=creds,
    autodiscover=True,
    access_type=DELEGATE)
#
# # Print first 100 inbox messages in reverse order
# for item in account.inbox.all().order_by('-datetime_received')[:100]:
#     print(item.subject, item.body, item.attachments)
#     break

# print(account.inbox.)