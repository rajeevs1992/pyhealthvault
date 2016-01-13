from healthvaultlib.tests.testbase import TestBase
from healthvaultlib.itemtypes.height import Height
from healthvaultlib.methods.putthings import PutThings


class TestPutThings(TestBase):

    def test_putthings_create(self):
        h1 = self.get_height_object(1.20)
        h2 = self.get_height_object(1.40)

        method = PutThings([h1, h2])
        method.execute(self.connection)

        items = method.response.healthrecorditems

        for item in items:
            self.assertIsNotNone(item.key)

    def test_putthings_edit(self):
        h1 = self.get_height_object(1.20)

        method = PutThings([h1])
        method.execute(self.connection)
        items = method.response.healthrecorditems

        initial_key = items[0].key

        h1.value_m = 1.30
        method = PutThings([h1])
        method.execute(self.connection)
        items = method.response.healthrecorditems

        self.assertNotEqual(initial_key.version_stamp,
                            items[0].key.version_stamp)

    def get_height_object(self, value_m):
        height = Height()
        height.value_m = value_m
        height.display_value = str(value_m * 100)
        height.display_units = 'cm'
        return height
