from lxml import etree

class ThingFormat():
    sections = []
    xml = None

    def __init__(self):
        pass

    def get_xml(self):
        _format = etree.Element('format')
        if self.sections:
            self.add_sections(_format)
        if self.xml is not None:
            xml = etree.Element('xml')
            xml.text = self.xml
            _format.append(xml)
        return _format

    def add_sections(self, _filter):
        for i in self.sections:
            section = etree.Element('section')
            section.text = i
            _filter.append(section)
