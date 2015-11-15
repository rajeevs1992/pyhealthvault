from healthvaultlib.methods.getpersoninfo import GetPersonInfo
from healthvaultlib.methods.create_authenticated_session_token import CreateAuthenticatedSessionToken


class Connection:
    applicationid = None
    healthserviceurl = None
    thumbprint = None
    shared_secret = None
    auth_token = None
    user_auth_token = None
    personid = None
    recordid = None

    isauthenticated = False

    def __init__(self, appid, healthserviceurl):
        self.applicationid = appid
        self.healthserviceurl = healthserviceurl

    def connect(self):
        method = CreateAuthenticatedSessionToken(self)
        method.execute(self)

        self.shared_secret = method.response.shared_secret
        self.auth_token = method.response.auth_token

        self.isauthenticated = True

    def set_person_and_record(self, personid, recordid):
        self.personid = personid
        self.recordid = recordid

    def set_person_and_record_from_personinfo(self):
        if not self.isauthenticated:
            self.connect()
        method = GetPersonInfo()
        method.execute(self)
        self.set_person_and_record(method.response.personinfo.personid,
                                   method.response.personinfo.selected_record_id)
