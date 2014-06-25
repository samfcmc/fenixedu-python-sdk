"""
FENIX SDK source code :)
"""

import requests
try:
	from ConfigParser import SafeConfigParser
except ImportError:
	#For python version 2.x
	from configparser import SafeConfigParser

from user import User
import endpoints
from request_methods import Requests

ERROR_KEY = 'error'

class FenixEduAPISingleton(object):
	__instance = None

	__single_user = None

	"""Make this class a singleton"""
	def __new__(cls):
		if FenixEduAPISingleton.__instance is None:
			FenixEduAPISingleton.__instance = object.__new__(cls)
			FenixEduAPISingleton.__single_user = User()
		return FenixEduAPISingleton.__instance

	def set_val(self, val):
		self.val = val

	def get_val(self):
		return self.val

	def __init__(self):
		""" Read settings from configuration file"""
		parser = SafeConfigParser()
		section = 'fenixedu'
		parser.read('fenixedu.ini')

		self.client_id = parser.get(section, 'client_id')
		self.redirect_uri = parser.get(section, 'redirect_uri')
		self.client_secret = parser.get(section, 'client_secret')

		self.base_url = parser.get(section, 'base_url')
		self.api_endpoint = parser.get(section, 'api_endpoint')
		self.api_version = parser.get(section, 'api_version')

	def _get_api_url(self):
		return self.base_url + self.api_endpoint + 'v' + str(self.api_version)

	""" Method to make a http request
		If no method parameter is passed it will make a Get
			request by default """
	def _request(self, url, params=None, method=None, headers=None):

		if method is None:
			method = Requests.GET

		r = method.perform_request(url, params, headers)

		return r

	def _api_private_request(self, endpoint, user, params=None, method=None, headers=None):
		params = params or {}
		url = self._get_api_url() + '/' + endpoint

		params['access_token'] = user.access_token
		r = self._request(url, params = params, method = method, headers = headers)
		""" Check if everything was fine
			If not: Try to refresh the access token """
		if r.status_code == 401:
			self._refresh_access_token(user)
			""" Repeat the request """
			r = self._request(url, params = params, method = method, headers = headers)
		return r

	def _refresh_access_token(self, user):
		url = self.base_url + '/' + endpoints.OAUTH_ENDPOINT + '/' + self.refresh_token_endpoint
		req_params = {'client_id' : self.client_id,
									'client_secret' : self.client_secret,
									'refresh_token' : user.refresh_token,
									'grant_type' : 'refresh_token',
									'redirect_uri' : self.redirect_uri,
									'code' : user.code}
		r_headers = {'content-type' : 'application/x-www-form-urlencoded'}
		r = self._request(url, params = req_params, method = Requests.POST, headers = r_headers)
		refresh = r.json()
		user.access_token = refresh['access_token']
		user.token_exprires = refresh['expires_in']

	def _api_public_request(self, endpoint, params=None, method=None, headers=None):
		url = self._get_api_url() + '/' + endpoint
		return self._request(url, params, method, headers = headers)

	def get_authentication_url(self):
		url = self.base_url + endpoints.OAUTH_ENDPOINT + '/userdialog?client_id=' + self.client_id + '&redirect_uri=' + self.redirect_uri
		return url

	def get_user_by_code(self, code):
		url = self.base_url + endpoints.OAUTH_ENDPOINT + '/' + endpoints.ACCESS_TOKEN_ENDPOINT
		r_params = {'client_id' : self.client_id,
								'client_secret' : self.client_secret,
								'redirect_uri' : self.redirect_uri,
								'code' : code,
								'grant_type' : 'authorization_code'}
		r_headers = {'content-type' : 'application/x-www-form-urlencoded'}
		r = self._request(url, params = r_params, method = Requests.POST, headers = r_headers)
		response = r.json()
		if ERROR_KEY in response:
			print('Error tryng to get an access token')
			print(r_object)

		access_token = response['access_token']
		refresh_token = response['refresh_token']
		token_expires = response['expires_in']
		user = User(access_token = access_token, refresh_token = refresh_token,
								token_expires = token_expires)

		return user

	def set_access_token(self, token):
		self.access_token = token

	def get_access_token(self):
		return self.access_token

	def get_refresh_token(self):
		return self.refresh_token

	def get_token_expires(self):
		return self.exprires

	#Logout
	def logout(self):
		self.access_token = ''

	def user_is_authenticated(self):
		if self.access_token:
			return True
		else:
			return False

	#Logout
	def logout(self):
		self.access_token = ''

	def user_is_authenticated(self):
		if self.access_token:
			return True
		else:
			return False

	""" API methods """
	""" Public Endpoints """
	def get_about(self):
		r = self._api_public_request(endpoints.ABOUT_ENDPOINT)
		return r.json()

	def get_academic_terms(self):
		r = self._api_public_request(endpoints.ACADEMIC_TERMS_ENDPOINT)
		return r.json()

	def get_course(self, id):
		r = self._api_public_request(endpoints.COURSES_ENDPOINT + '/' + id)
		return r.json()

	def get_course_evaluations(self, id):
		r = self._api_public_request(endpoints.COURSES_ENDPOINT + '/' + id + '/' + endpoints.EVALUATIONS_ENDPOINT)
		return r.json()

	def get_course_groups(self, id):
		r = self._api_public_request(endpoints.COURSES_ENDPOINT + '/' + id + '/' + endpoints.GROUPS_ENDPOINT)
		return r.json()

	def get_course_schedule(self, id):
		r = self._api_public_request(endpoints.COURSES_ENDPOINT + '/' + id + '/' + endpoints.SCHEDULE_ENDPOINT)
		return r.json()

	def get_course_students(self, id):
		r = self._api_public_request(endpoints.COURSES_ENDPOINT + '/' + id + '/' + endpoints.STUDENTS_ENDPOINT)
		return r.json()

	def get_degrees(self, year=None):
		if year:
			params = {'year' : year}
		else:
			params = None
		r = self._api_public_request(endpoints.DEGREES_ENDPOINT, params)
		return r.json()

	def get_degree(self, id, year=None):
		if year:
			params = {'year' : year}
		else:
			params = None

		r = self._api_public_request(endpoints.DEGREES_ENDPOINT + '/' + id, params)
		return r.json()

	def get_degree_courses(self, id):
		r = self._api_public_request(endpoints.DEGREES_ENDPOINT + '/' + id + '/' + endpoints.COURSES_ENDPOINT)
		return r.json()

	def get_spaces(self):
		r = self._api_public_request(endpoints.SPACES_ENDPOINT)
		return r.json()

	def get_space(self, id, day=None):
		if day:
			params = {'day' : day}
		else:
			params = None
		r = self._api_public_request(endpoints.SPACES_ENDPOINT + '/' + id, params = params)
		return r.json()

	""" Private Endpoints """
	def get_person(self, user):
		r = self._api_private_request(endpoints.PERSON_ENDPOINT, user=user)
		return r.json()

	def get_person_classes_calendar(self, user):
		r = self._api_private_request(endpoints.PERSON_ENDPOINT + '/' + endpoints.CALENDAR_ENDPOINT + '/' + endpoints.CLASSES_ENDPOINT, user=user)
		return r.json()

	def get_person_evaluations_calendar(self, user):
		r = self._api_private_request(endpoints.PERSON_ENDPOINT + '/' + endpoints.CALENDAR_ENDPOINT + '/' + endpoints.EVALUATIONS_ENDPOINT, user=user)
		return r.json()

	def get_person_curriculum(self, user):
		r = self._api_private_request(endpoints.PERSON_ENDPOINT + '/' + endpoints.CURRICULUM_ENDPOINT, user=user)
		return r.json()

	def get_person_courses(self, user, academicTerm=None):
		params = {}

		if academicTerm:
			params['academicTerm'] = academicTerm

		r = self._api_private_request(endpoints.PERSON_ENDPOINT + '/' + endpoints.COURSES_ENDPOINT, params = params, user=user)
		return r.json()

	def get_person_evaluations(self, user):
		r = self._api_private_request(endpoints.PERSON_ENDPOINT + '/' + endpoints.EVALUATIONS_ENDPOINT, user=user)
		return r.json()

	def get_person_payments(self, user):
		r = self._api_private_request(endpoints.PERSON_ENDPOINT + '/' + endpoints.PAYMENTS_ENDPOINT, user=user)
		return r.json()

	def enrol_person_in_evaluation(self, id, user, enrol_action = None):
		if enrol_action:
			params = {'enrol' : enrol_action}
		else:
			params = None
		r = self._api_private_request(endpoints.PERSON_ENDPOINT + '/' + endpoints.EVALUATIONS_ENDPOINT + '/' + id, params = params, method = Requests.PUT, user=user)
		return r

	def get_person_evaluation(self, id, user):
		r = self._api_private_request(endpoints.PERSON_ENDPOINT + '/' + endpoints.EVALUATIONS_ENDPOINT + '/' + id, user=user)
		return r
