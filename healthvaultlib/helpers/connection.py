class Connection:
    personid = None
    recordid = None
    shared_secret = None
    wctoken = None

    def __init__(self, personid, recordid, shared_secret, wctoken):
        self.personid = personid
        self.recordid = recordid
        self.shared_secret = shared_secret
        self.wctoken = wctoken
