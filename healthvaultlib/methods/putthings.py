from lxml import etree

from healthvaultlib.methods.method import Method
from healthvaultlib.methods.methodbase import RequestBase, ResponseBase
from healthvaultlib.objects.thingkey import ThingKey

class PutThingsRequest(RequestBase):
    
    def __init__(self, items):
        self.name = 'PutThings'
        self.version = 2
        self.healthrecorditems = items

    def get_info(self):
        info = etree.Element('info')
        for item in self.healthrecorditems:
            info.append(item.write_xml())
        return info
        
class PutThingsResponse(ResponseBase):

    def __init__(self):
        self.thing_keys = []
        self.name = 'PutThings'
        self.version = 1

    def parse_response(self, response):
        self.parse_info(response)
        for key in self.info.xpath('thing-id'):
            self.thing_keys.append(ThingKey(key))


class PutThings(Method):

    def __init__(self, items):
        self.request = PutThingsRequest(items)
        self.response = PutThingsResponse()
