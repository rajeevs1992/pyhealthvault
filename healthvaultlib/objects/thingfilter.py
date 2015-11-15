from lxml import etree

class ThingFilter():
    typeids = []

    def __init__(self):
        pass

    def get_xml(self):
        _filter = etree.Element('filter')
        if self.typeids:
            self.add_typeids(_filter)
        return _filter


    def add_typeids(self, _filter):
        for i in self.typeids:
            typeid = etree.Element('type-id')
            typeid.text = i
            _filter.append(typeid)
