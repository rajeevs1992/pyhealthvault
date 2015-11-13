import pytz
import hmac
import base64
import hashlib
import httplib
import datetime

from lxml import etree

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
        infohash = base64.encodestring(hashlib.sha1(etree.tostring(info)).digest())
        self.header = self.construct_header(infohash)
        hashedheader = hmac.new(base64.b64decode(self.connection.sharedsec),
                                etree.tostring(self.header), hashlib.sha1)
        self.auth = self.construct_auth(hashedheader)

    def construct_auth(hashedheader):
        auth = etree.Element('auth')

        hmac_data = etree.Element('hmac-data', algName='HMACSHA1')
        hmac_data.text = hashedheader
        auth.append(hmac_data)

        return auth

    def makerequest(self):
        self.construct_request()
        NSMAP = {'wc-request' : 'urn:com.microsoft.wc.request'}
        request_wrapper = etree.Element('wc-request:request', nsmap=NSMAP)
        request_wrapper.append(self.auth)
        request_wrapper.append(self.header)
        request_wrapper.append(self.info)

        response = self.sendrequest(etree.tostring(request_wrapper))
        self.method.response.parse_response(response)

    def sendrequest(request):
        '''
            Recieves a request xml as a string and posts it 
            to the health service url specified in the
            settings.py
        '''
        conn = httplib.HTTPConnection(HV_SERVICE_SERVER)
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
        return conn.getresponse()

    def construct_header(self, infohash):
        header = etree.Element('header')
        
        method = etree.Element('method')
        method.text = self.method.request.name
        header.append(method)

        method_version = etree.Element('method-version')
        method_version.text = self.method.request.version
        header.append(method_version)

        if self.connection.recordid is not None:
            record_id = etree.Element('record-id')
            record_id.text = self.connection.recordid
            header.append(record_id)

        if self.connection.personid is not None:
            person_id = etree.Element('person-id')
            person_id.text = self.connection.personid
            header.append(person_id)

        if self.connection.auth_token is not None and self.connection.wctoken is not None:
            auth_session = etree.Element('auth-session')

            auth_token = etree.Element('auth-token')
            auth_token.text = self.connection.auth_token
            auth_session.append(auth_token)

            user_auth_token = etree.Element('user-auth-token')
            user_auth_token.text = self.connection.wctoken
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
        msg_time.text = datetime.datetime.now(pytz.utc).isoformat()
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