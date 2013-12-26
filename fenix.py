"""
FENIX SDK source code :)
"""

import requests
from ConfigParser import SafeConfigParser

""" HTTP Methods """
class Requests(object):
	GET = 0
	POST = 1
	PUT = 2
	DELETE = 3


class FenixAPISingleton(object):
	__instance = None

	"""Make this class a singleton"""
	def __new__(cls):
		if FenixAPISingleton.__instance is None:
			FenixAPISingleton.__instance = object.__new__(cls)
		return FenixAPISingleton.__instance

	def set_val(self, val):
		self.val = val

	def get_val(self):
		return self.val

	def __init__(self):
		""" Read settings from configuration file"""
		parser = SafeConfigParser(allow_no_value = True)
		section = 'fenixedu'
		parser.read('fenixedu.ini')

		self.client_id = parser.get(section, 'client_id')
		self.redirect_uri = parser.get(section, 'redirect_uri')
		self.client_secret = parser.get(section, 'client_secret')
		
		self.base_url = parser.get(section, 'base_url')
		self.api_endpoint = parser.get(section, 'api_endpoint')
		self.api_version = parser.get(section, 'api_version')
		
		""" API specific """
		self.oauth_endpoint = 'oauth'
		self.access_token_endpoint = 'access_token'
		self.access_token = ''
		self.refresh_token = ''
		self.error_key = 'error'

		""" API endpoints """
		self.person_endpoint = 'person'
		self.about_endpoint = 'about'
		self.courses_endpoint = 'courses'
		self.evaluations_endpoint = 'evaluations'
		self.schedule_endpoint = 'schedule'
		self.groups_endpoint = 'groups'
		self.students_endpoint = 'students'
		self.degrees_endpoint = 'degrees'
		self.calendar_endpoint = 'calendar'
		self.payments_endpoint = 'payments'
		self.spaces_endpoint = 'spaces'
		self.classes_endpoint = 'classes'
		self.curriculum_endpoint = 'curriculum'
		self.refresh_token_endpoint = 'refresh_token'
		self.curriculum_endpoint = 'curriculum'

	def _get_api_url(self):
		return self.base_url + self.api_endpoint + 'v' + str(self.api_version)

	""" Method to make a http request
		If no method parameter is passed it will make a Get
			request by default """
	def _request(self, url, params=None, method=None, headers=None):

		if method is None or method == Requests.GET:
			r = requests.get(url, params = params, headers = headers)
		elif method == Requests.POST:
			r = requests.post(url, params = params, headers = headers)
		elif method == Requests.PUT:
			r = requests.put(url, params = params, headers = headers)
		elif method == Requests.DELETE:
			r = requests.delete(url, params = params, headers = headers)
		
		print('API request: ' + r.url)
		return r

	def _api_private_request(self, endpoint, req_params=None, method=None, headers=None):
		req_params = req_params or {}
		url = self._get_api_url() + '/' + endpoint
		req_params['access_token'] = self.access_token
		r = self._request(url, req_params, method, headers = headers)
		""" Check if everything was fine
			If not: Try to refresh the access token """
		if r.status_code == 401:
			self._refresh_access_token()
			""" Repeat the request """
			r = self._request(url, req_params, method, headers = headers)
		return r
	
	def _refresh_access_token(self):
		print('Refreshing access token')
		url = self.base_url + '/' + self.oauth_endpoint + '/' + self.refresh_token_endpoint
		req_params = {'client_id' : self.client_id, 'client_secret' : self.client_secret, 'refresh_token' : self.refresh_token, 
				'grant_type' : 'authorization_code', 'redirect_uri' : self.redirect_uri, 'code' : self.code}
		r_headers = {'content-type' : 'application/x-www-form-urlencoded'}
		r = self._request(url, req_params, Requests.POST, headers = r_headers)
		refresh = r.json()
		self.access_token = refresh['access_token']
		self.exprires = refresh['expires_in']

	def _api_public_request(self, endpoint, params=None, method=None, headers=None):
		url = self._get_api_url() + '/' + endpoint
		return self._request(url, params, method, headers = headers)

	def get_authentication_url(self):
		url = self.base_url + self.oauth_endpoint + '/userdialog?client_id=' + self.client_id + '&redirect_uri=' + self.redirect_uri
		return url

	def set_code(self, code):
		url = self.base_url + self.oauth_endpoint + '/' + self.access_token_endpoint
		r_params = {'client_id' : self.client_id, 'client_secret' : self.client_secret, 'redirect_uri' : self.redirect_uri, 'code' : code, 'grant_type' : 'authorization_code'}
		r_headers = {'content-type' : 'application/x-www-form-urlencoded'}
		r = self._request(url, params = r_params, method = Requests.POST, headers = r_headers)
		r_object = r.json()
		if self.error_key in r_object:
			print('Error tryng to get an access token')
			print(r_object)
		else:
			self.access_token = r_object['access_token']
			self.refresh_token = r_object['refresh_token']
			self.exprires = r_object['expires_in']
			self.code = code

	def set_access_token(self, token):
		self.access_token = token

	def get_access_token(self):
		return self.access_token

	def get_refresh_token(self):
		return self.refresh_token

	def get_token_expires(self):
		return self.exprires

	""" API methods """
	""" Public Endpoints """
	def get_about(self):
		r = self._api_public_request(self.about_endpoint)
		return r.json()

	def get_course(self, id):
		r = self._api_public_request(self.courses_endpoint + '/' + id)
		return r.json()

	def get_course_evaluations(self, id):
		r = self._api_public_request(self.courses_endpoint + '/' + id + '/' + self.evaluations_endpoint)
		return r.json()

	def get_course_groups(self, id):
		r = self._api_public_request(self.courses_endpoint + '/' + id + '/' + self.groups_endpoint)
		return r.json()

	def get_course_schedule(self, id):
		r = self._api_public_request(self.courses_endpoint + '/' + id + '/' + self.schedule_endpoint)
		return r.json()

	def get_course_students(self, id):
		r = self._api_public_request(self.courses_endpoint + '/' + id + '/' + self.students_endpoint)
		return r.json()

	def get_degrees(self, year=None):
		if year:
			params = {'year' : year}
		else:
			params = None
		r = self._api_public_request(self.degrees_endpoint, params)
		return r.json()

	def get_degree(self, id, year=None):
		if year:
			params = {'year' : year}
		else:
			params = None

		r = self._api_public_request(self.degrees_endpoint + '/' + id, params)
		return r.json()

	def get_degree_courses(self, id):
		r = self._api_public_request(self.degrees_endpoint + '/' + id + '/' + self.courses_endpoint)
		return r.json()
	
	def get_spaces(self):
		r = self._api_public_request(self.spaces_endpoint)
		return r.json()

	def get_space(self, id, day=None):
		if day:
			params = {'day' : day}
		else:
			params = None
		r = self._api_public_request(self.spaces_endpoint + '/' + id, params = params)
		return r.json()

	""" Private Endpoints """
	def get_person(self):
		r = self._api_private_request(self.person_endpoint)
		return r.json()

	def get_classes_calendar(self):
		r = self._api_private_request(self.person_endpoint + '/' + self.calendar_endpoint + '/' + self.classes_endpoint)
		return r.json()

	def get_evaluations_calendar(self, format=None):
		r = self._api_private_request(self.person_endpoint + '/' + self.calendar_endpoint + '/' + self.evaluations_endpoint)
		return r.json()

	def get_curriculum(self):
		r = self._api_private_request(self.person_endpoint + '/' + self.curriculum_endpoint)
		return r.json()

	def get_courses(self, sem=None, year=None):
		params = {}

		if sem:
			params['sem'] = sem
		if year:
			params['year'] = year

		r = self._api_private_request(self.person_endpoint + '/' + self.courses_endpoint, params)
		return r.json()

	def get_evaluations(self):
		r = self._api_private_request(self.person_endpoint + '/' + self.evaluations_endpoint)
		return r.json()

	def get_payments(self):
		r = self._api_private_request(self.person_endpoint + '/' + self.payments_endpoint)
		return r.json()

	def enrol_in_evaluation(self, id, enrol_action = None):
		if enrol_action:
			params = {'enrol' : enrol_action}
		else:
			params = None
		r = self._api_private_request(self.person_endpoint + '/' + self.evaluations_endpoint + '/' + id, params, Requests.PUT)
		return r
	
	def get_evaluation(self, id):
		r = self._api_private_request(self.person_endpoint + '/' + self.evaluations_endpoint + '/' + id)
		return r

