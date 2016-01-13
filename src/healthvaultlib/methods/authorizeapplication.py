from lxml import etree
from healthvaultlib.methods.method import Method
from healthvaultlib.methods.methodbase import RequestBase, ResponseBase


class AuthorizeApplicationRequest(RequestBase):

    def __init__(self, appid):
        super(AuthorizeApplicationRequest, self).__init__()
        self.name = 'AuthorizeApplication'
        self.version = 1
        self.app_id = appid

    def get_info(self):
        info = etree.Element('info')

        appid = etree.Element('app-id')
        appid.text = self.app_id
        info.append(appid)

        return info


class AuthorizeApplicationResponse(ResponseBase):

    def __init__(self):
        super(AuthorizeApplicationResponse, self).__init__()
        self.name = 'AuthorizeApplication'
        self.version = 1
        self.NSMAP = {'wc': 'urn:com.microsoft.wc.methods.response.any'}

    def parse_response(self, response):
        return None


class AuthorizeApplication(Method):

    def __init__(self, appid):
        self.request = AuthorizeApplicationRequest(appid)
        self.response = AuthorizeApplicationResponse()
