"""
FENIX SDK source code :)
"""

import requests

class FenixAPI(object):
	def __init__(self):
		"""Hardcoded now... TODO: Read from a properties file"""
		self.app_secret = 'zHaiWfLxfW1Wt8rbwusDAx8lt24Z4PvG0tyzSS7607nxRZb23mTNBqVZzab9KGzU45RMH4z2tn8e4PJ7xDB8OSuTzBE0dBs8BN3vKatTb4rX1BNWcTq'
		self.client_id = '7065221202521'
		self.access_token = ''
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
