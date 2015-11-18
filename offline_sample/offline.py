from healthvaultlib.helpers.connection import Connection
from healthvaultlib.methods.putthings import PutThings
from healthvaultlib.methods.getthings import GetThings
from healthvaultlib.itemtypes.height import Height
from settings import *
from healthvaultlib.objects.thinggroup import ThingGroup
from healthvaultlib.objects.thingfilter import ThingFilter
from healthvaultlib.objects.thingformat import ThingFormat

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

    _filter = ThingFilter()
    _format = ThingFormat()
    _format.sections.append('blobpayload')
    _filter.typeids.append('40750a6a-89b2-455c-bd8d-b420a4cb500b')
    group = ThingGroup([_filter])
    group._format = _format

    method = GetThings([group])
    method.execute(conn)


main()
