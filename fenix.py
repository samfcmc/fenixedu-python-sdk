"""
FENIX SDK source code :)
"""

import requests
from ConfigParser import SafeConfigParser


class FenixAPI(object):
	def __init__(self):
		""" Read settings from configuration file"""
		parser = SafeConfigParser(allow_no_value = True)
		section = 'fenixedu'
		parser.read('fenixedu.ini')

		self.client_id = parser.get(section, 'client_id') or 'troll'
		self.redirect_uri = parser.get(section, 'redirect_uri')
		self.client_secret = parser.get(section, 'client_secret')
		
		self.base_url = parser.get(section, 'base_url')
		self.api_endpoint = parser.get(section, 'api_endpoint')
		self.api_version = parser.get(section, 'api_version')
		
		""" API specific """
		self.oauth_endpoint = 'oauth/'
		self.access_token = ''
		self.error_key = 'error'

	def _get_api_url(self):
		return self.base_url + self.api_endpoint + 'v' + str(self.api_version)

	def _request(self, url, req_params=None):
		r = requests.get(url, params=req_params)
		print(r.url)
		return r

	def _api_request(self, endpoint, req_params=None):
		req_params = req_params or {}
		url = self._get_api_url() + '/' + endpoint
		req_params['access_token'] = self.access_token
		return self._request(url, req_params)

	def get_authentication_url(self):
		url = self.base_url + self.oauth_endpoint + 'userdialog?client_id=' + self.client_id + '&redirect_uri=' + self.redirect_uri
		return url

	def set_code(self, code):
		url = self.base_url + self.oauth_endpoint + 'access_token'
		r_params = {'client_id' : self.client_id, 'client_secret' : self.client_secret, 'redirect_uri' : self.redirect_uri, 'code' : code, 'grant_type' : 'authorization_code'}
		r_headers = {'content-type' : 'application/x-www-form-urlencoded'}
		r = requests.post(url, params = r_params, headers = r_headers)
		r_object = r.json()
		if self.error_key in r_object:
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

	""" API methods """
	def get_person(self):
		r = self._api_request('person')
		return r.json()

