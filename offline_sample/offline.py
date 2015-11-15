from healthvaultlib.helpers.connection import Connection
from healthvaultlib.methods.getthings import GetThings
from settings import *

def main():
    conn = Connection(HV_APPID, HV_SERVICE_SERVER)
    conn.thumbprint = APP_THUMBPRINT
    conn.connect()
    conn.set_person_and_record('214ade00-dbc1-448a-b409-0762ec814a34', '53ac76dd-c7e7-4d48-ac48-3c22c529704f')

    method = GetThings()
    method.execute(conn)
main()
