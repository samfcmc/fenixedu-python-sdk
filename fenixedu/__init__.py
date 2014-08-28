"""
FENIX SDK source code :)
"""

import requests
from . import user
from . import endpoints
from . import request_methods
from . import configuration

User = user.User
Requests = request_methods.Requests
FenixEduConfiguration = configuration.FenixEduConfiguration
ERROR_KEY = 'error'

class FenixEduClient(object):

	def __init__(self, config):
		self.config = config
		self.api_url = self.config.base_url + self.config.api_endpoint + 'v' + str(self.config.api_version)
		self.oauth_url = self.config.base_url + endpoints.OAUTH

	def _get_api_endpoint_url(self, endpoint, endpoint_params=None):
		url = self.api_url + '/' + endpoint
		if endpoint_params:
			for key, value in endpoint_params.items():
				url = url.replace(':' + key, str(value), 1)

		return url

	def _get_oauth_endpoint_url(self, endpoint):
		return self.oauth_url + '/' + endpoint

	def _add_parameters_to_url(self, url, parameters):
		new_url = url + '?'

		for key, value in parameters.items():
			new_url = new_url + key + '=' + value + '&'

		return new_url

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
		url = self._get_api_endpoint_url(endpoint)

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
		url = self._get_oauth_endpoint_url(self.refresh_token)
		req_params = {'client_id' : self.config.client_id,
									'client_secret' : self.config.client_secret,
									'refresh_token' : user.refresh_token,
									'grant_type' : 'refresh_token',
									'redirect_uri' : self.config.redirect_url,
									'code' : user.code}
		r_headers = {'content-type' : 'application/x-www-form-urlencoded'}
		r = self._request(url, params = req_params, method = Requests.POST, headers = r_headers)
		refresh = r.json()
		user.access_token = refresh['access_token']
		user.token_exprires = refresh['expires_in']

	def _api_public_request(self, endpoint, params=None, method=None, headers=None, endpoint_params=None):
		url = self._get_api_endpoint_url(endpoint, endpoint_params)
		return self._request(url, params, method, headers = headers)

	def get_authentication_url(self):
		auth_url = self._get_oauth_endpoint_url('userdialog')
		params = {'client_id': self.config.client_id, 'redirect_uri': self.config.redirect_uri}

		return self._add_parameters_to_url(auth_url, params)

	def get_user_by_code(self, code):
		url = self._get_oauth_endpoint_url(endpoints.ACCESS_TOKEN)
		r_params = {'client_id' : self.config.client_id,
								'client_secret' : self.config.client_secret,
								'redirect_uri' : self.config.redirect_uri,
								'code' : code,
								'grant_type' : 'authorization_code'}
		r_headers = {'content-type' : 'application/x-www-form-urlencoded'}
		r = self._request(url, params = r_params, method = Requests.POST, headers = r_headers)
		response = r.json()
		if ERROR_KEY in response:
			raise Exception('Error tryng to get an access token')

		access_token = response['access_token']
		refresh_token = response['refresh_token']
		token_expires = response['expires_in']
		user = User(access_token = access_token, refresh_token = refresh_token,
								token_expires = token_expires)

		return user

	""" API methods """
	""" Public Endpoints """
	def get_about(self):
		r = self._api_public_request(endpoints.ABOUT)
		return r.json()

	def get_academic_terms(self):
		r = self._api_public_request(endpoints.ACADEMIC_TERMS)
		return r.json()

	def get_course(self, id):
		r = self._api_public_request(endpoints.COURSE, endpoint_params={'id': id})
		return r.json()

	def get_course_evaluations(self, id):
		r = self._api_public_request(endpoints.COURSE_EVALUATIONS, endpoint_params={'id': id})
		return r.json()

	def get_course_groups(self, id):
		r = self._api_public_request(endpoints.COURSE_GROUPS, endpoint_params={'id': id})
		return r.json()

	def get_course_schedule(self, id):
		r = self._api_public_request(endpoints.COURSE_SCHEDULE, endpoint_params={'id': id})
		return r.json()

	def get_course_students(self, id):
		r = self._api_public_request(endpoints.COURSE_STUDENTS, endpoint_params={'id': id})
		return r.json()

	def get_degrees(self, year=None):
		if year:
			params = {'year' : year}
		else:
			params = None
		r = self._api_public_request(endpoints.DEGREES, params)
		return r.json()

	def get_degree(self, id, year=None):
		if year:
			params = {'year' : year}
		else:
			params = None

		r = self._api_public_request(endpoints.DEGREE, endpoint_params={'id': id})
		return r.json()

	def get_degree_courses(self, id):
		r = self._api_public_request(endpoints.DEGREE_COURSES, endpoint_params={'id': id})
		return r.json()

	def get_spaces(self):
		r = self._api_public_request(endpoints.SPACES)
		return r.json()

	def get_space(self, id, day=None):
		if day:
			params = {'day' : day}
		else:
			params = None
		r = self._api_public_request(endpoints.SPACE, params=params, endpoint_params={'id': id})
		return r.json()

	""" Private Endpoints """
	def get_person(self, user):
		r = self._api_private_request(endpoints.PERSON, user=user)
		return r.json()

	def get_person_classes_calendar(self, user):
		r = self._api_private_request(endpoints.PERSON_CALENDAR_CLASSES, user=user)
		return r.json()

	def get_person_evaluations_calendar(self, user):
		r = self._api_private_request(endpoints.PERSON_CALENDAR_EVALUATIONS, user=user)
		return r.json()

	def get_person_curriculum(self, user):
		r = self._api_private_request(endpoints.PERSON_CURRICULUM, user=user)
		return r.json()

	def get_person_courses(self, user, academicTerm=None):
		params = {}

		if academicTerm:
			params['academicTerm'] = academicTerm

		r = self._api_private_request(endpoints.PERSON_COURSES, params = params, user=user)
		return r.json()

	def get_person_evaluations(self, user):
		r = self._api_private_request(endpoints.PERSON_EVALUATIONS, user=user)
		return r.json()

	def enrol_person_in_evaluation(self, user, id, enrol_action = None):
		if enrol_action:
			params = {'enrol' : enrol_action}
		else:
			params = None
		r = self._api_private_request(endpoints.PERSON_EVALUATION, params = params, method = Requests.PUT, user=user, endpoint_params={'id': id})
		return r

	def get_person_payments(self, user):
		r = self._api_private_request(endpoints.PERSON + '/' + endpoints.PAYMENTS, user=user)
		return r.json()
