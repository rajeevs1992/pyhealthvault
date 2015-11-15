from lxml import etree
from healthvaultlib.itemtypes.healthrecorditem import HealthRecordItem
from healthvaultlib.utils.xmlutils import XmlUtils


class Height(HealthRecordItem):

    def __init__(self, thing_xml):
        self.when = None
        self.display_value = None
        self.value_m = None
        self.thing_xml = thing_xml
        self.parse_thing()

    def parse_thing(self):
        super(Height, self).parse_thing()
        xmlutils = XmlUtils(self.thing_xml)
        self.when = xmlutils.get_datetime_from_when(self.thing_xml.xpath('data-xml/height/when')[0])
        self.value_m = xmlutils.get_float_by_xpath('data-xml/height/value/m/text()')
        display_value =  xmlutils.get_float_by_xpath('data-xml/height/value/display/text()')
        display_unit =  xmlutils.get_string_by_xpath('data-xml/height/value/display/@units')
        self.display_value = "%f%s" % (display_value, display_unit)
