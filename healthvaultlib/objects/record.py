from lxml import etree
from healthvaultlib.utils.xmlutils import XmlUtils

class Record():
    id = None
    record_custodian = False
    rel_type = None
    rel_name = None
    auth_expires = None
    auth_expired = False
    display_name = None
    date_created = None

    def __init__(self, record_xml=None):
        if record_xml is not None:
            self.parse_xml(record_xml)

    def parse_xml(self, record_xml):
        xmlhelper = XmlUtils(record_xml)
        self.id = xmlhelper.get_string('id')
        self.record_custodian = xmlhelper.get_bool('record-custodian')
        self.rel_type = xmlhelper.get_int('rel-type')
        self.rel_name = xmlhelper.get_string('rel-name')
        self.auth_expires = xmlhelper.get_datetime('auth-expires')
        self.auth_expired = xmlhelper.get_bool('auth-expired')
        self.display_name = xmlhelper.get_string('display-name')
        self.date_created = xmlhelper.get_datetime('date-created')
