from lxml import etree
from healthvaultlib.methods.method import Method
from healthvaultlib.methods.methodbase import RequestBase, ResponseBase


class RemoveApplicationRecordAuthorizationRequest(RequestBase):

    def __init__(self):
        super(RemoveApplicationRecordAuthorizationRequest, self).__init__()
        self.name = 'RemoveApplicationRecordAuthorization'
        self.version = 1

    def get_info(self):
        info = etree.Element('info')
        return info


class RemoveApplicationRecordAuthorizationResponse(ResponseBase):

    def __init__(self):
        super(RemoveApplicationRecordAuthorizationResponse, self).__init__()
        self.name = 'RemoveApplicationRecordAuthorization'
        self.version = 1
        self.NSMAP = {'wc': 'urn:com.microsoft.wc.methods.response.any'}

    def parse_response(self, response):
        return None


class RemoveApplicationRecordAuthorization(Method):

    def __init__(self):
        self.request = RemoveApplicationRecordAuthorizationRequest()
        self.response = RemoveApplicationRecordAuthorizationResponse()
