from lxml import etree
from healthvaultlib.utils.xmlutils import XmlUtils
from healthvaultlib.objects.codedvalue import CodedValue
from healthvaultlib.itemtypes.healthrecorditem import HealthRecordItem


class BasicDemographicInformation(HealthRecordItem):

    def __init__(self, thing_xml):
        self.thing_xml = thing_xml
        self.gender = None
        self.birthyear = None
        self.country = None
        self.postcode = None
        self.parse_thing()

    def parse_thing(self):
        super(BasicDemographicInformation, self).parse_thing()
        xmlutils = XmlUtils(self.thing_xml)
        self.gender = xmlutils.get_string_by_xpath('data-xml/basic/gender/text()')
        self.birthyear = xmlutils.get_int_by_xpath('data-xml/basic/birthyear/text()')
        country_node = self.thing_xml.xpath('data-xml/basic/country')
        if country_node:
            self.country = CodedValue(country_node[0])
        self.postcode = xmlutils.get_string_by_xpath('data-xml/basic/postcode/text()')

