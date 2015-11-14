from dateutil import parser
class XmlUtils:
    element = None

    def __init__(self, element = None):
        self.element = element

    def get_string_by_xpath(self, xpath):
        if self.element is None:
            return None
        return self.element.xpath(xpath)[0]

    def get_int_by_xpath(self, xpath):
        value = self.get_single_value_by_xpath(xpath)
        return int(value)

    def get_bool_by_xpath(self, xpath):
        value = self.get_single_value_by_xpath(xpath)
        return value == 1

    def get_float_by_xpath(self, xpath):
        value = self.get_single_value_by_xpath(xpath)
        return float(value)

    def get_float_by_xpath(self, xpath):
        value = self.get_single_value_by_xpath(xpath)
        return float(value)

    def get_datetime_by_xpath(self, xpath):
        value = self.get_single_value_by_xpath(xpath)
        return parser.parse(value)
