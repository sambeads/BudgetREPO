import requests

def logger():
	payload = {'auth_userId':'','auth_passwd':''}
	with requests.Session() as session:
		#login = requests.get('https://secure07b.chase.com/web/auth/dashboard#/dashboard/overviewAccounts/overview/index')
		#print(login)
		page = session.post('https://secure07b.chase.com/auth/fcc/login',payload)
		print(page.text)

if __name__ == '__main__':
	logger()
