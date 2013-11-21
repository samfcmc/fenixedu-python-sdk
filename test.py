""" Functions to call the api and test it """

import fenix

api = fenix.FenixAPI()
print('Testing Fenix API SDK Python')
auth_url = api.get_authentication_url()
print(auth_url)
