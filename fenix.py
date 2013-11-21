"""
FENIX SDK source code :)
"""

import requests
import urllib

class FenixAPI(object):
	def __init__(self):
		"""Hardcoded now... TODO: Read from a properties file"""
		self.app_secret = 'zHaiWfLxfW1Wt8rbwusDAx8lt24Z4PvG0tyzSS7607nxRZb23mTNBqVZzab9KGzU45RMH4z2tn8e4PJ7xDB8OSuTzBE0dBs8BN3vKatTb4rX1BNWcTq'
		self.client_id = '7065221202521'
		self.redirect_uri = 'http://localhost:8000/login'
		self.base_url = 'https://fenix.ist.utl.pt/'
		self.oauth_endpoint = 'oauth/'
		self.api_endpoint = 'api/fenix/'
		self.api_version = 1

	def get_api_url():
		return self.base_url + api_endpoint + 'v' + self.api_version

	def _request(self, endpoint, req_params=None):
		url = self.base_url + endpoint
		r = requests.get(url, params=req_params)
		print(r.url)
		return r

	def _api_request(self, endpoint, req_params=None):
		req_params = req_params or {}
		req_params['access_token'] = self.access_token
		self._request(endpoint, req_params)

	def get_authentication_url(self):
		url = self.base_url + self.oauth_endpoint + 'userdialog?client_id=' + self.client_id + '&redirect_uri=' + self.redirect_uri
		return url

	def set_code(self, code):
		url = self.base_url + self.oauth_endpoint + 'access_token'
		r_params = {'client_id' : self.client_id, 'client_secret' : self.app_secret, 'redirect_uri' : self.redirect_uri, 'code' : code, 'grant_type' : 'authorization_code'}
		r_headers = {'content-type' : 'application/x-www-form-urlencoded'}
		r = requests.post(url, params = r_params, headers = r_headers)
		r_object = r.json()
		if 'error' in r_object:
			print('Error tryng to get an access token')
			print(r_object)
		else:
			self.access_token = r_object['access_token']
			self.refresh_token = r_object['refresh_token']
			self.exprires = r_object['expires_in']

	def get_access_token(self):
		return self.access_token

	def get_refresh_token(self):
		return self.refresh_token

	def get_token_expires(self):
		return self.exprires

