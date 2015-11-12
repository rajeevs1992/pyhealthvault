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

    def __init__(self):
        pass
