from healthvaultlib.utils.xmlutils import XmlUtils
from healthvaultlib.objects.vocabularycodeitem import VocabularyCodeItem


class VocabularyCodeSet:

    def __init__(self, code_set_xml=None):
        self.name = None
        self.family = None
        self.version = None
        self.code_item = []
        self.is_vocab_truncated = None

        self.language = None

        if code_set_xml is not None:
            self.parse_xml(code_set_xml)

    def parse_xml(self, xml):
        xmlutils = XmlUtils(xml)
        self.name = xmlutils.get_string_by_xpath('name')
        print self.name
        self.family = xmlutils.get_string_by_xpath('family')
        self.version = xmlutils.get_string_by_xpath('version')
        for item in xml.xpath('code-item'):
            self.code_item.append(VocabularyCodeItem(item))
        self.is_vocab_truncated = xmlutils.get_bool_by_xpath('is-vocab-truncated')
        self.language = xmlutils.get_lang()
