from healthvaultlib.utils.xmlutils import XmlUtils

class HealthRecordItem(object):
    
    def __init__(self, thing_xml):
        self.thing_xml = None

        self.thing_id = None
        self.version_stamp = None

        self.type_id = None
        self.type_name = None

        self.thing_state = None
        self.flags = None

        self.effective_date = None

        self.source = None
        self.thing_xml = thing_xml

    def parse_thing(self):
        xmlutils = XmlUtils(self.thing_xml)
        self.thing_id = xmlutils.get_string_by_xpath('thing-id/text()')
        self.version_stamp = xmlutils.get_string_by_xpath('thing-id/@version-stamp')

        self.type_id = xmlutils.get_string_by_xpath('type-id/text()')
        self.type_name = xmlutils.get_string_by_xpath('type-id/@name')

        self.thing_state = xmlutils.get_string_by_xpath('thing-state/text()')
        self.flags = xmlutils.get_int_by_xpath('flags/text()')
        self.effective_date = xmlutils.get_datetime_by_xpath('/thing/eff-date/text()')

        self.source = xmlutils.get_string_by_xpath('data-xml/common/source/text()')
