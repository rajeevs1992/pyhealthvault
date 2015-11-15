from lxml import etree

from healthvaultlib.methods.methodbase import RequestBase, ResponseBase
from healthvaultlib.methods.method import Method

class GetThingsRequest(RequestBase):
    
    def __init__(self):
        self.name = 'GetThings'
        self.version = 3

    def get_info(self):
        info = etree.Element('info')
        group = etree.Element('group')
        _filter = etree.Element('filter')
        type_id = etree.Element('type-id')
        type_id.text = '3d34d87e-7fc1-4153-800f-f56592cb0d17'
        _filter.append(type_id)
        _format = etree.Element('format')
        section = etree.Element('section')
        section.text = 'core'
        xml = etree.Element('xml')
        _format.append(section)
        _format.append(xml)
        group.append(_format)
        info.append(group)
        return info
        

class GetThingsResponse(ResponseBase):
    
    def __init__(self):
        self.name = 'GetThings'
        self.version = 3

    def parse_response(self, response):
        self.parse_info(response)

class GetThings(Method):

    def __init__(self):
        self.request = GetThingsRequest()
        self.response = GetThingsResponse()
