import unittest
from healthvaultlib.tests.testbase import TestBase
from healthvaultlib.itemtypes.height import Height
from healthvaultlib.methods.putthings import PutThings
from healthvaultlib.methods.authorizeapplication import AuthorizeApplication
from healthvaultlib.exceptions.healthserviceexception import HealthServiceException
from healthvaultlib.methods.removeapplicationrecordauthorization import RemoveApplicationRecordAuthorization


class TestAuthDeauth(TestBase):

    @unittest.skip('Run explicitly as deauths person')
    def test_01_deauth(self):
        # Deauth
        method = RemoveApplicationRecordAuthorization()
        method.execute(self.connection)
        with self.assertRaises(HealthServiceException):
            self.create_item()
    
    @unittest.skip('Yet to figure out how to call this method')
    def test_02_auth(self):
        # Auth
        method = AuthorizeApplication(self.connection.applicationid)
        method.execute(self.connection)
        self.create_item()

    def create_item(self):
        h1 = self.get_height_object(1.20)
        method = PutThings([h1])
        method.execute(self.connection)

    def get_height_object(self, value_m):
        height = Height()
        height.value_m = value_m
        height.display_value = str(value_m * 100)
        height.display_units = 'cm'
        return height
