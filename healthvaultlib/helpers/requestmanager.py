import pytz
import hmac
import base64
import hashlib
import httplib
import datetime

from lxml import etree

from healthvaultlib.exceptions.healthserviceexception import HealthServiceException

class RequestManager():
    
    connection = None

    method = None
    info = None
    header = None
    auth = None

    def __init__(self, method, connection):
        self.method = method
        self.connection = connection

    def construct_request(self):
        self.info = self.method.request.get_info()
        infohash = base64.encodestring(hashlib.sha1(etree.tostring(self.info)).digest()).strip()
        self.header = self.construct_header(infohash)
        if self.connection.shared_secret is not None:
            hashedheader = hmac.new(base64.b64decode(self.connection.shared_secret),
                                    etree.tostring(self.header), hashlib.sha1)
            hashedheader64 = base64.encodestring(hashedheader.digest()).strip()
            self.auth = self.construct_auth(hashedheader64)

    def construct_auth(self, hashedheader):
        auth = etree.Element('auth')

        hmac_data = etree.Element('hmac-data', algName='HMACSHA1')
        hmac_data.text = hashedheader
        auth.append(hmac_data)

        return auth

    def makerequest(self):
        self.construct_request()
        NSMAP = {'wc-request' : 'urn:com.microsoft.wc.request'}
        root_name = etree.QName('urn:com.microsoft.wc.request', 'request')
        request_wrapper = etree.Element(root_name, nsmap=NSMAP)
        if self.auth is not None:
            request_wrapper.append(self.auth)
        request_wrapper.append(self.header)
        request_wrapper.append(self.info)

        print '[REQUEST]'
        print etree.tostring(request_wrapper, pretty_print=True)

        response = self.sendrequest(etree.tostring(request_wrapper))

        print '[RESPONSE]'
        print etree.tostring(response, pretty_print=True)
        
        self.throw_if_error(response)

        self.method.response.parse_response(response)

    def throw_if_error(self, response):
        status_code = int(response.xpath('/response/status/code/text()')[0])
        if status_code != 0:
            error_description = response.xpath('/response/status/error/message/text()')[0]
            raise HealthServiceException(error_description)
       

    def sendrequest(self, request):
        '''
            Recieves a request xml as a string and posts it 
            to the health service url specified in the
            settings.py
        '''
        conn = httplib.HTTPSConnection(self.connection.healthserviceurl, 443)
        conn.putrequest('POST','/platform/wildcat.ashx')
        conn.putheader('Content-Type','text/xml')
        conn.putheader('Content-Length','%d' % len(request))
        conn.endheaders()
        try:
            conn.send(request)
        except socket.error, v:
            if v[0] == 32:      # Broken pipe
                conn.close()
            raise
        response = conn.getresponse().read()
        return etree.fromstring(response)

    def construct_header(self, infohash):
        header = etree.Element('header')
        
        method = etree.Element('method')
        method.text = self.method.request.name
        header.append(method)

        method_version = etree.Element('method-version')
        method_version.text = str(self.method.request.version)
        header.append(method_version)

        if self.connection.recordid is not None:
            record_id = etree.Element('record-id')
            record_id.text = self.connection.recordid
            header.append(record_id)

        if self.connection.personid is not None:
            person_id = etree.Element('person-id')
            person_id.text = self.connection.personid
            header.append(person_id)

        if self.connection.auth_token is not None and self.connection.user_auth_token is not None:
            auth_session = etree.Element('auth-session')

            auth_token = etree.Element('auth-token')
            auth_token.text = self.connection.auth_token
            auth_session.append(auth_token)

            user_auth_token = etree.Element('user-auth-token')
            user_auth_token.text = self.connection.user_auth_token
            auth_session.append(user_auth_token)

            header.append(auth_session)
        else:
            appid = etree.Element('app-id')
            appid.text = self.connection.applicationid
            header.append(appid)

        language = etree.Element('language')
        language.text = 'en'
        header.append(language)

        country = etree.Element('country')
        country.text = 'US'
        header.append(country)

        msg_time = etree.Element('msg-time')
        msg_time.text = datetime.datetime.now().isoformat()
        header.append(msg_time)

        msg_ttl = etree.Element('msg-ttl')
        msg_ttl.text = '3600'
        header.append(msg_ttl)

        version = etree.Element('version')
        version.text = '1.0'
        header.append(version)

        info_hash = etree.Element('info-hash')
        hash_data = etree.Element('hash-data', algName='SHA1')
        hash_data.text = infohash
        info_hash.append(hash_data)
        header.append(info_hash)

        return header
