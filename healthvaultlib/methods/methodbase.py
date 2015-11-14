from lxml import etree

class MethodBase:
    name = ''
    version = 1

    def __init__(self, name, version):
        self.name = name
        self.version = version

class RequestBase(MethodBase):
    
    def __init__(self):
        pass


class ResponseBase(MethodBase):
    info = None

    def __init__(self):
        pass

    def get_info_namespace(self):
        return {'wc' : ('urn:com.microsoft.wc.methods.response.%s%d' % (self.name, self.version))}

    def parse_info(self, response):
        NSMAP = self.get_info_namespace()
        self.info = response.xpath('/response/wc:info', namespaces=NSMAP)[0]
