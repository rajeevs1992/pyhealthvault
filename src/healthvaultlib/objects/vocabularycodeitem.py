from healthvaultlib.utils.xmlutils import XmlUtils


class VocabularyCodeItem:

    def __init__(self, xml=None):
        self.code_value = None
        self.display_text = None
        self.abbreviation_text = None
        self.info_xml = None

        if xml is not None:
            self.parse_xml(xml)

    def parse_xml(self, xml):
        xmlutils = XmlUtils(xml)
        self.code_value = xmlutils.get_string_by_xpath('code-value')
        self.display_text = xmlutils.get_string_by_xpath('display-text')
        self.abbreviation_text = xmlutils.get_string_by_xpath('abbreviation-text')
        info_xml = xml.xpath('info-xml')
        if info_xml != []:
            self.info_xml = info_xml[0]
