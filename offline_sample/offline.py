from healthvaultlib.helpers.connection import Connection
from healthvaultlib.methods.putthings import PutThings
from healthvaultlib.itemtypes.height import Height
from settings import *

def main():
    conn = Connection(HV_APPID, HV_SERVICE_SERVER)
    conn.thumbprint = APP_THUMBPRINT
    conn.connect()
    conn.set_person_and_record('214ade00-dbc1-448a-b409-0762ec814a34', '53ac76dd-c7e7-4d48-ac48-3c22c529704f')

    h = Height()
    h.value_m = 1.89
    h.display_value = '189'
    h.display_units = 'cm'
    method = PutThings([h])
    method.execute(conn)
main()
