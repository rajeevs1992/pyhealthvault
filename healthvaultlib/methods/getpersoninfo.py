from healthvaultlib.methods.methodbase import RequestBase, ResponseBase
from healthvaultlib.objects.personinfo import PersonInfo

class GetPersonInfoRequest(RequestBase):
    
    def __init__(self):
        self.name = 'GetPersonInfo'
        self.version = '1'

    def get_info(self):
        info = etree.Element('info')
        return info

class GetPersonInfoResponse(ResponseBase):
    personinfo = None

    def __init__(self):
        self.name = 'GetPersonInfo'
        self.version = '1'

    def parse_response(self, response):
        self.parse_info(response)
        self.personinfo = PersonInfo(self.info)
