import requests
import bs4
import utils

def logger(configurationfile):
    payload = {'auth_userId': configurationfile.get(
        'auth_userId'), 'auth_passwd': configurationfile.get('auth_passwd')}
    
    with requests.Session() as session:
        # login = requests.get('https://secure07b.chase.com/web/auth/dashboard#/dashboard/overviewAccounts/overview/index')
        # print(login)
        login_page = 'https://secure07b.chase.com/auth/fcc/login'
        #page = session.post(
            #login_page, headers = payload)
        #get = session.get(login_page)
        print(page.text)

if __name__ == '__main__':
	config = utils.read_config_file()
	logger(config)