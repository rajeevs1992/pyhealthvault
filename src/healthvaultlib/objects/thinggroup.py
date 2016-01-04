from lxml import etree


class ThingGroup():

    def __init__(self, filters):
        self.format = None
        self.filters = filters

    def write_xml(self):
        group = etree.Element('group')
        for i in self.filters:
            group.append(i.write_xml())
        if self.format is not None:
            group.append(self.format.write_xml())
        return group
