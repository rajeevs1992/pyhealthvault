import pytz
import datetime

from lxml import etree

from healthvaultlib.hvcrypto import HVCrypto
from methodbase import RequestBase, ResponseBase

class CreateAuthenticatedSessionTokenRequest(RequestBase):

    applicationid = None
    
    def __init__(self, appid):
        self.name = 'CreateAuthenticatedSessionToken'
        self.version = 2
        self.applicationid = appid

    def get_info(self):
        content = self.construct_content()
        info = self.construct_info(content)
        return 

    def construct_content(self):
        content = etree.Element('content')

        appid = etree.Element('app-id')
        appid.text = self.applicationid
        content.append(appid)

        _hmac = etree.Element('hmac')
        _hmac.text = 'HMACSHA256'
        content.append(_hmac)

        signing_time = etree.Element('signing-time')
        signing_time.text = datetime.datetime.now(pytz.utc).isoformat()
        content.append(signing_time)

        return content

    def construct_info(self, content):
        info = etree.Element('info')
        auth_info = etree.Element('auth-info')
        app_id = etree.Element('app-id')
        app_id.text = self.applicationid
        auth_info.append(app_id)
        info.append(auth_info)

        crypto = HVCrypto()

        credential = etree.Element('credential')
        appserver2 = etree.Element('appserver2')
        sig = etree.Element('sig', digestMethod='SHA1', sigMethod='RSA-SHA1', thumbprint=self.thumbprint)
        sig.text = crypto.sign(etree.tostring(content))
        appserver2.append(sig)

        appserver2.append(content)
        credential.append(appserver2)
        auth_info.append(credential)
        info.append(auth_info)

        return info

class CreateAuthenticatedSessionTokenResponse(ResponseBase):
    shared_secret = None
    user_auth_token = None
    
    def __init__(self, appid):
        self.name = 'CreateAuthenticatedSessionToken'
        self.version = 2

    def parse_response(self, response):
        response_xml = etree.fromstring(response)
        NSMAP = self.get_info_namespace()
        self.shared_secret = response_xml.xpath('/response/wc:info/shared-secret/text()', namespaces = NSMAP)[0]
        self.user_auth_token = response_xml.xpath('/response/wc:info/token/text()', namespaces = NSMAP)[0]
