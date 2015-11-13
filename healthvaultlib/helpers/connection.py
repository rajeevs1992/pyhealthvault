from methods.create_authenticated_session_token import CreateAuthenticatedSessionTokenRequest
from methods.create_authenticated_session_token import CreateAuthenticatedSessionTokenResponse
from methods.getpersoninfo import GetPersonInfoRequest, GetPersonInfoResponse
from methods.method import Method
from helpers.requestmanager import RequestManager


class Connection:
    applicationid = None
    shared_secret = None
    user_auth_token = None
    personid = None
    recordid = None

    isauthenticated = False

    def __init__(self, appid):
        self.applicationid = appid

    def connect(self):
        cast_request = CreateAuthenticatedSessionTokenRequest(self.applicationid)
        cast_response = CreateAuthenticatedSessionTokenResponse()
        method = Method(cast_request, cast_response)

        requestmgr = RequestManager(method, self)
        requestmgr.makerequest()

        self.shared_secret = requestmgr.response.shared_secret
        self.user_auth_token = requestmgr.response.user_auth_token
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
        self.set_person_and_record(requestmgr.response.personid, requestmgr.response.recordid)
