from lxml import etree
from healthvaultlib.itemtypes.healthrecorditem import HealthRecordItem
from healthvaultlib.utils.xmlutils import XmlUtils


class BasicDemographicInformation(HealthRecordItem):

    def __init__(self, thing_xml):
        self.display_value = None
        self.thing_xml = thing_xml
        self.parse_thing()

    def parse_thing(self):
        super(BasicDemographicInformation, self).parse_thing()
        xmlutils = XmlUtils(self.thing_xml)
