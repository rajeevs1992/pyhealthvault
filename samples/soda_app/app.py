import urllib
import settings
import webbrowser
from healthvaultlib.helpers.connection import Connection
from healthvaultlib.methods.getauthorizedpeople import GetAuthorizedPeople
from healthvaultlib.methods.newapplicationcreationinfo import NewApplicationCreationInfo
from healthvaultlib.objects.getauthorizedpeopleparameters import GetAuthorizedPeopleParameters

def main():
    conn = Connection(settings.SODA_MASTER_APPID, settings.HV_SERVICE_SERVER)

    method = NewApplicationCreationInfo()
    method.execute(conn)


    app_token = method.response.app_token

    qs = {}
    qs['appCreationToken'] = app_token
    qs['appid'] = conn.applicationid
    qs['instanceName'] = 'PythonSoda'

    target_qs = urllib.urlencode(qs)
    target_qs = urllib.quote_plus(target_qs)
    app_creation_url = '%s/redirect.aspx?target=CREATEAPPLICATION&targetqs=%s'
    req_url = app_creation_url % (settings.HV_SHELL_URL, target_qs)
    print req_url
    webbrowser.open(req_url)
    print 'Press enter after auth'
    raw_input()

    conn.applicationid = method.response.app_id
    conn.soda_shared_secret = method.response.shared_secret

    conn.connect()

    getpeople = GetAuthorizedPeople(GetAuthorizedPeopleParameters())
    getpeople.execute(conn)

    print 'Welcome to SODA, %s' % getpeople.response.authorized_people[0].name

main()
