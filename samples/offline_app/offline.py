from settings import HV_APPID, HV_SERVICE_SERVER
from healthvaultlib.helpers.connection import Connection
from settings import APP_THUMBPRINT, APP_PUBLIC_KEY, APP_PRIVATE_KEY
from healthvaultlib.methods.getvocabulary import GetVocabulary
from healthvaultlib.objects.vocabularyparameters import VocabularyParameters
from healthvaultlib.objects.vocabularykey import VocabularyKey


def main():
    conn = Connection(HV_APPID, HV_SERVICE_SERVER)
    conn.thumbprint = APP_THUMBPRINT
    conn.publickey = APP_PUBLIC_KEY
    conn.privatekey = APP_PRIVATE_KEY
    conn.connect()
    conn.set_person_and_record('214ade00-dbc1-448a-b409-0762ec814a34', '53ac76dd-c7e7-4d48-ac48-3c22c529704f')
    method = GetVocabulary()
    thing = VocabularyKey()
    thing.name = 'thing-types'
    thing.family = 'wc'
    thing.version = '1'

    param = VocabularyParameters([thing])
    #method.request.vocabulary_parameters = param
    method.execute(conn)

    for i in method.response.vocabulary_code_set:
        print i.name
        print i.family
        print i.version

        for j in i.code_item:
            print j.code_value
            print j.display_text

    for i in method.response.vocabulary_key:
        print i.name
        print i.family
        print i.version
        print i.description

main()
