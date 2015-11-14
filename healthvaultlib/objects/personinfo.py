from healthvaultlib.utils.xmlutils import XmlUtils
from healthvaultlib.objects.record import Record

class PersonInfo():
    personid = None
    name = None
    selected_record_id = None
    more_records = False
    records = []

    def __init__(self, info_element=None):
        if info_element is not None:
            self.parse_xml(info_element)

    def parse_xml(self, info_element):
        xmlutils = XmlUtils(info_element)
        self.personid = xmlutils.get_string_by_xpath('personid/text()')
        self.name = xmlutils.get_string_by_xpath('name/text()')
        self.selected_record_id = xmlutils.get_string_by_xpath('selected-record-id/text()')
        self.more_records = xmlutils.get_bool_by_xpath('more-records/text()')
        if self.more_records:
            records = info_element.xpath('record')
            for i in records:
                self.records.append(Record(i))
