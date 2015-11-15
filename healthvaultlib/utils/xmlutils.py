from dateutil import parser
class XmlUtils:
    element = None

    def __init__(self, element = None):
        self.element = element

    def get_string_by_xpath(self, xpath):
        if self.element is None:
            return None
        result = self.element.xpath(xpath)
        if len(result) > 0:
            return result[0]
        return None

    def get_int_by_xpath(self, xpath):
        value = self.get_string_by_xpath(xpath)
        return int(value) if value is not None else None

    def get_bool_by_xpath(self, xpath):
        value = self.get_string_by_xpath(xpath)
        return value == 1 if value is not None else False

    def get_float_by_xpath(self, xpath):
        value = self.get_string_by_xpath(xpath)
        return float(value) if value is not None else None

    def get_datetime_by_xpath(self, xpath):
        value = self.get_string_by_xpath(xpath)
        return parser.parse(value) if value is not None else None

    def get_string(self, attributename):
        value = self.element.get(attributename)
        return value if value is not None else None

    def get_bool(self, attributename):
        value = self.get_string(attributename)
        return value == 1

    def get_int(self, attributename):
        value = self.get_string(attributename)
        return int(value) if value is not None else None

    def get_float(self, attributename):
        value = self.get_string(attributename)
        return float(value) if value is not None else None

    def get_datetime(self, attributename):
        value = self.get_string(attributename)
        return parser.parse(value) if value is not None else None
