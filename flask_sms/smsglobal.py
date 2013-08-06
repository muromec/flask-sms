from urllib import quote, urlencode
import urllib2

HTTP_RPC_URL = 'http://www.smsglobal.com/http-api.php'

class SMSGlobal(object):
  def __init__(self, app=None):
    if app is not None:
      self.init_app(app)

  def init_app(self, app):
    self.username = app.config['SMSGLOBAL_USER']
    self.password = app.config['SMSGLOBAL_PASSWORD']
    if 'SMSGLOBAL_DEFAULT_FROM' in app.config:
      self.default_from = app.config['SMSGLOBAL_DEFAULT_FROM']
    else:
      self.default_from = None

  def send(self, text, to_num, from_num=None):
    if from_num is None and self.default_from is None:
      raise TypeError("Source number not configured or passed")

    from_num = from_num or self.default_from

    assert hasattr(self, 'username'), "SMS app has no configured username"
    assert hasattr(self, 'password'), "SMS app has no configured password"


    kw = {
      "action": "sendsms",
      "user": self.username,
      "password": self.password,
      "to": to_num,
      "from": from_num,
      "text": quote(text),
    }

    http = getattr(self, '_http_send') or urllib2.urlopen

    http_ret = http(HTTP_RPC_URL, urlencode(kw))
    if hasattr(http_ret, 'read'):
      http_ret.read()
