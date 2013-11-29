""" Functions to call the api and test it """

import sys
import fenix

api = fenix.FenixAPISingleton()
print('Testing Fenix API SDK Python')
auth_url = api.get_authentication_url()
print(auth_url)
api.set_code(sys.argv[1])
print('Access token: ' + api.get_access_token())
print('Refresh token: ' + api.get_refresh_token())
api._refresh_access_token()
print('New access token: ' + api.get_access_token())

print(api.get_space('2465311230082'))
