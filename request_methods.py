import requests

class GetRequest(object):
  def perform_request(self, url, params=None, headers=None):
    r = requests.get(url, params = params, headers = headers)
    return r

class PostRequest(object):
  def perform_request(self, url, params=None, headers=None):
    r = requests.post(url, params = params, headers = headers)
    return r

class PutRequest(object):
  def perform_request(self, url, params=None, headers=None):
    r = requests.put(url, params = params, headers = headers)
    return r

class DeleteRequest(object):
  def perform_request(self, url, params=None, headers=None):
    r = requests.delete(url, params = params, headers = headers)
    return r

""" HTTP Methods """
class Requests(object):
  GET = GetRequest()
  POST = PostRequest()
  PUT = PutRequest()
  DELETE = DeleteRequest()
