from lxml import etree
from healthvaultlib.itemtypes.healthrecorditem import HealthRecordItem
from healthvaultlib.utils.xmlutils import XmlUtils


class WeightGoal(HealthRecordItem):

    def __init__(self, thing_xml):
        self.when = None
        self.display_value = None
        self.thing_xml = thing_xml
        self.parse_thing()

    def parse_thing(self):
        super(WeightGoal, self).parse_thing()
        xmlutils = XmlUtils(self.thing_xml)
        self.when = xmlutils.get_datetime_from_when(self.thing_xml.xpath('data-xml/weightgoal/when')[0])
