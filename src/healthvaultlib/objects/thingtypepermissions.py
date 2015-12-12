from healthvaultlib.utils.xmlutils import XmlUtils
from lxml import etree

class ThingTypePermissions:
    
    def __init__(self, permission_xml=None):
        self.thing_type_id = ''
        self.online_access_permissions = []
        self.offline_access_permissions = []

        if permission_xml is not None:
            self.parse_xml(permission_xml)

    def parse_xml(self, thing_type_permission_xml):
        xmlutils = XmlUtils(thing_type_permission_xml)
        self.thing_type_id = xmlutils.get_string_by_xpath('thing-type-id/text()')
        for perm in thing_type_permission_xml.xpath('online-access-permissions/permission'):
            self.online_access_permissions.append(perm.xpath('./text()')[0])
        for perm in thing_type_permission_xml.xpath('offline-access-permissions/permission'):
            self.offline_access_permissions.append(perm.xpath('./text()')[0])
