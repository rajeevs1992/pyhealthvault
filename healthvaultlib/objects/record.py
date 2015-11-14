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
        self.id = xmlhelper.get_string_by_xpath('/id/text()')
        self.record_custodian = xmlhelper.get_bool_by_xpath('/record-custodian/text()')
        self.rel_type = xmlhelper.get_int_by_xpath('/rel-type/text()')
        self.rel_name = xmlhelper.get_string_by_xpath('/rel-name/text()')
        self.auth_expires = xmlhelper.get_datetime_by_xpath('/auth-expires/text()')
        self.auth_expired = xmlhelper.get_bool_by_xpath('/auth-expired/text()')
        self.display_name = xmlhelper.get_string_by_xpath('/display-name/text()')
        self.date_created = xmlhelper.get_datetime_by_xpath('/date-created/text()')

