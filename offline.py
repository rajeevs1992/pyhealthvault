from healthvaultlib.helpers.connection import Connection
from healthvaultlib.methods.putthings import PutThings
from healthvaultlib.methods.querypermissions import QueryPermissions
from healthvaultlib.itemtypes.height import Height
from settings import *

def main():
    conn = Connection(HV_APPID, HV_SERVICE_SERVER)
    conn.thumbprint = APP_THUMBPRINT
    conn.connect()
    conn.set_person_and_record('214ade00-dbc1-448a-b409-0762ec814a34', '53ac76dd-c7e7-4d48-ac48-3c22c529704f')

    method = QueryPermissions(['822a5e5a-14f1-4d06-b92f-8f3f1b05218f', 'a5033c9d-08cf-4204-9bd3-cb412ce39fc0', '40750a6a-89b2-455c-bd8d-b420a4cb500b'])
    method.execute(conn)

    for i in method.response.permissions:
        print i.thing_type_id
        print i.offline_access_permissions
        print i.online_access_permissions
main()
