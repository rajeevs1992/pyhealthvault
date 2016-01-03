from lxml import etree

from healthvaultlib.methods.method import Method
from healthvaultlib.objects.vocabularykey import VocabularyKey
from healthvaultlib.objects.vocabularycodeset import VocabularyCodeSet
from healthvaultlib.methods.methodbase import RequestBase, ResponseBase



class GetVocabularyRequest(RequestBase):

    def __init__(self):
        super(GetVocabularyRequest, self).__init__()
        self.name = 'GetVocabulary'
        self.version = 2
        self.vocabulary_parameters = None

    def get_info(self):
        info = etree.Element('info')
        if self.vocabulary_parameters is not None:
            info.append(self.vocabulary_parameters.write_xml())
        return info


class GetVocabularyResponse(ResponseBase):

    def __init__(self):
        super(GetVocabularyResponse, self).__init__()
        self.vocabulary_key = []
        self.vocabulary_code_set = []
        self.name = 'GetVocabulary'
        self.version = 1

    def parse_response(self, response):
        self.parse_info(response)
        for key in self.info.xpath('vocabulary-key'):
            self.vocabulary_key.append(VocabularyKey(key))
        for code_set in self.info.xpath('vocabulary'):
            self.vocabulary_code_set.append(VocabularyCodeSet(code_set))


class GetVocabulary(Method):

    def __init__(self):
        self.request = GetVocabularyRequest()
        self.response = GetVocabularyResponse()
