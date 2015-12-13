from healthvaultlib.utils.xmlutils import XmlUtils
from lxml import etree

class ThingTypePermissions:
    
    flags = {}

    def __init__(self, permission_xml=None):
        self.thing_type_id = ''
        self.online_access_permissions = 0
        self.offline_access_permissions = 0
        self.other_settings = {}

        self.init_permission_flags()

        if permission_xml is not None:
            self.parse_xml(permission_xml)

    def parse_xml(self, thing_type_permission_xml):
        xmlutils = XmlUtils(thing_type_permission_xml)
        self.thing_type_id = xmlutils.get_string_by_xpath('thing-type-id/text()')
        for perm in thing_type_permission_xml.xpath('online-access-permissions/permission'):
            self.add_permission(perm.xpath('./text()')[0], True)
        for perm in thing_type_permission_xml.xpath('offline-access-permissions/permission'):
            self.add_permission(perm.xpath('./text()')[0], False)

    def init_permission_flags(self):
        if self.flags:
            return
        self.flags['Read'] = 1
        self.flags['Update'] = 2
        self.flags['Create'] = 4
        self.flags['Delete'] = 8

    def add_permission(self, permission, is_online):
        if is_online:
            self.online_access_permissions |= self.flags[permission]
        else:
            self.offline_access_permissions |= self.flags[permission]
