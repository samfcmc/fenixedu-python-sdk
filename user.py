""" User: """
class User(object):
  def __init__(self, access_token = None, refresh_token = None,
                token_expires = None):
    self.access_token = access_token
    self.refresh_token = refresh_token
    self.token_expires = token_expires
