from lxml import etree

from healthvaultlib.methods.methodbase import RequestBase, ResponseBase
from healthvaultlib.methods.method import Method

class GetThingsRequest(RequestBase):
    
    groups = []
    
    def __init__(self, groups):
        self.name = 'GetThings'
        self.version = 3
        self.groups = groups

    def get_info(self):
        info = etree.Element('info')
        for group in self.groups:
            info.append(group.get_xml())
        return info
        

class GetThingsResponse(ResponseBase):
    
    def __init__(self):
        self.name = 'GetThings'
        self.version = 3

    def parse_response(self, response):
        self.parse_info(response)

class GetThings(Method):

    def __init__(self, groups):
        self.request = GetThingsRequest(groups)
        self.response = GetThingsResponse()
