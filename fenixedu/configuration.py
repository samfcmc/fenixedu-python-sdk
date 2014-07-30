### API Configuration

try:
  from ConfigParser import SafeConfigParser
except ImportError:
  #For python version 2.x
  from configparser import SafeConfigParser

DEFAULT_BASE_URL = 'https://fenix.tecnico.ulisboa.pt/'
DEFAULT_API_ENDPOINT = 'api/fenix/'
DEFAULT_API_VERSION = '1'
DEFAULT_CONFIG_FILE = 'fenixedu.ini'

class FenixEduConfiguration(object):

  @staticmethod
  def fromConfigFile(filename = DEFAULT_CONFIG_FILE):
    """ Read settings from configuration file"""
    parser = SafeConfigParser()
    section = 'fenixedu'
    parser.read(filename)

    client_id = parser.get(section, 'client_id')
    redirect_uri = parser.get(section, 'redirect_uri')
    client_secret = parser.get(section, 'client_secret')

    base_url = parser.get(section, 'base_url')
    api_endpoint = parser.get(section, 'api_endpoint')
    api_version = parser.get(section, 'api_version')

    return FenixEduConfiguration(client_id = client_id,
                                  redirect_uri = redirect_uri,
                                  client_secret = client_secret,
                                  base_url = base_url,
                                  api_endpoint = api_endpoint,
                                  api_version = api_version)

  def __init__(self, client_id, redirect_uri,
                client_secret, base_url = DEFAULT_BASE_URL,
                api_endpoint = DEFAULT_API_ENDPOINT,
                api_version = DEFAULT_API_VERSION):
    self.client_id = client_id
    self.redirect_uri = redirect_uri
    self.client_secret = client_secret

    self.base_url = base_url
    self.api_endpoint = api_endpoint
    self.api_version = api_version
