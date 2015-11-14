from healthvaultlib.methods.create_authenticated_session_token import CreateAuthenticatedSessionTokenRequest
from healthvaultlib.methods.create_authenticated_session_token import CreateAuthenticatedSessionTokenResponse
from healthvaultlib.methods.getpersoninfo import GetPersonInfoRequest, GetPersonInfoResponse
from healthvaultlib.methods.method import Method
from healthvaultlib.helpers.requestmanager import RequestManager


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
        cast_request = CreateAuthenticatedSessionTokenRequest(self)
        cast_response = CreateAuthenticatedSessionTokenResponse()
        method = Method(cast_request, cast_response)

        requestmgr = RequestManager(method, self)
        requestmgr.makerequest()

        self.shared_secret = requestmgr.method.response.shared_secret
        self.auth_token = requestmgr.method.response.auth_token

        self.isauthenticated = True

    def set_person_and_record(self, personid, recordid):
        self.personid = personid
        self.recordid = recordid

    def set_person_and_record_from_personinfo(self):
        if not self.isauthenticated:
            self.connect()
        getpersoninfo_request = GetPersonInfoRequest()
        getpersoninfo_response = GetPersonInfoResponse()
        method = Method(getpersoninfo_request, getpersoninfo_response)
        requestmgr = RequestManager(method, self)
        requestmgr.makerequest()
        self.set_person_and_record(requestmgr.response.personinfo.personid,
                                   requestmgr.response.personinfo.selected_record_id)
